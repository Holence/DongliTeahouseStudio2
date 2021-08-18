# # --
from DTPySide import *

from session import LobbySession
from module.Diary import Diary
from module.Ui_DiarySearch import Ui_DiarySearch
class DiarySearch(Ui_DiarySearch,QWidget):
	def __init__(self,parent,Headquarter:LobbySession,diary:Diary):
		super().__init__(parent)
		self.setupUi(self)

		self.Headquarter=Headquarter
		self.diary=diary

		self.lineEdit.returnPressed.connect(self.showSearch)

		def slot(line):
			y=line["y"]
			m=line["m"]
			d=line["d"]
			index=line["index"]
			
			self.diary.showDay(QDate(y,m,d))
			self.diary.textList.setCurrentRow(index)
			self.diary.showLine()
		
		self.listWidget.textClicked.connect(slot)
		self.listWidget.setObjectName("DiarySeachTextList")
		
		# 不允许拖到SearchList中
		self.listWidget.setAcceptDrops(False)
		
		self.lineEdit.setFocus()
	
	def showSearch(self):
		search=self.lineEdit.text()
		search_list,date_range_list,concept_list,_=self.Headquarter.parseSearchText(search)

		if search.strip()=="":
			return
		
		if search_list==[] and date_range_list==[] and concept_list==[]:
			self.listWidget.clear()
			return
		
		rank=False
		if self.checkBox.checkState()==Qt.Checked:
			rank=True
		line_list=self.Headquarter.getDiaryLineList(search_list,date_range_list,concept_list,rank=rank)
		
		self.listWidget.setTextList("Search",line_list)