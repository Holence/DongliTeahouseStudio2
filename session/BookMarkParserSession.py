# # --
from DTPySide import *

class BookmarkParserSession(DTFrame.DTMainWindow):
	
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
		self.setWindowTitle("Import Bookmarks")

		from module import BookmarkParser
		bookmark_parser=BookmarkParser(self,self.Headquarter)
		self.setCentralWidget(bookmark_parser)

		self.resize(self.minimumWidth(),self.minimumHeight())
		self.adjustSize()
		MoveToCenterOfScreen(self)