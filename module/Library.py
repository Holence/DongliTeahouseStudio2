# # --
from DTPySide import *

from session import LobbySession
from module.Ui_Library import Ui_Library
class Library(QWidget,Ui_Library):
	
	def __init__(self, parent, Headquarter: LobbySession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.fixed_shown_files=None
		self.initializeWindow()
		self.initializeSignal()
		self.showSearch()
	
	def initializeWindow(self):
		self.splitter.setStretchFactor(0,3)
		self.splitter.setStretchFactor(1,1)

		self.fileTab.setHeadquarter(self.Headquarter)
		self.fileTab.fileTable.setObjectName("LibraryFileTable") #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.fileTab.fileList.setObjectName("LibraryFileList") #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		
		self.textList.setHeadquarter(self.Headquarter)
		self.textList.setObjectName("LibraryTextList%s"%len(self.Headquarter.library_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.conceptTable.setHeadquarter(self.Headquarter)
		self.conceptTable.setObjectName("LibraryConceptTable%s"%len(self.Headquarter.library_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName

		self.actionSearch_File.setIcon(IconFromCurrentTheme("search.svg"))
		self.dateEdit.setDate(WhatDayIsToday(1))
		self.dateEdit.setDisplayFormat("yyyy.MM.dd")

	def initializeSignal(self):
		self.actionDelete.triggered.connect(self.deleteCenter)
		self.fileTab.fileDelete.connect(self.deleteFile)
		self.conceptTable.conceptDelete.connect(self.deleteFileConcept)
		self.textList.textDelete.connect(self.deleteFileText)
		
		self.actionSearch_File.triggered.connect(self.lineEdit_search.setFocus)
		
		def slot():
			self.clearFixedShownFiles()
			self.showSearch(clear=True)
			self.fileTab.clearSelection()
			self.fileTab.fileList.scrollToTop()
			self.fileTab.fileTable.scrollToTop()
			
		self.lineEdit_search.returnPressed.connect(slot)

		def slot2():
			self.conceptTable.scrollToTop()
			self.textList.scrollToTop()
			self.textViewer.verticalScrollBar().setValue(0)
			self.showFile(reset=True)
		self.fileTab.fileClicked.connect(slot2)
		self.fileTab.fileDropped.connect(self.addFile)

		self.lineEdit_name.editingFinished.connect(self.saveFileName)
		
		self.tabWidget.currentChanged.connect(self.refreshTab)
		self.conceptTable.conceptDropped.connect(self.addFileConcept)
		self.textList.textDropped.connect(self.addFileText)

		self.conceptTable.conceptSort.connect(self.sortFileConcept)

	def showSearch(self,clear=False):
		search=self.lineEdit_search.text()
		name_list,date_range_list,concept_list,TYPE=self.Headquarter.parseSearchText(search)
		
		# 不写日期范围，就为当日
		if search.strip()=="":
			date_range_list=[WhatDayIsToday(1)]
		
		if name_list==[] and date_range_list==[] and concept_list==[] and TYPE==None:
			self.fileTab.Clear()
			return

		self.fileTab.setFileList(self.Headquarter.getLibraryFileList(name_list,date_range_list,concept_list,TYPE))

		if clear==True:
			self.lineEdit_name.clear()
			self.dateEdit.clear()
			self.conceptTable.Clear()
			self.textList.clear()
			self.textViewer.clear()

	def refreshTab(self, reset=False):
		
		def ShowFileConcept():
			store=self.conceptTable.verticalScrollBar().value()
			self.conceptTable.setConceptIDList(file["concept"])
			if reset==True:
				self.conceptTable.scrollToTop()
			else:
				self.conceptTable.verticalScrollBar().setValue(store)
		
		def showFileTextList():
			# 嘿，listwidget的scrollbar就不需要手动设置
			self.textList.setTextList("Library",file_dict)
		
		def showFileText():
			text=""
			diary_data=self.Headquarter.getDiaryData()
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						flag=False
						for line in diary_data[year][month][day]:
							if List_Intersection_Full(line["file"],[file_dict])!=[]:
								if flag==False:
									text+="### "+QLocale().toString(QDate(int(year),int(month),int(day)),"yyyy.M.d ddd")+"\n\n"
									flag=True
								text+=line["text"]+"\n\n"

			store=self.textViewer.verticalScrollBar().value()
			self.textViewer.setMarkdown(text)
			if reset==True:
				self.textViewer.verticalScrollBar().setValue(0)
			else:
				self.textViewer.verticalScrollBar().setValue(store)
		
		date=self.dateEdit.date()
		name=self.lineEdit_name.text()
		file=self.Headquarter.getLibraryFile(date,name)

		if file!=None:
			file_dict=self.Headquarter.generateDiaryConceptFileDict(date,file["type"],name,file["url"])

			if self.tabWidget.currentIndex()==0:
				ShowFileConcept()
			elif self.tabWidget.currentIndex()==1:
				showFileTextList()
			elif self.tabWidget.currentIndex()==2:
				showFileText()

	def showFile(self, reset=False):
		res=self.fileTab.currentFile()
		if res!=None:
			date,name=res

			self.dateEdit.setDate(date)
			self.lineEdit_name.setText(name)

			self.refreshTab(reset)
		else:
			self.dateEdit.clear()
			self.lineEdit_name.clear()

			self.conceptTable.Clear()
			self.textList.clear()
			self.textViewer.clear()


	def refresh(self):
		row=self.fileTab.currentRow()

		if self.fixed_shown_files==None:
			self.showSearch()
		else:
			self.showFixShownFiles()
		
		if row!=-1:
			self.fileTab.selectRow(row)
		self.showFile()
	
	def saveFileName(self):
		row=self.fileTab.currentRow()
		if row!=-1:
			date,oldname=self.fileTab.currentFile()
			newname=self.lineEdit_name.text()
			if newname!=oldname:
				self.Headquarter.renameLibraryFile(self.dateEdit.date(),oldname,newname)
				self.refresh()

	def addFile(self,url_list,_):
		y,m,d=WhatDayIsToday(0)
		for url in url_list:
			# Library_Data中file添加file
			self.Headquarter.addLibraryFile(QDate(y,m,d),url,[]) # 淦！
		self.showSearch()
	
	def addFileConcept(self,id_list):
		res=self.fileTab.currentFile()
		if res!=None:
			date,name=res

			# file中添加concept
			current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
			if current_file!=None:
				current_file["concept"]=List_Union(current_file["concept"],id_list)
				self.showFile()
				
				# concept中添加file
				file=self.Headquarter.generateDiaryConceptFileDict(date,current_file["type"],name,current_file["url"])
				for id in id_list:
					concept=self.Headquarter.getConcept(id)
					concept["file"]=List_Union_Full(concept["file"],[file])
		else:
			self.conceptTable.Clear()
	
	def addFileText(self,text_list):
		res=self.fileTab.currentFile()
		if res!=None:
			date,name=res
			
			# file中添加concept
			current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
			if current_file!=None:
				
				# text中添加file
				file=self.Headquarter.generateDiaryConceptFileDict(date,current_file["type"],name,current_file["url"])
				for text in text_list:
					line=self.Headquarter.getDiaryDayLine(QDate(text["y"],text["m"],text["d"]),text["index"])
					if file not in line["file"]:
						line["file"].append(file)
			
				self.refreshTab()
				self.textList.setFocus()
		else:
			self.textList.clear()

	###################################################################

	def deleteCenter(self):
		if self.fileTab.fileTable.hasFocus() or self.fileTab.fileList.hasFocus():
			self.deleteFile()
		elif self.conceptTable.hasFocus():
			self.deleteFileConcept()
		elif self.textList.hasFocus():
			self.deleteFileText()
	
	def deleteFile(self):
		delete_file_list=[]
		warning_text=""
		if self.fileTab.stackedWidget.currentIndex()==0:
			for model_index in self.fileTab.fileTable.selectionModel().selectedRows():
				row=model_index.row()

				type=int(self.fileTab.fileTable.item(row,0).text())
				y,m,d=map(int,self.fileTab.fileTable.item(row,1).text().split("."))
				date=QDate(y,m,d)
				name=self.fileTab.fileTable.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.fileTab.fileTable.item(row,4).text())
				delete_file_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))
				if type!=2:
					warning_text+="%s\n"%os.path.join(self.Headquarter.library_base,url)
				else:
					warning_text+="%s\n"%url
		else:
			for model_index in self.fileTab.fileList.selectionModel().selectedRows():
				row=model_index.row()

				url=self.Headquarter.extractFileURL(self.fileTab.fileList.item(row).toolTip().split("\n")[0])
				if url[:4]=="http":
					name=self.fileTab.fileList.item(row).text()
					date=QDate().fromString(name[name.rfind("|")+1:][1:-1],"yyyy.M.d")
					name=name[:name.rfind("|")]
				else:
					y,m,d=url.split("/")[:3]
					date=QDate(int(y),int(m),int(d))
					name=self.fileTab.fileList.item(row).text()

				type=self.Headquarter.getLibraryFile(date,name)["type"]
				delete_file_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))
				if type!=2:
					warning_text+="%s\n"%os.path.join(self.Headquarter.library_base,url)
				else:
					warning_text+="%s\n"%url
		
		if delete_file_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete file:",DTIcon.Question(),warning_text).exec_():
				self.Headquarter.deleteLibraryFile(delete_file_list)
				self.refresh()

	def deleteFileConcept(self):

		warning_text=""
		delete_id_list=[]
		for model_index in self.conceptTable.selectionModel().selectedRows():
			row=model_index.row()
			id=int(self.conceptTable.item(row,0).text())
			delete_id_list.append(id)
			warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
		
		if delete_id_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete linked file in concept:",DTIcon.Question(),warning_text).exec_():
				date=self.dateEdit.date()
				name=self.lineEdit_name.text()
				current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
				file=self.Headquarter.generateDiaryConceptFileDict(date,current_file["type"],name,current_file["url"])

				for id in delete_id_list:
					# concept中删除file
					concept=self.Headquarter.getConcept(id)
					concept["file"].remove(file)
					
					# file中删除concept
					current_file["concept"].remove(id)

				self.showFile()
	
	def deleteFileText(self):
		warning_text=""
		delete_text_list=[]
		for model_index in self.textList.selectionModel().selectedRows():
			index=model_index.row()
			text=self.textList.text_list[index]
			delete_text_list.append(text)
			warning_text+=self.textList.item(index).text()+"\n\n"
		
		if delete_text_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete linked file in text:",DTIcon.Question(),warning_text).exec_():
				date=self.dateEdit.date()
				name=self.lineEdit_name.text()
				current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
				file=self.Headquarter.generateDiaryConceptFileDict(date,current_file["type"],name,current_file["url"])

				for text in delete_text_list:
					line=self.Headquarter.getDiaryDayLine(QDate(text["y"],text["m"],text["d"]),text["index"])
					line["file"].remove(file)
				
				self.refreshTab()
	
	def sortFileConcept(self):
		date=self.dateEdit.date()
		name=self.lineEdit_name.text()
		current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
		current_file["concept"]=[]
		for row in range(self.conceptTable.rowCount()):
			id=int(self.conceptTable.item(row,0).text())
			current_file["concept"].append(id)
		self.refreshTab()
	
	def showFixShownFiles(self):
		self.fileTab.setFileList(self.fixed_shown_files)

	def setFixedShownFiles(self, file_list):
		self.fixed_shown_files=file_list
		self.showFixShownFiles()
	
	def clearFixedShownFiles(self):
		self.fixed_shown_files=None