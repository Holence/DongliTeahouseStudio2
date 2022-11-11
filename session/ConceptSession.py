# # --
from DTPySide import *

from session.LobbySession import LobbySession
class ConceptSession(DTFrame.DTMainWindow):
	
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
		if event.type()==QEvent.KeyPress:
			if event.key()==Qt.Key_Control or event.key()==Qt.Key_Shift:
				self.__selectPressed=True
		if event.type()==QEvent.KeyRelease:
			if event.key()==Qt.Key_Control or event.key()==Qt.Key_Shift:
				self.__selectPressed=False
		return False # 这里是让继续延续event的处理，不要被filter掉了
	
	def refresh(self):
		self.concept_module.refresh()

	def __init__(self, app: DTAPP, Headquarter: LobbySession):
		super().__init__(app)
		self.Headquarter=Headquarter
		self.__selectPressed=False
	
	def isSelect(self):
		return self.__selectPressed
	
	def setSelect(self,bool):
		self.__selectPressed=bool
	
	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Concept")

		from module import Concept
		self.concept_module=Concept(self,self.Headquarter)
		self.setCentralWidget(self.concept_module)

		try:
			self.resize(self.Headquarter.UserSetting().value("WindowStatus/ConceptSize"))
			self.move(self.Headquarter.UserSetting().value("WindowStatus/ConceptPos"))
		except:
			self.resize(self.minimumWidth(),self.minimumHeight())
			self.adjustSize()
			MoveToCenterOfScreen(self)
	
	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.concept_module.conceptTable.installEventFilter(self)
		self.concept_module.lineEdit_search.installEventFilter(self)
		self.concept_module.lineEdit_name.installEventFilter(self)
		self.concept_module.plainTextEdit_detail.installEventFilter(self)
		self.concept_module.textviewer_detail.installEventFilter(self)
		self.concept_module.fileTab.fileTable.installEventFilter(self)
		self.concept_module.fileTab.fileList.installEventFilter(self)
		self.concept_module.textList.installEventFilter(self)
		self.concept_module.textViewer.installEventFilter(self)
		self.concept_module.parentTable.installEventFilter(self)
		self.concept_module.childTree.installEventFilter(self)
		self.concept_module.relativeTable.installEventFilter(self)

		self.addAction(self.concept_module.actionAdd_Concept)
		self.addAction(self.concept_module.actionDelete)
		self.addAction(self.concept_module.actionSearch_Concept)
		self.addAction(self.concept_module.actionAdd_Parent)
		self.addAction(self.concept_module.actionAdd_Child)
		self.addAction(self.concept_module.actionAdd_Relative)
		self.addAction(self.concept_module.actionSwitch_Detail_Eidt_View)
	
	def initializeMenu(self):

		self.menu_edit=QMenu(QCoreApplication.translate("Lobby", "Edit"),self)
		self.menu_edit.setIcon(IconFromCurrentTheme("pen-tool.svg"))
		self.menu_edit.addAction(self.concept_module.actionAdd_Concept)
		self.menu_edit.addAction(self.concept_module.actionAdd_Parent)
		self.menu_edit.addAction(self.concept_module.actionAdd_Child)
		self.menu_edit.addAction(self.concept_module.actionAdd_Relative)
		# self.menu_edit.addAction(self.concept_module.actionDelete)
		self.addMenuToMainMenu(self.menu_edit)

		self.addActionToMainMenu(self.concept_module.actionSearch_Concept)
		self.addActionToMainMenu(self.concept_module.actionSwitch_Detail_Eidt_View)

		self.addSeparatorToMainMenu()
		super().initializeMenu()