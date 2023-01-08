# # --
from DTPySide import *

from session import LobbySession
class Notes(DTWidget.DTDockWidget):    
    
    def __init__(self, parent: LobbySession) -> None:
        super().__init__("Notes", parent)
        self.Parent=parent
        self.Layout=QHBoxLayout()
        self.textEdit_note=DTWidget.DTPlainTextEdit(self)
        self.Layout.addWidget(self.textEdit_note)
        
        self.Widget=QWidget()
        self.Widget.setLayout(self.Layout)
        self.setWidget(self.Widget)

        self.Widget.setMinimumSize(198, 188)

        try:
            text=self.Parent.data[3]
        except:
            text=""
            self.Parent.data.append(text)
        self.textEdit_note.setPlainText(text)
        
        def save():
            self.Parent.data[3]=self.textEdit_note.toPlainText()
        self.textEdit_note.editingFinished.connect(save)