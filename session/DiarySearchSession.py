# # --
from DTPySide import *

class DiarySearchSession(DTFrame.DTMainWindow):
	
	closed=Signal()

	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()
		self.closed.emit()

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
	
	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.diary_search_module.textList.installEventFilter(self)
		self.diary_search_module.textViewer.installEventFilter(self)
		self.diary_search_module.lineEdit.installEventFilter(self)
	
	def refresh(self):
		self.diary_search_module.showSearch()