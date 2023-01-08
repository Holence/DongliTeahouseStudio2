# # --
from DTPySide import *

from session import LobbySession
from module.Diary import Diary
from module.Ui_DiarySearch import Ui_DiarySearch
class DiarySearch(Ui_DiarySearch, QWidget):
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
			self.diary.textList.clearSelection()
			self.diary.textList.setCurrentRow(index)
			self.diary.showLine()
		
		self.textList.textClicked.connect(slot)
		self.textList.setObjectName("DiarySearchTextList")
		self.textList.setHeadquarter(self.Headquarter)
		
		# 不允许拖到SearchList中
		self.textList.setAcceptDrops(False)
		
		self.lineEdit.setFocus()
	
	def showSearch(self):
		search=self.lineEdit.text()
		search_list,date_range_list,concept_list,_=self.Headquarter.parseSearchText(search)

		if search.strip()=="":
			return
		
		if search_list==[] and date_range_list==[] and concept_list==[]:
			self.textList.clear()
			return
		
		rank=False
		if self.checkBox.checkState()==Qt.Checked:
			rank=True
		line_list=self.Headquarter.getDiaryLineList(search_list,date_range_list,concept_list,rank=rank)
		
		self.textList.setTextList("Search",line_list)

		text=""
		old_date=""
		for line in line_list:
			year=line["y"]
			month=line["m"]
			day=line["d"]
			date=QLocale().toString(QDate(int(year),int(month),int(day)),"yyyy.M.d ddd")
			if old_date!=date:
				text+="### "+date+"\n\n"
				old_date=date
			text+=line["text"]+"\n\n"
		self.textViewer.setMarkdown(text)