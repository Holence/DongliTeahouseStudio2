# # --
from DTPySide import *

from session import LobbySession
from module.Ui_Library import Ui_Library
class Library(QWidget,Ui_Library):
	
	def __init__(self, parent, Headquarter: LobbySession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):
		self.splitter.setStretchFactor(0,3)
		self.splitter.setStretchFactor(1,1)

		self.fileTable.setHeadquarter(self.Headquarter)
		self.fileTable.setObjectName("LibraryFileTable") #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.textList.setHeadquarter(self.Headquarter)
		self.textList.setObjectName("LibraryTextList%s"%len(self.Headquarter.library_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.conceptTable.setHeadquarter(self.Headquarter)
		self.conceptTable.setObjectName("LibraryConceptTable%s"%len(self.Headquarter.library_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName

	def initializeSignal(self):
		self.actionDelete.triggered.connect(self.deleteCenter)
		
		self.lineEdit_search.returnPressed.connect(self.showSearch)
		self.fileTable.itemClicked.connect(self.showFile)
		self.fileTable.fileDropped.connect(self.addFile)

		self.lineEdit_name.editingFinished.connect(self.saveFileName)
		
		self.tabWidget.currentChanged.connect(self.refreshTab)
		self.conceptTable.conceptDropped.connect(self.addFileConcept)
		self.textList.textDropped.connect(self.addFileText)

	def showSearch(self):
		search=self.lineEdit_search.text()
		name_list,date_range_list,concept_list,TYPE=self.Headquarter.parseSearchText(search)
		
		# 不写日期范围，就为当日
		if search.strip()=="":
			date_range_list=[WhatDayIsToday(1)]
		
		if name_list==[] and date_range_list==[] and concept_list==[] and TYPE==None:
			self.fileTable.Clear()
			return

		self.fileTable.setFileList(self.Headquarter.getLibraryFileList(name_list,date_range_list,concept_list,TYPE))

		self.lineEdit_name.clear()
		self.dateEdit.clear()
		self.conceptTable.Clear()
		self.textList.clear()
		self.textViewer.clear()

	def refreshTab(self):
		
		def ShowFileConcept():
			self.conceptTable.setConceptIDList(file["concept"])
		
		def showFileTextList():
			self.textList.setTextList("Library",file_dict)
		
		def showFileText():
			text=""
			day_list=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
			diary_data=self.Headquarter.getDiaryData()
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						flag=False
						for line in diary_data[year][month][day]:
							if List_Intersection_Full(line["file"],[file_dict])!=[]:
								if flag==False:
									text+="%s.%s.%s %s\n\n"%(year,month,day,day_list[QDate(int(year),int(month),int(day)).dayOfWeek()-1])
									flag=True
								text+=line["text"]+"\n\n"
			self.textViewer.setMarkdown(text)
		
		date=self.dateEdit.date()
		name=self.lineEdit_name.text()
		file=self.Headquarter.getLibraryFile(date,name)

		if file!=None:
			file_dict=self.Headquarter.generateDiaryConceptFileDict(date,file["type"],name,file["url"])

			self.conceptTable.Clear()
			self.textList.clear()
			self.textViewer.clear()
			if self.tabWidget.currentIndex()==0:
				ShowFileConcept()
			elif self.tabWidget.currentIndex()==1:
				showFileTextList()
			elif self.tabWidget.currentIndex()==2:
				showFileText()

	def showFile(self):
		row=self.fileTable.currentRow()
		if row!=-1:
			date=Str_To_QDate(self.fileTable.item(row,1).text(),".")
			name=self.fileTable.item(row,3).text()

			self.dateEdit.setDate(date)
			self.lineEdit_name.setText(name)

			self.refreshTab()
		else:
			self.dateEdit.clear()
			self.lineEdit_name.clear()

			self.conceptTable.Clear()
			self.textList.clear()
			self.textViewer.clear()


	def refresh(self):
		row=self.fileTable.currentRow()
		self.showSearch()
		
		if row!=-1:
			self.fileTable.setCurrentItem(self.fileTable.item(row,0))
		self.showFile()
	
	def saveFileName(self):
		row=self.fileTable.currentRow()
		if row!=-1:
			oldname=self.fileTable.item(row,3).text()
			newname=self.lineEdit_name.text()
			self.Headquarter.renameLibraryFile(self.dateEdit.date(),oldname,newname)
			self.refresh()

	def addFile(self,url_list,_):
		y,m,d=WhatDayIsToday(0)
		for url in url_list:
			# Library_Data中file添加file
			self.Headquarter.addLibraryFile(QDate(y,m,d),url)
		self.showSearch()
	
	def addFileConcept(self,id_list):
		row=self.fileTable.currentRow()
		if row!=-1:
			date=self.dateEdit.date()
			name=self.lineEdit_name.text()
			
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
		row=self.fileTable.currentRow()
		if row!=-1:
			date=self.dateEdit.date()
			name=self.lineEdit_name.text()
			
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
		if self.fileTable.hasFocus():
			self.deleteFile()
		elif self.conceptTable.hasFocus():
			self.deleteFileConcept()
		elif self.textList.hasFocus():
			self.deleteFileText()
	
	def deleteFile(self):
		delete_file_list=[]
		warning_text="You want to delete file:\n\n"
		for model_index in self.fileTable.selectionModel().selectedRows():
			row=model_index.row()

			type=int(self.fileTable.item(row,0).text())
			y,m,d=map(int,self.fileTable.item(row,1).text().split("."))
			date=QDate(y,m,d)
			name=self.fileTable.item(row,3).text()
			url=self.fileTable.item(row,4).text().replace(self.Headquarter.library_base+"/","")
			delete_file_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))
			if type!=2:
				warning_text+="%s\n"%os.path.join(self.Headquarter.library_base,url)
			else:
				warning_text+="%s\n"%url

		
		if delete_file_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm",warning_text,DTIcon.Question()).exec_():
				self.Headquarter.deleteLibraryFile(delete_file_list)
				self.refresh()

	def deleteFileConcept(self):

		warning_text="You want to delete linked file in concept:\n\n"
		delete_id_list=[]
		for model_index in self.conceptTable.selectionModel().selectedRows():
			row=model_index.row()
			id=int(self.conceptTable.item(row,0).text())
			delete_id_list.append(id)
			warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
		
		if delete_id_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm",warning_text,DTIcon.Question()).exec_():
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
		warning_text="You want to delete linked file in text:\n\n"
		delete_text_list=[]
		for model_index in self.textList.selectionModel().selectedRows():
			index=model_index.row()
			text=self.textList.text_list[index]
			delete_text_list.append(text)
			warning_text+=self.textList.item(index).text()+"\n\n"
		
		if delete_text_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm",warning_text,DTIcon.Question()).exec_():
				date=self.dateEdit.date()
				name=self.lineEdit_name.text()
				current_file=self.Headquarter.getLibraryFile(self.dateEdit.date(),name)
				file=self.Headquarter.generateDiaryConceptFileDict(date,current_file["type"],name,current_file["url"])

				for text in delete_text_list:
					line=self.Headquarter.getDiaryDayLine(QDate(text["y"],text["m"],text["d"]),text["index"])
					line["file"].remove(file)
				
				self.refreshTab()