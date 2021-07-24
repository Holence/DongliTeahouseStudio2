# # --
from DTPySide import *
from session import LobbySession

app=DTAPP([])
app.setApplicationName("DongliTeahouse")
mainsession=LobbySession(app)
app.setMainSession(mainsession)

app.debugRun("123",True)
app.run()

# 缩略图
# alt打开文件目录
# 文件复制导出
# 导出JSON