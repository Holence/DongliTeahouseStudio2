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
		self.initialize()
		self.setWindowTitle("Diary Search")

		from module import DiarySearch
		self.diary_search_module=DiarySearch(self,Headquarter,diary)
		self.setCentralWidget(self.diary_search_module)
		self.diary_search_module.lineEdit.setFocus()