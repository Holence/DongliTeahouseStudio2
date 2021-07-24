# # --
from DTPySide import *

from module import Setting
class SettingSession(DTSession.DTSettingSession):
	def __init__(self,Headquarter,app):
		super().__init__(Headquarter,app)

		self.setting=Setting(Headquarter)

		self.menubutton_diary=DTWidget.DTSettingButton(QIcon(":/icon/white/white_feather.svg"))
		self.addButtonAndPage(self.menubutton_diary,self.setting.page_diary)

		self.menubutton_concept=DTWidget.DTSettingButton(QIcon(":/icon/white/white_hash.svg"))
		self.addButtonAndPage(self.menubutton_concept,self.setting.page_concept)

		self.menubutton_library=DTWidget.DTSettingButton(QIcon(":/icon/white/white_inbox.svg"))
		self.addButtonAndPage(self.menubutton_library,self.setting.page_library)