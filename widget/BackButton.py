# # --
from DTPySide import *

from session.LobbySession import LobbySession
class BackButton(QPushButton):

    rightClicked=Signal()
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setIcon(IconFromCurrentTheme("chevron-left.svg"))
    
    def mousePressEvent(self, e: QMouseEvent):
        if e.button()==Qt.RightButton:
            self.rightClicked.emit()
        else:
            super().mousePressEvent(e)