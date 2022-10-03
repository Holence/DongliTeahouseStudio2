# # --
from DTPySide import *

class DiarySearchSession(DTFrame.DTMainWindow):
	
	closed=Signal()

	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()
		self.closed.emit()
	
	def __init__(self, app: DTAPP, Headquarter, diary):
		super().__init__(app)
		self.Headquarter=Headquarter
		self.diary=diary
		self.initialize()

	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Diary Search")

		from module import DiarySearch
		self.diary_search_module=DiarySearch(self,self.Headquarter,self.diary)
		self.setCentralWidget(self.diary_search_module)
		self.diary_search_module.lineEdit.setFocus()

		self.resize(self.minimumWidth(),self.minimumHeight())
		self.adjustSize()
		MoveToCenterOfScreen(self)