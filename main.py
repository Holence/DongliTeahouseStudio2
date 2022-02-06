# # --
import translation
from DTPySide import *
from session import LobbySession

app=DTAPP(sys.argv)

app.setWindowIcon(DTIcon.HoloIcon1())
app.setApplicationName("DongliTeahouseStudio")
app.setApplicationVersion("2.0.1.1")
app.setAuthor("鍵山狐")
app.setLoginEnable(True)
app.loadTranslation(translation)
app.setBackupEnable(True)
app.setBackupList(["data.dlcw"])

mainsession=LobbySession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()