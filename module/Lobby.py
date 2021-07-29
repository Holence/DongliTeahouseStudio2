# # --
from DTPySide import *

from module.Ui_Lobby import Ui_Lobby
from session import LobbySession
class Lobby(QWidget,Ui_Lobby):
	def __init__(self, Headquarter: LobbySession):
		super().__init__(parent=Headquarter)
		self.setupUi(self)

		self.Headquarter=Headquarter
		self.desktop.setHeadquarter(self.Headquarter)

		self.btn_diary.clicked.connect(lambda:self.summon("diary","Diary"))
		self.btn_concept.clicked.connect(lambda:self.summon("concept","Concept"))
		self.btn_library.clicked.connect(lambda:self.summon("library","Library"))
	
		self.actionExport_to_Json.triggered.connect(self.ExportToJson)
		self.actionCheck_Library.triggered.connect(self.checkLibrary)
		self.actionSwitch_Secure_Mode.triggered.connect(self.switchSecureMode)

		self.SecureMode=False
		
	def switchSecureMode(self):
		if self.SecureMode==False:
			self.SecureMode=True
			self.actionSwitch_Secure_Mode.setIcon(QIcon(":/icon/white/white_toggle-right.svg"))
			self.actionSwitch_Secure_Mode.setText("Secure Mode - On")
			DTFrame.DTMessageBox(self,"Information","Secure mode is on. Password will be needed opening modules.",DTIcon.Happy())
		else:
			if DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				self.SecureMode=False
				self.actionSwitch_Secure_Mode.setIcon(QIcon(":/icon/white/white_toggle-left.svg"))
				self.actionSwitch_Secure_Mode.setText("Secure Mode - Off")
				DTFrame.DTMessageBox(self,"Information","Secure mode is off. Password will not be needed opening modules.",DTIcon.Happy())
	
	def summon(self, へ_へ, ヘ＿ヘ):
		if self.SecureMode==True:
			if not DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				return
		
		exec(f"""
flag=False
for {へ_へ} in self.Headquarter.{へ_へ}_heap:
	if {へ_へ}.isHidden():
		{へ_へ}.show()
		{へ_へ}.setFocus()
		flag=True
		break

if flag==True:
	# 清理掉没有hidden的
	self.Headquarter.{へ_へ}_heap=[{へ_へ} for {へ_へ} in self.Headquarter.{へ_へ}_heap if {へ_へ}.isHidden()==False]
else:
	# 新建
	from session.{ヘ＿ヘ}Session import {ヘ＿ヘ}Session
	new_{へ_へ}={ヘ＿ヘ}Session(self.Headquarter.app,self.Headquarter)
	new_{へ_へ}.initialize()
	self.Headquarter.{へ_へ}_heap.append(new_{へ_へ})
	self.Headquarter.refreshModuleSingal()
	new_{へ_へ}.show()
	new_{へ_へ}.setFocus()

# print("{ヘ＿ヘ}",len(self.Headquarter.{へ_へ}_heap))
""")
	
	def ExportToJson(self):
		Json_Save(self.Headquarter.data,"Export_Data_%s.json"%WhatDayIsToday("0"))
	
	def checkLibrary(self):
		
		if self.SecureMode==True:
			if not DTSession.DTLoginSession(self.Headquarter.UserSetting().value("BasicInfo/Password")).exec_():
				return
		
		if not os.path.exists(self.Headquarter.library_base):
			DTFrame.DTMessageBox(self,"Error","Cannot access Library, please check the direction existence!")
			return

		from module.LibraryCheck import LibraryCheck
		dlg=DTFrame.DTDialog(self,"Library Check")
		dlg.TitleBar.title_icon.setIcon(QIcon())
		dlg.TitleBar.title_icon.setText("💩")
		dlg.TitleBar.title_icon.setStyleSheet("font-size:25pt")
		
		module=LibraryCheck(self.Headquarter)
		dlg.setCentralWidget(module)
		dlg.buttonBox.hide()
		dlg.setMinimumSize(1500,1100)
		dlg.exec_()

		for diary in self.Headquarter.diary_heap:
			diary.diary_module.refresh()
		for concept in self.Headquarter.concept_heap:
			concept.concept_module.refresh()
		for library in self.Headquarter.library_heap:
			library.library_module.refresh()