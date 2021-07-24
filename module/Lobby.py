# # --
from DTPySide import *

from module.Ui_Lobby import Ui_Lobby
from session import LobbySession
class Lobby(QWidget,Ui_Lobby):
	def __init__(self, Headquarter: LobbySession):
		super().__init__(parent=Headquarter)
		self.setupUi(self)

		self.Headquarter=Headquarter

		self.btn_diary.clicked.connect(self.summonDiary)
		# self.btn_diary.setToolTip("Diary")
		self.btn_concept.clicked.connect(self.summonConcept)
		# self.btn_concept.setToolTip("Concept")
		self.btn_library.clicked.connect(self.summonLibrary)
		# self.btn_library.setToolTip("Library")
	
	def summonDiary(self):
		flag=False
		for diary in self.Headquarter.diary_dump:
			if diary.isHidden():
				diary.show()
				diary.setFocus()
				flag=True
				break
		
		if flag==True:
			# 清理掉没有hidden的
			self.Headquarter.diary_dump=[diary for diary in self.Headquarter.diary_dump if diary.isHidden()==False]
		else:
			# 新建
			from session.DiarySession import DiarySession
			new_diary=DiarySession(self.Headquarter.app,self.Headquarter)
			new_diary.initialize()
			self.Headquarter.diary_dump.append(new_diary)
			self.Headquarter.refreshModuleSingal()
			new_diary.show()
		
		# print("Diary",len(self.Headquarter.diary_dump))

	def summonConcept(self):
		flag=False
		for concept in self.Headquarter.concept_dump:
			if concept.isHidden():
				concept.show()
				concept.setFocus()
				flag=True
				break
		
		if flag==True:
			# 清理掉没有hidden的
			self.Headquarter.concept_dump=[concept for concept in self.Headquarter.concept_dump if concept.isHidden()==False]
		else:
			# 新建
			from session.ConceptSession import ConceptSession
			new_concept=ConceptSession(self.Headquarter.app,self.Headquarter)
			new_concept.initialize()
			self.Headquarter.concept_dump.append(new_concept)
			self.Headquarter.refreshModuleSingal()
			new_concept.show()
		
		# print("Concept:",len(self.Headquarter.concept_dump))
	
	def summonLibrary(self):
		flag=False
		for library in self.Headquarter.library_dump:
			if library.isHidden():
				library.show()
				library.setFocus()
				flag=True
				break
		
		if flag==True:
			# 清理掉没有hidden的
			self.Headquarter.library_dump=[library for library in self.Headquarter.library_dump if library.isHidden()==False]
		else:
			# 新建
			from session.LibrarySession import LibrarySession
			new_library=LibrarySession(self.Headquarter.app,self.Headquarter)
			new_library.initialize()
			self.Headquarter.library_dump.append(new_library)
			self.Headquarter.refreshModuleSingal()
			new_library.show()
		
		# print("Library",len(self.Headquarter.library_dump))