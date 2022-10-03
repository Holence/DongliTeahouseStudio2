# # --
from DTPySide import *

from session.LobbySession import LobbySession
class LibrarySession(DTFrame.DTMainWindow):
	def eventFilter(self, watched: QObject, event:QMouseEvent) -> bool:
		# 为了实现重新focusIn窗体的时候刷新界面，虽然手动把一堆子控件installEventFilter一遍，但也只能这样了
		# focusInEvent和mousePressEvent都试了，都不可能捕获子控件的事件，所以只有点击到TitleBar或者window的空白区域，才可能被触发
		if (event.type()==QEvent.MouseButtonPress and event.button()==Qt.LeftButton) or event.type()==QEvent.FocusIn:
			# print(watched)
			# if hasattr(self.Headquarter.lobby,"DataChecker"):
			# 	self.Headquarter.lobby.checkDataCompleteness()
			
			if self.Headquarter.WindowFocusing()!=self:
				self.Headquarter.setWindowFocusing(self)
				# print("Now focused in",self.Headquarter.WindowFocusing())
				self.refresh()
		return False # 这里是让继续延续event的处理，不要被filter掉了
	
	def refresh(self):
		self.library_module.refresh()

	def __init__(self, app: DTAPP, Headquarter: LobbySession):
		super().__init__(app)
		self.Headquarter=Headquarter
	
	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Library")

		from module import Library
		self.library_module=Library(self,self.Headquarter)
		self.setCentralWidget(self.library_module)

		try:
			self.resize(self.Headquarter.UserSetting().value("WindowStatus/LibrarySize"))
			self.move(self.Headquarter.UserSetting().value("WindowStatus/LibraryPos"))
		except:
			self.resize(self.minimumWidth(),self.minimumHeight())
			self.adjustSize()
			MoveToCenterOfScreen(self)
	
	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.library_module.lineEdit_search.installEventFilter(self)
		self.library_module.lineEdit_name.installEventFilter(self)
		self.library_module.fileTab.fileTable.installEventFilter(self)
		self.library_module.fileTab.fileList.installEventFilter(self)
		self.library_module.conceptTable.installEventFilter(self)
		self.library_module.textList.installEventFilter(self)
		self.library_module.textViewer.installEventFilter(self)
		
		self.addAction(self.library_module.actionDelete)
		self.addAction(self.library_module.actionSearch_File)
	
	def initializeMenu(self):
		
		self.addActionToMainMenu(self.library_module.actionSearch_File)
		
		super().initializeMenu()
		