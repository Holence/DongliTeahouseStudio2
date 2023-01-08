# # --
import translation
from DTPySide import *
from session import LobbySession

app=DTAPP(sys.argv)

app.setWindowIcon(DTIcon.HoloIcon1())
app.setApplicationName("DongliTeahouseStudio")
app.setApplicationVersion("2.0.2.9 build with DTPySide %s"%importlib.metadata.version('DTPySide'))
app.setAuthor("鍵山狐")
app.setLoginEnable(True)
app.loadTranslation(translation)
app.setDataList(["data.dlcw"])
app.setBackupEnable(True)

mainsession=LobbySession(app)
app.setMainSession(mainsession)

# app.debugRun("123",True)
app.run()