# # --
from DTPySide import *

from session.LobbySession import LobbySession
class FileTable(DTWidget.DTHorizontalTabel):

	fileDropped=Signal(list,list)

	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# text/url_list: 来自内部，["file:///E:/dlcw/2021/7/21/a.txt","https://www.google.com"]；
		#                来自外部，则为windows explorer的drag event自带的url_list
		# FileList: 来自内部，[{
		# 	"y":y,
		# 	"m":m,
		# 	"d":d,
		# 	"type":type,
		# 	"name":name,
		# 	"url":url
		# }]
		#                来自外部，为[]
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)
		
		url_list = []
		file_list=[]
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			
			type=int(self.item(row,0).text())
			y,m,d=map(int,self.item(row,1).text().split("."))
			name=self.item(row,2).text()
			url=self.item(row,3).text().replace(self.Headquarter.library_base+"/","")
			file_list.append({
				"y":y,
				"m":m,
				"d":d,
				"type":type,
				"name":name,
				"url":url
			})

			if self.item(row,0).text()=="0":
				url="file:///"+self.item(row,3).text()
			url_list.append(QUrl(url))
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setUrls(url_list)
		mime.setData("FileList",bytes(json.dumps(file_list),encoding="utf-8"))
		
		drag = QDrag(self)
		drag.setPixmap(QIcon(":/icon/white/white_inbox.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().objectName()==self.objectName():
			# 拖到自己
			event.ignore()
		elif event.mimeData().objectName()!="" and self.objectName()=="LibraryFileTable":
			# 内部不允许拖到LibraryFileTable
			event.ignore()
		elif event.mimeData().hasUrls():
			event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 淦！为什么接受资源管理器拖进来的文件，还得implement这个event。
		# 找这个Bug花了我将近一个小时的时间？！茶屋工作室1.0里就不用的？！！
		event.acceptProposedAction()

	def dropEvent(self, event:QDropEvent):
		url_list=[url.toString() for url in event.mimeData().urls()]
		
		try:
			file_list=json.loads((event.mimeData().data("FileList").data().decode("utf-8")))
		except:
			file_list=[]
		
		self.fileDropped.emit(url_list,file_list)
	
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(150)
		self.setColumn(["Type","Date","File","Url"])
		self.setColumnHidden(3,True)
		self.itemDoubleClicked.connect(self.openFile)
		self.file_icon_provider=QFileIconProvider()
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
	
	def setFileList(self, file_list):
		"""设置filetable为file_list，适用于diary和concept的FileTable

		Args:
			file_list (list): diary line和concept字典中的["file"]对应的list（具有y,m,d,name,type,url属性）
		"""
		self.StoreTableStatus()
		self.Clear()

		row=0
		for file in file_list:
			
			y=file["y"]
			m=file["m"]
			d=file["d"]
			type=file["type"]
			name=file["name"]
			url=file["url"]

			if type==0:
				url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
				file_info=QFileInfo(url)
				icon=self.file_icon_provider.icon(file_info)
			else:
				icon=QIcon(":/icon/white/white_globe.svg")
			
			self.addRow(row,[QTableWidgetItem(str(type)),QTableWidgetItem("%s.%s.%s"%(y,m,d)),QTableWidgetItem(icon,name),QTableWidgetItem(url)])
			row+=1
		
		self.RestoreTableStatus()
	
	def openFile(self):
		url=self.item(self.currentRow(),3).text()
		type=self.item(self.currentRow(),0).text()
		if type=="0":
			try:
				os.startfile(url)
			except Exception as e:
				DTFrame.DTMessageBox(self,"Warning","Could not open file!\n\n%s"%e)
		else:
			os.system("start explorer \"%s\""%url)