# # --
from DTPySide import *

from session import LobbySession
from module.Ui_Setting import Ui_Setting
class Setting(Ui_Setting, QStackedWidget):
	def __init__(self,Headquarter:LobbySession):
		super().__init__(Headquarter)
		self.setupUi(self)
		self.Headquarter=Headquarter

		self.lineEdit_library_base.setText(Symmetric_Decrypt(self.Headquarter.password(), self.Headquarter.UserSetting().value("LibraryBase"), iteration=self.Headquarter.iteration()))
		self.pushButton_library_base.clicked.connect(self.setLibraryBase)

	def setLibraryBase(self):
		dlg=QFileDialog(self)
		library_base=dlg.getExistingDirectory()
		if library_base:
			self.Headquarter.UserSetting().setValue("LibraryBase",Symmetric_Encrypt(self.Headquarter.password(), library_base, iteration=self.Headquarter.iteration()))
			self.Headquarter.library_base=Symmetric_Decrypt(self.Headquarter.password(), self.Headquarter.UserSetting().value("LibraryBase"), iteration=self.Headquarter.iteration())
			self.lineEdit_library_base.setText(Symmetric_Decrypt(self.Headquarter.password(), self.Headquarter.UserSetting().value("LibraryBase"), iteration=self.Headquarter.iteration()))
			DTFrame.DTMessageBox(self,"Information","Library Base changed to\n\n \"%s\" \n\nsuccessfully!"%self.Headquarter.library_base,DTIcon.Information())