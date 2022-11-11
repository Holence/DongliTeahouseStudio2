# # --
from DTPySide import *

from session import LobbySession
from module.Ui_Concept import Ui_Concept
class Concept(QWidget,Ui_Concept):
	def __init__(self, parent, Headquarter: LobbySession):
		super().__init__(parent=parent)
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.current_id=-1
		self.concept_history_queue=[] # 储存之前访问过的concept的队列

		self.initializeWindow()
		self.initializeSignal()
	
	def initializeWindow(self):
		self.splitter_center.setStretchFactor(0,1)
		self.splitter_center.setStretchFactor(1,4)
		
		self.splitter_whole.setStretchFactor(0,1)
		self.splitter_whole.setStretchFactor(1,2)
		self.splitter_whole.setStretchFactor(2,1)

		self.plainTextEdit_detail.setStyleSheet("font-size:12pt")
		self.textviewer_detail.setStyleSheet("font-size:12pt")

		# 搜索处的concept table只能drag out不能drop in
		self.conceptTable.setDragDropMode(QAbstractItemView.DragOnly)
		self.conceptTable.setHeadquarter(self.Headquarter)
		self.conceptTable.setObjectName("ConceptConceptTable%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName

		self.fileTab.setHeadquarter(self.Headquarter)
		self.fileTab.fileTable.setObjectName("ConceptFileTable%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.fileTab.fileList.setObjectName("ConceptFileList%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.textList.setHeadquarter(self.Headquarter)
		self.textList.setObjectName("ConceptTextList%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		
		self.parentTable.setHeadquarter(self.Headquarter)
		self.parentTable.setObjectName("ParentConceptTable%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.childTree.setHeadquarter(self.Headquarter)
		self.childTree.setObjectName("ConceptTree%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.relativeTable.setHeadquarter(self.Headquarter)
		self.relativeTable.setObjectName("RelativeConceptTable%s"%len(self.Headquarter.concept_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName

		self.lineEdit_parent.setHeadquarter(self.Headquarter)
		self.lineEdit_child.setHeadquarter(self.Headquarter)
		self.lineEdit_relative.setHeadquarter(self.Headquarter)

		self.actionAdd_Concept.setIcon(IconFromCurrentTheme("plus.svg"))
		self.actionAdd_Parent.setIcon(IconFromCurrentTheme("user-plus.svg"))
		self.actionAdd_Child.setIcon(IconFromCurrentTheme("user-plus.svg"))
		self.actionAdd_Relative.setIcon(IconFromCurrentTheme("user-plus.svg"))
		self.actionSearch_Concept.setIcon(IconFromCurrentTheme("search.svg"))
		self.actionSwitch_Detail_Eidt_View.setIcon(IconFromCurrentTheme("slack.svg"))

		self.pushButton_back.setStyleSheet("""
			border: none;
			icon-size: 18px;
			max-height: 24px;
			min-height: 24px;
			min-width: 24px;
			max-width: 24px;
		""")

		self.pushButton_delete.setIcon(IconFromCurrentTheme("trash-2.svg"))
		self.pushButton_delete.setStyleSheet("""
			border: none;
			icon-size: 18px;
			max-height: 24px;
			min-height: 24px;
			min-width: 24px;
			max-width: 24px;
		""")

	def initializeSignal(self):
		# 添加concept
		self.actionAdd_Concept.triggered.connect(self.addConcept)
		self.actionDelete.triggered.connect(self.deleteCenter)
		self.fileTab.fileDelete.connect(self.deleteConceptFile)
		self.textList.textDelete.connect(self.deleteConceptText)
		self.conceptTable.conceptDelete.connect(self.deleteConcept)
		self.parentTable.conceptDelete.connect(self.deleteParent)
		self.childTree.conceptDelete.connect(self.deleteChild)
		self.relativeTable.conceptDelete.connect(self.deleteRelative)
		
		# search
		self.lineEdit_search.textEdited.connect(self.showSearch)
		def slot():
			self.conceptTable.setFocus()
			self.conceptTable.selectRow(0)
		self.lineEdit_search.returnPressed.connect(slot)
		self.actionSearch_Concept.triggered.connect(self.lineEdit_search.setFocus)

		def slot(id):
			self.fileTab.fileList.scrollToTop()
			self.fileTab.fileTable.scrollToTop()
			self.textList.scrollToTop()
			self.textViewer.verticalScrollBar().setValue(0)
			self.stackedWidget.setCurrentIndex(1)
			self.showConcept(id)
		# 点击concept，展示concept
		self.conceptTable.conceptClicked.connect(slot)
		self.conceptTable.conceptReturnPressed.connect(slot)

		#修改concept信息
		self.lineEdit_name.editingFinished.connect(self.saveName)
		self.plainTextEdit_detail.editingFinished.connect(self.saveDetail)

		self.actionSwitch_Detail_Eidt_View.triggered.connect(self.switchDetailEditAndView)
		
		self.checkBox.stateChanged.connect(self.refreshTab)
		self.fileTab.fileDropped.connect(self.addConceptFile)
		self.tabWidget.currentChanged.connect(self.refreshTab)
		self.textList.textDropped.connect(self.addConceptText)

		self.parentTable.conceptDoubleClicked.connect(slot)
		self.parentTable.conceptDropped.connect(self.addParent)
		self.lineEdit_parent.conceptAdd.connect(self.addParent)
		self.actionAdd_Parent.triggered.connect(self.lineEdit_parent.setFocus)
		
		self.childTree.conceptDoubleClicked.connect(slot)
		self.childTree.conceptDropped.connect(self.addChild)
		self.lineEdit_child.conceptAdd.connect(self.addChild)
		self.actionAdd_Child.triggered.connect(self.lineEdit_child.setFocus)

		self.relativeTable.conceptDoubleClicked.connect(slot)
		self.relativeTable.conceptDropped.connect(self.addRelative)
		self.lineEdit_relative.conceptAdd.connect(self.addRelative)
		self.actionAdd_Relative.triggered.connect(self.lineEdit_relative.setFocus)

		self.pushButton_back.clicked.connect(self.showPreviousConcept)
		self.pushButton_back.rightClicked.connect(self.showConceptHistory)

		self.pushButton_delete.clicked.connect(lambda:self.deleteConcept(id=self.current_id))

		self.fileTab.fileTable.fileSorted.connect(self.sortConceptFile)
		self.fileTab.fileTable.fileMoveToTop.connect(self.fileMoveToTop)
		self.fileTab.fileTable.fileMoveToBottom.connect(self.fileMoveToBottom)
		self.parentTable.conceptSort.connect(self.sortConceptParent)
		self.relativeTable.conceptSort.connect(self.sortConceptRelative)
	
	def refresh(self, deleted_id_list=None):
		self.showSearch()

		if type(deleted_id_list)==list:
			new_id=self.current_id
			for id in deleted_id_list:
				if self.current_id==id:
					new_id=-1
					break
				elif self.current_id>id:
					new_id-=1
			self.current_id=new_id
			self.conceptTable.clearSelection()
		else:
			# 有可能因为另一个Concept窗口删除了一个Concept，而导致这里请求不到Concept，于是需要判断一下
			if self.Headquarter.getConcept(self.current_id)==None:
				self.current_id=-1

		self.showConcept(self.current_id,reset=False)
	
	def showSearch(self):
		search=self.lineEdit_search.text()
		concept_id_list=self.Headquarter.getConceptIDList(search)
		self.conceptTable.setConceptIDList(concept_id_list)
		# 有时候按了shift后添加concept，shift没被消除
		self.window().setSelect(False)

	def refreshTab(self, reset=False):
		def showConceptTextList():
			# 嘿，listwidget的scrollbar就不需要手动设置
			self.textList.setTextList("Concept",id_list)
		
		def ShowConceptText():
			text=""
			diary_data=self.Headquarter.getDiaryData()
			for year in diary_data:
				for month in diary_data[year]:
					for day in diary_data[year][month]:
						flag=False
						for line in diary_data[year][month][day]:
							if List_Intersection(line["concept"],id_list)!=[]:
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

		def showConceptFile():
			file_list=[]
			for id in id_list:
				concept=self.Headquarter.getConcept(id)
				file_list+=concept["file"]
			self.fileTab.setFileList(file_list)

			if reset==True:
				self.fileTab.fileList.scrollToTop()
				self.fileTab.fileTable.scrollToTop()
		
		def deepin(root_id):
			child_id_list=self.Headquarter.getConcept(root_id)["child"]
			for child_id in child_id_list:
				if child_id not in id_list:
					id_list.append(child_id)
					deepin(child_id)
		
		if self.current_id!=-1:

			id_list=[]
			state=self.checkBox.checkState()
			if state==Qt.Unchecked:
				self.checkBox.setText(QCoreApplication.translate("Concept","Only Root"))
				id_list.append(self.current_id)
			elif state==Qt.PartiallyChecked:
				self.checkBox.setText(QCoreApplication.translate("Concept","Only Child"))
				deepin(self.current_id)
			elif state==Qt.Checked:
				self.checkBox.setText(QCoreApplication.translate("Concept","Both Root and Child"))
				id_list.append(self.current_id)
				deepin(self.current_id)
			
			if self.tabWidget.currentIndex()==0:
				showConceptFile()
			elif self.tabWidget.currentIndex()==1:
				showConceptTextList()
			else:
				ShowConceptText()


	def showConcept(self, id:int, force=False, reset=True):
		
		if not self.window().isSelect() or force==True:

			# 如果列表中选中的不是这个id，就清空选中，减少一些误导
			row=self.conceptTable.currentRow()
			if row!=-1 and int(self.conceptTable.item(row,0).text())!=id:
				self.conceptTable.clearSelection()
			
			# 保存之前的id到concept_history_queue中
			if self.current_id!=-1:
				if len(self.concept_history_queue)==10:
					self.concept_history_queue.pop()
				if self.current_id not in self.concept_history_queue:
					self.concept_history_queue.insert(0,self.current_id)
				else:
					self.concept_history_queue.remove(self.current_id)
					self.concept_history_queue.insert(0,self.current_id)
				if id in self.concept_history_queue:
					self.concept_history_queue.remove(id)

			self.current_id=id
			if self.current_id!=-1:
				concept=self.Headquarter.getConcept(self.current_id)
				self.lineEdit_name.setText(concept["name"])
				self.window().setWindowTitle("Concept %s"%concept["name"])

				if self.stackedWidget.currentIndex()==0:
					store=self.plainTextEdit_detail.verticalScrollBar().value()
					self.plainTextEdit_detail.setPlainText(concept["detail"])
					self.plainTextEdit_detail.verticalScrollBar().setValue(store)
				else:
					store=self.textviewer_detail.verticalScrollBar().value()
					self.textviewer_detail.setMarkdown(concept["detail"])
					self.textviewer_detail.verticalScrollBar().setValue(store)
				
				self.refreshTab(reset)

				# parent child relative
				self.parentTable.setConceptIDList(concept["parent"])
				self.childTree.setChildTree(self.current_id)
				self.relativeTable.setConceptIDList(concept["relative"])
			else:
				self.lineEdit_name.clear()
				self.window().setWindowTitle("Concept")
				self.plainTextEdit_detail.clear()
				self.fileTab.Clear()
				self.textList.clear()
				self.textViewer.clear()
				self.parentTable.Clear()
				self.childTree.clear()
				self.relativeTable.Clear()
	
	def showPreviousConcept(self):
		if self.concept_history_queue!=[]:
			self.showConcept(self.concept_history_queue[0])

	def showConceptHistory(self):
		pos=self.pushButton_back.pos()
		menu=QMenu()
		
		for id in self.concept_history_queue:

			name=str(id)+" | "+self.Headquarter.getConcept(id)["name"]
			action=QAction(name,self)
			action.triggered.connect(partial(self.showConcept,id))
			menu.addAction(action)

		pos=self.mapToGlobal(pos)+QPoint(0,self.pushButton_back.height())
		menu.exec_(pos)

	def addConcept(self):
		if self.lineEdit_name.hasFocus():
			self.saveName()
		elif self.plainTextEdit_detail.hasFocus():
			self.saveDetail()

		new_concept=self.Headquarter.appendConcept()
		self.showConcept(new_concept["id"],force=True)
		self.showSearch()
		self.conceptTable.clearSelection()
		self.lineEdit_name.setFocus()
		# 有时候按了shift后添加concept，shift没被消除
		self.window().setSelect(False)
	
	def saveName(self):
		if self.current_id!=-1:
			concept=self.Headquarter.getConcept(self.current_id)
			concept["name"]=self.lineEdit_name.text()
			concept["az"]=Str_to_AZ(concept["name"])
			self.showSearch()
			self.window().setWindowTitle("Concept %s"%concept["name"])
	
	def saveDetail(self):
		if self.current_id!=-1:
			concept=self.Headquarter.getConcept(self.current_id)
			concept["detail"]=self.plainTextEdit_detail.toPlainText()
			self.showSearch()

	def switchDetailEditAndView(self):
		if self.stackedWidget.currentIndex()==0:
			# View
			self.stackedWidget.setCurrentIndex(1)
			self.plainTextEdit_detail.clearFocus()
		else:
			
			# Edit
			self.stackedWidget.setCurrentIndex(0)
		self.refresh()
	
	def addConceptFile(self,url_list,file_list):
		if self.current_id!=-1:
			concept=self.Headquarter.getConcept(self.current_id)
			# 外来
			if file_list==[]:
				date=WhatDayIsToday(1)
				for url in url_list:
					
					# Library_Data中file添加file
					res=self.Headquarter.addLibraryFile(date,url,[self.current_id])
					if res!=None:
						name,new_file=res
						
						# concept中添加file
						if type(url)==dict:
							# BookmarkParser来的标准型filedict，就不用去获取网页title了，ymd也不是当日，而是收藏夹中的日期
							file=url
							concept["file"].append(self.Headquarter.generateDiaryConceptFileDict(QDate(file["y"],file["m"],file["d"]),new_file["type"],name,new_file["url"]))
						else:
							concept["file"].append(self.Headquarter.generateDiaryConceptFileDict(date,new_file["type"],name,new_file["url"]))
					else:
						# 失败
						continue
			else:
				# Library_Data中file添加concept id
				for new_file in file_list:
					y=new_file["y"]
					m=new_file["m"]
					d=new_file["d"]
					name=new_file["name"]
					file=self.Headquarter.getLibraryFile(QDate(y,m,d),name)
					if self.current_id not in file["concept"]:
						file["concept"].append(self.current_id)
				
				# concept中添加file
				concept["file"]=List_Union_Full(concept["file"],file_list)

			self.refreshTab()
	
	def addConceptText(self,text_list):
		if self.current_id!=-1:
			
			for text in text_list:
				line=self.Headquarter.getDiaryDayLine(QDate(text["y"],text["m"],text["d"]),text["index"])
				if self.current_id not in line["concept"]:
					line["concept"].append(self.current_id)
			
			self.refreshTab()
			self.textList.setFocus()
		else:
			self.textList.clear()
	
	#############################################################################################

	def addParent(self,id_list):
		if self.current_id!=-1:
			self.Headquarter.addParent(self.current_id,id_list)
			self.parentTable.setConceptIDList(self.Headquarter.getConcept(self.current_id)["parent"])
			self.childTree.setChildTree(self.current_id)
			# 有时候按了shift后添加concept，shift没被消除
			self.window().setSelect(False)
	
	def addChild(self,id_list):
		if self.current_id!=-1:
			self.Headquarter.addChild(self.current_id,id_list)
			self.parentTable.setConceptIDList(self.Headquarter.getConcept(self.current_id)["parent"])
			self.childTree.setChildTree(self.current_id)
			# 有时候按了shift后添加concept，shift没被消除
			self.window().setSelect(False)
	
	def addRelative(self,id_list):
		if self.current_id!=-1:
			self.Headquarter.addRelative(self.current_id,id_list)
			self.relativeTable.setConceptIDList(self.Headquarter.getConcept(self.current_id)["relative"])
			# 有时候按了shift后添加concept，shift没被消除
			self.window().setSelect(False)
	
	#############################################################################################

	def deleteCenter(self):
		if self.conceptTable.hasFocus():
			self.deleteConcept()
		elif self.fileTab.fileTable.hasFocus() or self.fileTab.fileList.hasFocus():
			self.deleteConceptFile()
		elif self.textList.hasFocus():
			self.deleteConceptText()
		elif self.parentTable.hasFocus():
			self.deleteParent()
		elif self.childTree.hasFocus():
			self.deleteChild()
		elif self.relativeTable.hasFocus():
			self.deleteRelative()
	
	def deleteConcept(self, id=None):
		if id!=None:
			delete_id_list=[id]
		else:
			delete_id_list=[]
			for model_index in self.conceptTable.selectionModel().selectedRows():
				row=model_index.row()
				id=int(self.conceptTable.item(row,0).text())	
				delete_id_list.append(id)
	
		warning_text=""
		for id in delete_id_list:
			warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
		
		if delete_id_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete concept:",DTIcon.Question(),warning_text).exec_():
				self.Headquarter.deleteConcept(delete_id_list)
				
				for i in range(len(self.Headquarter.concept_heap)):
					self.Headquarter.concept_heap[i].concept_module.refresh(deleted_id_list=delete_id_list)
	
	def deleteConceptFile(self):
		# Only Root时才能选择删除
		if self.checkBox.checkState()==Qt.Unchecked:
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
					warning_text+="%s\n\n"%name
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
					warning_text+="%s\n\n"%name
			
			if delete_file_list!=[]:
				if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete concept linked file:",DTIcon.Question(),warning_text).exec_():
					concept=self.Headquarter.getConcept(self.current_id)
					
					# concept中去除file
					concept["file"]=List_Difference_Full(concept["file"],delete_file_list)
					
					# Library_Data中file去除concept id
					for delete_file in delete_file_list:
						file=self.Headquarter.getLibraryFile(QDate(delete_file["y"],delete_file["m"],delete_file["d"]),delete_file["name"])
						file["concept"].remove(self.current_id)
					
					self.refreshTab()
		else:
			DTFrame.DTMessageBox(self,"Warning","You can only delete concept file in \"only root\" mode.",DTIcon.Warning())
			return
		
	def deleteConceptText(self):
		# Only Root时才能选择删除
		if self.checkBox.checkState()==Qt.Unchecked:
			warning_text=""
			delete_text_list=[]
			for model_index in self.textList.selectionModel().selectedRows():
				index=model_index.row()
				text=self.textList.text_list[index]
				delete_text_list.append(text)
				warning_text+=self.textList.item(index).text()+"\n\n"
			
			if delete_text_list!=[]:
				if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete linked concept in text:",DTIcon.Question(),warning_text).exec_():

					for text in delete_text_list:
						line=self.Headquarter.getDiaryDayLine(QDate(text["y"],text["m"],text["d"]),text["index"])
						line["concept"].remove(self.current_id)
					
					self.refreshTab()
		else:
			DTFrame.DTMessageBox(self,"Warning","You can only delete concept text in \"only root\" mode.",DTIcon.Warning())
			return

	def deleteParent(self):
		delete_id_list=[]
		warning_text=""
		for model_index in self.parentTable.selectionModel().selectedRows():
			row=model_index.row()
			id=int(self.parentTable.item(row,0).text())
			
			delete_id_list.append(id)
			warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
		
		if delete_id_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete parent:",DTIcon.Question(),warning_text).exec_():
				self.Headquarter.deleteParent(self.current_id,delete_id_list)
				self.parentTable.setConceptIDList(self.Headquarter.getConcept(self.current_id)["parent"])
	
	def deleteChild(self):
		delete_id_list=[]
		not_child_list=[]

		warning_text="You want to delete child:"
		delete_id_str=""
		not_child_warning="The concepts below are not direct child of the root concept, they will not be deleted."
		not_child_str=""
		
		concept=self.Headquarter.getConcept(self.current_id)
		for item in self.childTree.selectedItems():
			id=int(item.text(0))
			if id in concept["child"]:
				if id not in delete_id_list:
					delete_id_list.append(id)
					delete_id_str+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
			else:
				if id not in delete_id_list:
					not_child_list.append(id)
					not_child_str+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])

		if delete_id_list!=[] and not_child_list==[]:
			
			if DTFrame.DTConfirmBox(self,"Delete Confirm",warning_text,DTIcon.Question(),delete_id_str).exec_():
				self.Headquarter.deleteChild(self.current_id,delete_id_list)
				self.childTree.setChildTree(self.current_id)
		elif delete_id_list!=[] and not_child_list!=[]:
			
			if DTFrame.DTConfirmBox(self,"Delete Confirm",warning_text,DTIcon.Question(),delete_id_str+"\n"+not_child_warning+"\n\n"+not_child_str).exec_():
				self.Headquarter.deleteChild(self.current_id,delete_id_list)
				self.childTree.setChildTree(self.current_id)
		elif delete_id_list==[] and not_child_list!=[]:
			DTFrame.DTMessageBox(self,"Warning",not_child_warning,DTIcon.Holo01(),not_child_str)
		else:
			pass


	def deleteRelative(self):
		delete_id_list=[]
		warning_text=""
		for model_index in self.relativeTable.selectionModel().selectedRows():
			row=model_index.row()
			id=int(self.relativeTable.item(row,0).text())
			
			delete_id_list.append(id)
			warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
		
		if delete_id_list!=[]:
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete relative:",DTIcon.Question(),warning_text).exec_():
				self.Headquarter.deleteRelative(self.current_id,delete_id_list)
				self.relativeTable.setConceptIDList(self.Headquarter.getConcept(self.current_id)["relative"])

	def sortConceptFile(self):
		if self.checkBox.checkState()==Qt.Unchecked:
			concept=self.Headquarter.getConcept(self.current_id)
			concept["file"]=[]
			for row in range(self.fileTab.fileTable.rowCount()):
				type=int(self.fileTab.fileTable.item(row,0).text())
				y,m,d=map(int,self.fileTab.fileTable.item(row,1).text().split("."))
				date=QDate(y,m,d)
				name=self.fileTab.fileTable.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.fileTab.fileTable.item(row,4).text())
				new_file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				concept["file"].append(new_file)
		else:
			DTFrame.DTMessageBox(self,"Warning","You can only sort file in \"only root\" mode.",DTIcon.Warning())
		self.refresh()

	def fileMoveToTop(self):
		if self.checkBox.checkState()==Qt.Unchecked:
			selected=[]
			for model_index in self.fileTab.fileTable.selectionModel().selectedRows():
				row=model_index.row()
				selected.append(row)
			
			concept=self.Headquarter.getConcept(self.current_id)
			top=[]
			others=[]
			for row in range(self.fileTab.fileTable.rowCount()):
				type=int(self.fileTab.fileTable.item(row,0).text())
				y,m,d=map(int,self.fileTab.fileTable.item(row,1).text().split("."))
				date=QDate(y,m,d)
				name=self.fileTab.fileTable.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.fileTab.fileTable.item(row,4).text())
				new_file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				if row in selected:
					top.append(new_file)
				else:
					others.append(new_file)
			top.extend(others)
			concept["file"]=top.copy()
		else:
			DTFrame.DTMessageBox(self,"Warning","You can only sort file in \"only root\" mode.",DTIcon.Warning())
		self.refresh()

	def fileMoveToBottom(self):
		if self.checkBox.checkState()==Qt.Unchecked:
			selected=[]
			for model_index in self.fileTab.fileTable.selectionModel().selectedRows():
				row=model_index.row()
				selected.append(row)
			
			concept=self.Headquarter.getConcept(self.current_id)
			bottom=[]
			others=[]
			for row in range(self.fileTab.fileTable.rowCount()):
				type=int(self.fileTab.fileTable.item(row,0).text())
				y,m,d=map(int,self.fileTab.fileTable.item(row,1).text().split("."))
				date=QDate(y,m,d)
				name=self.fileTab.fileTable.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.fileTab.fileTable.item(row,4).text())
				new_file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				if row in selected:
					bottom.append(new_file)
				else:
					others.append(new_file)
			others.extend(bottom)
			concept["file"]=others.copy()
		else:
			DTFrame.DTMessageBox(self,"Warning","You can only sort file in \"only root\" mode.",DTIcon.Warning())
		self.refresh()

	def sortConceptParent(self):
		concept=self.Headquarter.getConcept(self.current_id)
		concept["parent"]=[]
		for row in range(self.parentTable.rowCount()):
			id=int(self.parentTable.item(row,0).text())
			concept["parent"].append(id)
		self.refresh()
	
	def sortConceptRelative(self):
		concept=self.Headquarter.getConcept(self.current_id)
		concept["relative"]=[]
		for row in range(self.relativeTable.rowCount()):
			id=int(self.relativeTable.item(row,0).text())
			concept["relative"].append(id)
		self.refresh()
		