# # --
from DTPySide import *

class AdvanceSearchSession(DTFrame.DTMainWindow):
	
	closed=Signal()

	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()
		self.closed.emit()
	
	def __init__(self, app: DTAPP, Headquarter):
		super().__init__(app)
		self.Headquarter=Headquarter
		self.initialize()

	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Advance Search")

		from module import AdvanceSearch
		advance_search=AdvanceSearch(self,self.Headquarter)
		self.setCentralWidget(advance_search)

		self.resize(self.minimumWidth(),self.minimumHeight())
		self.adjustSize()
		MoveToCenterOfScreen(self)