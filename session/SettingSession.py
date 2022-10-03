# # --
from DTPySide import *

from module import Setting
class SettingSession(DTSession.DTSettingSession):
	def __init__(self,Headquarter,app):
		super().__init__(Headquarter,app)

		self.setting=Setting(Headquarter)

		self.menubutton=DTWidget.DTSettingButton(IconFromCurrentTheme("tool.svg"))
		self.addButtonAndPage(self.menubutton,self.setting.page)