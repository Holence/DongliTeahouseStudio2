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
		self.initialize()
		self.setWindowTitle("Import Bookmarks")

		from module import BookmarkParser
		bookmark_parser=BookmarkParser(self,Headquarter)
		self.setCentralWidget(bookmark_parser)