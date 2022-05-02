# # --
import translation
from DTPySide import *
from session import LobbySession

app=DTAPP(sys.argv)

app.setWindowIcon(DTIcon.HoloIcon1())
app.setApplicationName("DongliTeahouseStudio")
app.setApplicationVersion("2.0.2.4 build with DTPySide 0.1.4")
app.setAuthor("鍵山狐")
app.setLoginEnable(True)
app.loadTranslation(translation)
app.setDataList(["data.dlcw"])
app.setBackupEnable(True)

mainsession=LobbySession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()