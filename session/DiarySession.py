# # --
from DTPySide import *

from session.LobbySession import LobbySession
class DiarySession(DTFrame.DTMainWindow):
	
	def closeEvent(self, event:QCloseEvent):
		super().closeEvent(event)
		if hasattr(self.diary_module,"dairy_search_window"):
			self.diary_module.dairy_search_window.close()

	def hide(self) -> None:
		super().hide()
		if hasattr(self.diary_module,"dairy_search_window"):
			self.diary_module.dairy_search_window.hide()
	
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
		self.diary_module.refresh()
	
	def __init__(self, app: DTAPP, Headquarter: LobbySession):
		super().__init__(app)
		self.Headquarter=Headquarter
	
	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Diary")

		from module import Diary
		self.diary_module=Diary(self,self.Headquarter)
		self.setCentralWidget(self.diary_module)

		try:
			self.resize(self.Headquarter.UserSetting().value("WindowStatus/DiarySize"))
			self.move(self.Headquarter.UserSetting().value("WindowStatus/DiaryPos"))
		except:
			self.resize(self.minimumWidth(),self.minimumHeight())
			self.adjustSize()
			MoveToCenterOfScreen(self)
	
	def initializeSignal(self):
		super().initializeSignal()
		self.installEventFilter(self)
		self.diary_module.conceptTable.installEventFilter(self)
		self.diary_module.fileTab.fileTable.installEventFilter(self)
		self.diary_module.fileTab.fileList.installEventFilter(self)
		self.diary_module.textList.installEventFilter(self)
		self.diary_module.textEdit.installEventFilter(self)
		self.diary_module.textViewer.installEventFilter(self)
		
		self.addAction(self.diary_module.actionGoto_Random_Day)
		self.addAction(self.diary_module.actionPrevious_Week)
		self.addAction(self.diary_module.actionPrevious_Day)
		self.addAction(self.diary_module.actionNext_Day)
		self.addAction(self.diary_module.actionNext_Week)
		self.addAction(self.diary_module.actionFirst_Line)
		self.addAction(self.diary_module.actionPrevious_Line)
		self.addAction(self.diary_module.actionNext_Line)
		self.addAction(self.diary_module.actionLast_Line)
		
		self.addAction(self.diary_module.actionAdd_Line)
		self.addAction(self.diary_module.actionDelete)

		self.addAction(self.diary_module.actionSwitch_Eidt_View)
		self.addAction(self.diary_module.actionFind_Text)
		self.addAction(self.diary_module.actionAdd_Concept)
		self.addAction(self.diary_module.actionImport_Text)
	
	def initializeMenu(self):

		self.addActionToMainMenu(self.diary_module.actionGoto_Random_Day)
		self.menu_navigate=QMenu(QCoreApplication.translate("Diary", "Navigate"),self)
		self.menu_navigate.setIcon(IconFromCurrentTheme("map.svg"))
		self.menu_navigate.addAction(self.diary_module.actionPrevious_Week)
		self.menu_navigate.addAction(self.diary_module.actionPrevious_Day)
		self.menu_navigate.addAction(self.diary_module.actionNext_Day)
		self.menu_navigate.addAction(self.diary_module.actionNext_Week)
		self.menu_navigate.addAction(self.diary_module.actionFirst_Line)
		self.menu_navigate.addAction(self.diary_module.actionPrevious_Line)
		self.menu_navigate.addAction(self.diary_module.actionNext_Line)
		self.menu_navigate.addAction(self.diary_module.actionLast_Line)
		self.addMenuToMainMenu(self.menu_navigate)
		
		self.menu_edit=QMenu(QCoreApplication.translate("Lobby", "Edit"),self)
		self.menu_edit.setIcon(IconFromCurrentTheme("pen-tool.svg"))
		self.menu_edit.addAction(self.diary_module.actionAdd_Line)
		self.menu_edit.addAction(self.diary_module.actionAdd_Concept)
		self.menu_edit.addAction(self.diary_module.actionImport_Text)
		# self.menu_edit.addAction(self.diary_module.actionDelete)
		self.addMenuToMainMenu(self.menu_edit)
		
		self.addActionToMainMenu(self.diary_module.actionSwitch_Eidt_View)
		self.addActionToMainMenu(self.diary_module.actionFind_Text)
		
		self.addSeparatorToMainMenu()
		super().initializeMenu()