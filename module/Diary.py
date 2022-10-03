# # --
from DTPySide import *

from session import LobbySession
from module.Ui_Diary import Ui_Diary
class Diary(QWidget,Ui_Diary):

	def __init__(self, parent, Headquarter: LobbySession):
		super().__init__()
		self.setupUi(self)
		self.Headquarter=Headquarter
		self.current_date=QDate()
		self.initializeWindow()
		self.initializeSignal()
		self.current_date=self.calendar.selectedDate()
		self.date_history_queue=[]
		self.current_index=-1
	
	def initializeWindow(self):

		self.splitter_whole.setStretchFactor(0,5)
		self.splitter_whole.setStretchFactor(1,1)
		self.splitter_left.setStretchFactor(0,10)
		self.splitter_left.setStretchFactor(1,1)
		self.splitter_right.setStretchFactor(0,1)
		self.splitter_right.setStretchFactor(1,2)
		self.splitter_right.setStretchFactor(2,1)

		self.textList.setHeadquarter(self.Headquarter)
		self.textList.setObjectName("DiaryTextList%s"%len(self.Headquarter.diary_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.conceptTable.setHeadquarter(self.Headquarter)
		self.conceptTable.setObjectName("DiaryConceptTable%s"%len(self.Headquarter.diary_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.lineEdit_concept.setHeadquarter(self.Headquarter)
		self.fileTab.setHeadquarter(self.Headquarter)
		self.fileTab.fileTable.setObjectName("DiaryFileTable%s"%len(self.Headquarter.diary_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName
		self.fileTab.fileList.setObjectName("DiaryFileList%s"%len(self.Headquarter.diary_heap)) #三个模块中名字重复了，DND时要判断objectName，这里得手动设置不同的objectName

		self.actionSwitch_Eidt_View.setIcon(IconFromCurrentTheme("slack.svg"))
		
		self.actionGoto_Random_Day.setIcon(IconFromCurrentTheme("gift.svg"))
		self.actionPrevious_Week.setIcon(IconFromCurrentTheme("chevron-up.svg"))
		self.actionPrevious_Day.setIcon(IconFromCurrentTheme("chevron-up.svg"))
		self.actionPrevious_Line.setIcon(IconFromCurrentTheme("chevron-up.svg"))
		self.actionFirst_Line.setIcon(IconFromCurrentTheme("chevron-up.svg"))

		self.actionNext_Day.setIcon(IconFromCurrentTheme("chevron-down.svg"))
		self.actionNext_Week.setIcon(IconFromCurrentTheme("chevron-down.svg"))
		self.actionNext_Line.setIcon(IconFromCurrentTheme("chevron-down.svg"))
		self.actionLast_Line.setIcon(IconFromCurrentTheme("chevron-down.svg"))

		self.actionAdd_Line.setIcon(IconFromCurrentTheme("plus.svg"))
		self.actionAdd_Concept.setIcon(IconFromCurrentTheme("hash.svg"))
		self.actionFind_Text.setIcon(IconFromCurrentTheme("search.svg"))
		self.actionImport_Text.setIcon(IconFromCurrentTheme("download-cloud.svg"))

		self.pushButton_back.setStyleSheet("""
			border: none;
			icon-size: 15px;
			max-height: 15px;
			min-height: 15px;
			min-width: 15px;
			max-width: 15px;
		""")

		self.CalendarPaintMonth()
		self.textEdit.setEnabled(False)

		self.label_calendar.setStyleSheet("font-size: 13pt;")
	
	def initializeSignal(self):

		self.actionGoto_Random_Day.triggered.connect(self.GotoRandomDay)
		self.actionSwitch_Eidt_View.triggered.connect(self.switchEditAndView)
		self.actionPrevious_Day.triggered.connect(self.toPreviousDay)
		self.actionNext_Day.triggered.connect(self.toNextDay)
		self.actionPrevious_Week.triggered.connect(self.toPreviousWeek)
		self.actionNext_Week.triggered.connect(self.toNextWeek)
		
		self.actionAdd_Line.triggered.connect(self.addLine)
		self.actionFirst_Line.triggered.connect(self.toFirstLine)
		self.actionPrevious_Line.triggered.connect(self.toPreviousLine)
		self.actionNext_Line.triggered.connect(self.toNextLine)
		self.actionLast_Line.triggered.connect(self.toLastLine)

		self.actionDelete.triggered.connect(self.deleteCenter)
		self.textList.textDelete.connect(self.deleteLine)
		self.fileTab.fileDelete.connect(self.deleteLineFile)
		self.conceptTable.conceptDelete.connect(self.deleteLineConcept)
		
		self.pushButton_back.clicked.connect(self.toHistoryPreviousDay)
		self.pushButton_back.rightClicked.connect(self.showDayHistory)

		# 点击日期
		def slot(date):
			self.textList.scrollToTop()
			self.textViewer.verticalScrollBar().setValue(0)
			self.textEdit.setEnabled(False)
			self.showDay(date, reset=True)
		self.calendar.clicked.connect(slot)

		self.calendar.currentPageChanged.connect(self.CalendarPaintMonth)
		
		# 点击（更换选中的）一行
		self.textList.itemClicked.connect(lambda:self.showLine(focus=False)) #聚焦离开了textEdit会触发saveLine，紧接着就是showDay中的showLine，focus=False让不强制聚焦
		# 行排序
		self.textList.textDropped.connect(self.sortLine)
		
		# 保存当前行
		self.textEdit.editingFinished.connect(lambda:self.saveLine(focus=False)) #聚焦离开了textEdit会触发saveLine，紧接着就是showDay中的showLine，focus=False让不强制聚焦

		# 添加line链接concept
		self.conceptTable.conceptDropped.connect(self.addLineConcept)
		self.lineEdit_concept.conceptAdd.connect(self.addLineConcept)
		self.actionAdd_Concept.triggered.connect(self.lineEdit_concept.setFocus)

		self.fileTab.fileDropped.connect(self.addLineFile)

		self.actionFind_Text.triggered.connect(self.findText)

		self.actionImport_Text.triggered.connect(self.importText)

		self.fileTab.fileTable.fileSorted.connect(self.sortLineFile)
		self.conceptTable.conceptSort.connect(self.sortLineConcept)
	
	def CalendarPaintMonth(self):
		format = QTextCharFormat()
		empty_format=QTextCharFormat()
		format.setForeground(QColor("#FFADAD"))
		year=self.calendar.yearShown()
		month=self.calendar.monthShown()
		self.label_calendar.setText("%s.%s"%(year,month))
		begin=QDate(year,month,1)
		end=begin.daysInMonth()
		end=QDate(year,month,end)
		while begin<=end:
			res=self.Headquarter.getDiaryDay(begin)
			if res!=None:
				self.calendar.setDateTextFormat(begin,format)
			else:
				self.calendar.setDateTextFormat(begin,empty_format)
			begin=begin.addDays(1)

	def refresh(self):
		self.showDay()

	def showDay(self, date=None, reset=False):
		"""展示选中的日期，相当于全刷新
		"""
		
		# 保存之前的date到date_history_queue中
		if date!=None:
			if len(self.date_history_queue)==10:
				self.date_history_queue.pop()
			if self.current_date not in self.date_history_queue:
				self.date_history_queue.insert(0,self.current_date)
			else:
				self.date_history_queue.remove(self.current_date)
				self.date_history_queue.insert(0,self.current_date)
			if date in self.date_history_queue:
				self.date_history_queue.remove(date)

		if date!=None:
			self.current_date=date
			self.calendar.setSelectedDate(self.current_date)
		else:
			self.current_date=self.calendar.selectedDate()
		
		if reset==True:
			self.textEdit.clear()
		else:
			self.CalendarPaintMonth()
		
		self.window().setWindowTitle("Diary %s"%QLocale().toString(self.current_date,"yyyy.M.d ddd"))
		
		day_data=self.Headquarter.getDiaryDay(self.current_date)
		
		self.current_index=-1
		
		if day_data!=None:
			# 有该日
			concept_id_list=[]
			file_list=[]
			if self.stackedWidget.currentIndex()==0:
				self.textList.setTextList("Diary",self.current_date)
				for line in day_data:
					concept_id_list=List_Union(concept_id_list,line["concept"])
					file_list=List_Union_Full(file_list,line["file"])
			else:
				text=""
				for line in day_data:
					text+=line["text"]+"\n\n\n\n"
					concept_id_list=List_Union(concept_id_list,line["concept"])
					file_list=List_Union_Full(file_list,line["file"])
				store=self.textViewer.verticalScrollBar().value()
				self.textViewer.setMarkdown(text)
				self.textViewer.verticalScrollBar().setValue(store)
			
			self.conceptTable.setConceptIDList(concept_id_list)
			self.conceptTable.clearSelection()
			self.fileTab.setFileList(file_list)
			self.fileTab.clearSelection()
			if reset==True:
				# 指定日，全刷
				self.textList.scrollToTop()
				self.textList.clearSelection()
				self.textList.setCurrentRow(-1)
			else:
				# 无指定日，刷新行
				self.showLine()

		else:
			# 无该日，clear
			self.textList.clear()
			self.conceptTable.Clear()
			self.fileTab.Clear()
			self.textViewer.clear()

	def toHistoryPreviousDay(self):
		if self.date_history_queue!=[]:
			self.showDay(self.date_history_queue[0],reset=True)

	def showDayHistory(self):
		pos=self.pushButton_back.pos()+self.splitter_right.pos()
		menu=QMenu()
		
		for date in self.date_history_queue:

			name=QLocale().toString(date,"yyyy.M.d ddd")
			action=QAction(name,self)
			action.triggered.connect(partial(self.showDay, date))
			menu.addAction(action)

		pos=self.mapToGlobal(pos)+QPoint(0,self.pushButton_back.height())
		
		menu.exec_(pos)
	
	def showLine(self, focus=True):
		"""展示选中的行
		"""

		index=self.textList.currentRow()
		if index!=-1:
			self.textEdit.setEnabled(True)
			self.current_index=index
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			if line!=None:
				self.textEdit.setPlainText(line["text"])
				self.conceptTable.setConceptIDList(line["concept"])
				self.fileTab.setFileList(line["file"])
				self.textEdit.moveCursor(QTextCursor.End)
				
				if focus!=False:
					self.textList.scrollToItem(self.textList.item(index))
					self.textEdit.setFocus()
					

	def sortLine(self):
		day_data=self.Headquarter.getDiaryDay(self.current_date)
		if day_data!=None and len(day_data)!=1:
			if len(day_data)!=self.textList.count():
				DTFrame.DTMessageBox(self,"Error","Fatal Error during text sorting!!!",DTIcon.Error())
			
			diary_data=self.Headquarter.getDiaryData()
			y,m,d=map(str,QDate_to_Tuple(self.current_date))
			
			diary_data[y][m][d]=[]

			for index in range(len(day_data)):
				old_index=[line["text"]==self.textList.item(index).text() for line in day_data].index(True)
				line=day_data.pop(old_index)
				diary_data[y][m][d].append(line)
			
			self.showDay()
		else:
			# 真是奇怪了，只有一个item的时候，拖动放入后复制了一份？！
			self.showDay()			
	
	def switchEditAndView(self):
		if self.stackedWidget.currentIndex()==0:
			# View
			self.stackedWidget.setCurrentIndex(1)
			self.textEdit.clearFocus()
		else:
			# Edit
			self.stackedWidget.setCurrentIndex(0)
		
		self.showDay()

	def GotoRandomDay(self):
		self.saveLine()
		date=self.Headquarter.getRandomDiaryDate()
		self.showDay(date, reset=True)
		self.textEdit.setEnabled(False)
		self.textEdit.clearFocus()

	def toPreviousWeek(self):
		self.saveLine()
		date=self.current_date.addDays(-7)
		self.showDay(date, reset=True)
		self.textEdit.setEnabled(False)
		self.textEdit.clearFocus()

	def toPreviousDay(self):
		self.saveLine()
		date=self.current_date.addDays(-1)
		self.showDay(date, reset=True)
		self.textEdit.setEnabled(False)
		self.textEdit.clearFocus()
		
	def toNextDay(self):
		self.saveLine()
		date=self.current_date.addDays(1)
		self.showDay(date, reset=True)
		self.textEdit.setEnabled(False)
		self.textEdit.clearFocus()
		
	def toNextWeek(self):
		self.saveLine()
		date=self.current_date.addDays(7)
		self.showDay(date, reset=True)
		self.textEdit.setEnabled(False)
		self.textEdit.clearFocus()
	
	def toFirstLine(self):
		self.saveLine()
		self.textList.setCurrentRow(0)
		self.showLine()
		
	def toPreviousLine(self):
		if self.textList.currentRow()>0:
			self.saveLine()
			self.textList.setCurrentRow(self.textList.currentRow()-1)
			self.showLine()
		
	def toNextLine(self):
		if self.textList.currentRow()!=self.textList.count()-1:
			self.saveLine()
			self.textList.setCurrentRow(self.textList.currentRow()+1)
			self.showLine()
		
	def toLastLine(self):
		self.saveLine()
		self.textList.setCurrentRow(self.textList.count()-1)
		self.showLine()

	def saveLine(self,focus=True):
		index=self.current_index
		
		if index!=-1:
		
			text=self.textEdit.toPlainText()
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			line["text"]=text
			self.textList.setTextList("Diary",self.current_date)
			self.textList.clearSelection()
			self.showLine(focus)

	def addLine(self):
		
		index=self.current_index
		
		if index!=-1:# and self.textEdit.isEnabled():
			self.saveLine()
		else:
			# 没有选择，就不存储行
			if self.textList.count()!=0:
				# 在最后一行插入
				index=self.textList.count()-1
			else:
				# index保持为-1，在第一行插入
				pass

		# 没有容器，在第一行插入
		day_data=self.Headquarter.getDiaryDay(self.current_date)
		if day_data==None:
			day_data=self.Headquarter.addDiaryDay(self.current_date)
			self.CalendarPaintMonth()

		day_data.insert(index+1,{
			"text": "",
			"concept": [],
			"file": []
		})
		
		item=QListWidgetItem("")
		item.setIcon(QIcon("./icon/%s/line_00.png"%QIcon.themeName()))
		self.textList.setTextList("Diary",self.current_date)
		self.textList.clearSelection()
		self.textList.setCurrentRow(index+1)
		self.showLine()
		self.textEdit.setFocus()
	
	def addLineConcept(self,id_list):
		index=self.textList.currentRow()
		if index!=-1:

			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			for id in List_Difference(id_list,line["concept"]):
				line["concept"].append(id)
			
			self.showDay()

	def addLineFile(self,url_list,file_list):
		index=self.textList.currentRow()
		if index!=-1:
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			# 外来
			if file_list==[]:
				date=WhatDayIsToday(1)
				for url in url_list:

					# Library_Data中file添加file
					res=self.Headquarter.addLibraryFile(date,url,[])
					if res!=None:
						name,new_file=res

						# line中添加file
						if type(url)==dict:
							# BookmarkParser来的标准型filedict，就不用去获取网页title了，ymd也不是当日，而是收藏夹中的日期
							file=url
							line["file"].append(self.Headquarter.generateDiaryConceptFileDict(QDate(file["y"],file["m"],file["d"]),new_file["type"],name,new_file["url"]))
						else:
							line["file"].append(self.Headquarter.generateDiaryConceptFileDict(date,new_file["type"],name,new_file["url"]))
					else:
						# 失败
						continue
			else:
				# line中添加file
				line["file"]=List_Union_Full(line["file"],file_list)

			self.showDay()

	def deleteCenter(self):
		if self.textList.hasFocus():
			self.deleteLine()
		elif self.conceptTable.hasFocus():
			self.deleteLineConcept()
		elif self.fileTab.fileTable.hasFocus() or self.fileTab.fileList.hasFocus():
			self.deleteLineFile()
	
	def deleteLine(self):
		index=self.textList.currentRow()
		if index!=-1:
			day_data=self.Headquarter.getDiaryDay(self.current_date)
			warning_text=""
			delete_index_list=[]
			for model_index in self.textList.selectionModel().selectedRows():
				index=model_index.row()
				warning_text+=day_data[index]["text"]+"\n"
				delete_index_list.append(index)
			
			if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete text:",DTIcon.Question(),warning_text).exec_():
				self.Headquarter.deleteDiaryDayLine(self.current_date,delete_index_list)
				self.CalendarPaintMonth()
				self.textEdit.setEnabled(False)
				self.showDay(reset=True)
	
	def deleteLineConcept(self):
		index=self.textList.currentRow()
		if index!=-1:
		
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			
			delete_id_list=[]
			warning_text=""
			for model_index in self.conceptTable.selectionModel().selectedRows():
				row=model_index.row()
				id=int(self.conceptTable.item(row,0).text())
				
				delete_id_list.append(id)
				warning_text+="%s: %s\n"%(id,self.Headquarter.getConcept(id)["name"])
	
			if delete_id_list!=[]:
				if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete line linked concept:",DTIcon.Question(),warning_text).exec_():
					line["concept"]=List_Difference(line["concept"],delete_id_list)
					self.refresh()
	
	def deleteLineFile(self):
		index=self.textList.currentRow()
		if index!=-1:
		
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			
			delete_filename_list=[]
			warning_text=""
			if self.fileTab.stackedWidget.currentIndex()==0:
				for model_index in self.fileTab.fileTable.selectionModel().selectedRows():
					row=model_index.row()
					filename=self.fileTab.fileTable.item(row,3).text()
				
					delete_filename_list.append(filename)
					warning_text+="%s\n\n"%(filename)
			else:
				for model_index in self.fileTab.fileList.selectionModel().selectedRows():
					row=model_index.row()

					url=self.Headquarter.extractFileURL(self.fileTab.fileList.item(row).toolTip().split("\n")[0])
					if url[:4]=="http":
						name=self.fileTab.fileList.item(row).text()
						name=name[:name.rfind("|")]
					else:
						name=self.fileTab.fileList.item(row).text()

					delete_filename_list.append(name)
					warning_text+="%s\n\n"%(name)
	
			if delete_filename_list!=[]:
				if DTFrame.DTConfirmBox(self,"Delete Confirm","You want to delete line linked file:",DTIcon.Question(),warning_text).exec_():
					line["file"]=[file for file in line["file"] if file["name"] not in delete_filename_list]
					self.refresh()
		else:
			DTFrame.DTMessageBox(self,"Warning","Please select line first, then select the file to delete.",DTIcon.Warning())
		
	def findText(self):
		def slot():
			del self.dairy_search_window
		
		if hasattr(self,"dairy_search_window"):
			ShowUp(self.dairy_search_window)
			return
		
		from session import DiarySearchSession
		self.dairy_search_window=DiarySearchSession(self.Headquarter.app,self.Headquarter,self)
		self.dairy_search_window.closed.connect(slot)
		self.dairy_search_window.show()
	
	def importText(self):
		dlg=DTFrame.DTDialog(self,"Import Text")
		dlg.setFocus()
		label=QLabel("Format:\n\n# 2001.1.1\n\nFirst text block.\n\n~~~\n\nSecond text block.\n\n# 2001.1.2\n\nFirst text block.\n\n~~~\n\nSecond text block.")
		label.setStyleSheet("font-size:12pt;")
		textedit=QPlainTextEdit()
		textedit.setStyleSheet("font-size:10pt;")
		textedit.setFocus()
		layout=QHBoxLayout()
		layout.setMargin(0)
		layout.addWidget(label)
		layout.addWidget(textedit)
		widget=QWidget()
		widget.setLayout(layout)
		dlg.setCentralWidget(widget)
		dlg.setMinimumSize(500,500)
		
		dlg.adjustSize()
		MoveToCenterOfScreen(dlg)

		if dlg.exec_():
			text=[i for i in textedit.toPlainText().splitlines() if i!=""]
			
			if text==[]:
				return
			
			if text[0][:2]!="# ":
				DTFrame.DTMessageBox(dlg,"Error","Wrong format!\n\nText should start with \"# \".",DTIcon.Error())
			else:
				
				text_block=""
				date_list=[]
				for i in text:
					if i[:2]=="# ":
						
						# 新一日之前的最后一个block
						if text_block!="":
							date_list[-1].append({
								"text": text_block.strip(),
								"concept": [],
								"file": []
							})
							text_block=""
						
						try:
							date=list(map(int,i[2:].split(".")))
							date=QDate(date[0],date[1],date[2])
							if not date.isValid():
								DTFrame.DTMessageBox(dlg,"Error","Wrong format!\n\nError occurs parsing date.%s"%i,DTIcon.Error())
								break
						
						except Exception as e:
							DTFrame.DTMessageBox(dlg,"Error","Wrong format!\n\nError occurs parsing date.%s"%i,DTIcon.Error())
							break
						
						date_list.append([date])
					
					elif i=="~~~":
						date_list[-1].append({
							"text": text_block.strip(),
							"concept": [],
							"file": []
						})
						text_block=""
					else:
						text_block+=i+"\n\n"
				
				# 最后一日的最后一个block
				else:
					if text_block!="":
						date_list[-1].append({
							"text": text_block.strip(),
							"concept": [],
							"file": []
						})

					for day in date_list:
						date=day[0]
						text_list=day[1:]
						day_data=self.Headquarter.getDiaryDay(date)
						if day_data==None:
							day_data=self.Headquarter.addDiaryDay(date)
						
						for text in text_list:
							day_data.append(text)
					self.CalendarPaintMonth()
					self.refresh()
					DTFrame.DTMessageBox(dlg,"Information","Import successed!",DTIcon.Happy())

	def sortLineFile(self):
		index=self.textList.currentRow()
		if index!=-1:
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			line["file"]=[]
			for row in range(self.fileTab.fileTable.rowCount()):
				type=int(self.fileTab.fileTable.item(row,0).text())
				y,m,d=map(int,self.fileTab.fileTable.item(row,1).text().split("."))
				date=QDate(y,m,d)
				name=self.fileTab.fileTable.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.fileTab.fileTable.item(row,4).text())
				new_file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				line["file"].append(new_file)
		else:
			DTFrame.DTMessageBox(self,"Warning","Please select line first, then select the file to sort.",DTIcon.Warning())
		self.refresh()
	
	def sortLineConcept(self):
		index=self.textList.currentRow()
		if index!=-1:
			line=self.Headquarter.getDiaryDayLine(self.current_date,index)
			line["concept"]=[]
			for row in range(self.conceptTable.rowCount()):
				id=int(self.conceptTable.item(row,0).text())
				line["concept"].append(id)
		else:
			DTFrame.DTMessageBox(self,"Warning","Please select line first, then select the concept to sort.",DTIcon.Warning())
		self.refresh()