# # --
from DTPySide import *

from session import LobbySession
from module.Ui_BookmarkParser import Ui_BookmarkParser
class BookmarkParser(Ui_BookmarkParser, QWidget):
	def __init__(self, parent, Headquarter:LobbySession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=Headquarter
		
		self.pushButton_open.clicked.connect(self.openHtml)
		
		self.bookmarkTab.setHeadquarter(self.Headquarter)
		self.bookmarkTab.fileTable.setObjectName("BookmarkFileTable")
		self.bookmarkTab.pushButton_list.hide()
		self.bookmarkTab.pushButton_table.hide()
		
		# 不允许拖到Bookmark中
		self.bookmarkTab.fileTable.setAcceptDrops(False)

		self.folderList.itemClicked.connect(self.showFolder)
	
	def showFolder(self):
		foldername=self.folderList.currentItem().text()
		bookmarks=self.folder_dict[foldername]
		self.bookmarkTab.setFileList(bookmarks)

	def openHtml(self):
		
		def parseData(data_str:str):
			data_str=data_str[data_str.find("base64,")+7:]
			return data_str

		def parseDate(timestamp_str):
			date=QDateTime()
			date.setTime_t(int(timestamp_str))
			date=date.date()
			return date

		def deepin_parse(root,current_folder):
			if root.get("type")==None or root["type"]=="folder":
				
				tail=""
				while True:
					folder_name=root["title"]+tail
					if self.folder_dict.get(folder_name)==None:
						self.folder_dict[folder_name]=[]
						break
					else:
						tail+="*"
						continue
				
				current_folder=folder_name
				for child in root["children"]:
					deepin_parse(child,current_folder)
				
			elif root["type"]=="bookmark":
				date=parseDate(root["add_date"])
				name=root["title"]
				url=root["url"]
				
				if root["icon"]!=None:
					data=parseData(root["icon"])
				else:
					data=-1

				cache_name=date.toString("yyyyMMdd")+name
				self.Headquarter.cache[cache_name]=data

				self.folder_dict[current_folder].append(self.Headquarter.generateDiaryConceptFileDict(date,2,name,url))
				return

		dlg=QFileDialog(self)
		url=dlg.getOpenFileUrl(self,"Open Html",filter="Bookmark (*.html)")[0].url()
		if url!="":
			url=url.replace("file:///","")
			
			import bookmarks_parser
			try:
				bookmarks = bookmarks_parser.parse(url)
			except Exception as e:
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
				return
			
			self.folder_dict={}
			for s in bookmarks:
				current_folder=""
				deepin_parse(s,current_folder)
			
			for folder,bookmarks in self.folder_dict.items():
				self.folderList.addItem(folder)
			
			self.folderList.setCurrentRow(0)
			self.showFolder()