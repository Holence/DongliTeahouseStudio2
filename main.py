# # --
from DTPySide import *
from session import LobbySession

app=DTAPP([])

app.setWindowIcon(DTIcon.HoloIcon1())
app.setApplicationName("DongliTeahouseStudio")
app.setApplicationVersion("2.0.0.3")
app.setAuthor("鍵山狐")
app.setLoginEnable(True)

app.setBackupEnable(True)
app.setBackupList(["data.dlcw"])

mainsession=LobbySession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()