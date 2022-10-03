# # --
from DTPySide import *
from web_func import *

class DesktopButton(QPushButton):
	
	deleteSignal=Signal(str)

	def __init__(self, parent, Headquarter, url):
		super().__init__(parent=parent)
		self.url=url
		self.Headquarter=Headquarter
		self.clicked.connect(self.openFile)
		self.setFlat(True)
		self.setStyleSheet("""
        QPushButton{
            icon-size: 24px;
            max-height: 32px;
            min-height: 32px;
            max-width: 32px;
            min-width: 32px;
            background:transparent;
            border:none;
        };
        """)

		if url[:8]=="file:///":
			self.setToolTip(os.path.basename(url))
		else:
			self.setToolTip(url)
		
		self.refreshIcon()

	def refreshIcon(self,force=False):
		
		# 本地load图标
		if self.url[:8]=="file:///":
			file_info=QFileInfo(self.url[8:])
			icon=QFileIconProvider().icon(file_info)
		
		# 网页favicon
		else:
			cache_name=self.url
			data=self.Headquarter.cache.get(cache_name)
			
			# cache中没有
			if data==None or force==True:

				redirect_dict={
					"bilibili":"https://www.bilibili.com/favicon.ico",
					"douban":"https://img3.doubanio.com/favicon.ico",
					"mail.google":"https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico",
					"gmail":"https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico"
				}
				for key,value in redirect_dict.items():
					if key in self.url:
						data=GetWebPagePic(value)
						break
				else:
					data=GetWebFavIcon(self.url)
				# 载入成功
				
				if data!=None:
					data=base64.b64encode(data)
					self.Headquarter.cache[cache_name]=data #cache中存储
					pixmap=QPixmap()
					pixmap.loadFromData(base64.b64decode(data))
					pixmap=pixmap.scaled(24,24,Qt.KeepAspectRatio)
					icon=QIcon(pixmap)
				# 载入失败
				else:
					self.Headquarter.cache[cache_name]=-1 #cache中存储为-1
					icon=IconFromCurrentTheme("globe.svg")
			
			# cache中为-1
			elif data==-1:
				icon=IconFromCurrentTheme("globe.svg")
			
			# cache中有
			else:
				pixmap=QPixmap()
				pixmap.loadFromData(base64.b64decode(data))
				pixmap=pixmap.scaled(24,24,Qt.KeepAspectRatio)
				icon=QIcon(pixmap)
		
		self.setIcon(icon)

	def mouseReleaseEvent(self, e: QMouseEvent):
		if e.button()==Qt.RightButton:
			
			menu=QMenu()
			
			deleteAction=QAction(QCoreApplication.translate("Library", "Delete"))
			deleteAction.triggered.connect(self.deleteLater)
			deleteAction.triggered.connect(lambda:self.deleteSignal.emit(self.url))
			menu.addAction(deleteAction)
			
			refreshIconAction=QAction(QCoreApplication.translate("Library", "Refresh Icon"))
			refreshIconAction.triggered.connect(lambda:self.refreshIcon(force=True))
			menu.addAction(refreshIconAction)
			
			show_ContextMenu_Right(menu,self)
		else:
			super().mouseReleaseEvent(e)
	
	def openFile(self):
		if self.url[0:8]=="file:///":
			try:
				os.startfile(self.url)
			except Exception as e:
				DTFrame.DTMessageBox(self,"Warning","Could not open file! Try running Check Library.\n\n%s"%e,DTIcon.Warning())
		else:
			os.system("start explorer \"%s\""%self.url)

from session.LobbySession import LobbySession
class Desktop(QWidget):
	"""这里的data数据随时存储，不给Lobby那边添麻烦
	"""
	def __init__(self, parent) -> None:
		super().__init__(parent=parent)
		self.setAcceptDrops(True)
		
		self.Layout=QGridLayout(self)
		self.Layout.setMargin(0)
		self.setLayout(self.Layout)
		
		self.btn_list=[] # 储存btn的指针，用于清空layout
		
	def saveDesktop(self):
		self.Headquarter.UserSetting().setValue("Desktop",json.dumps(self.url_list))
	
	def setHeadquarter(self,Headquarter:LobbySession):
		self.Headquarter=Headquarter
		self.refresh()

	def refresh(self):

		# 删除所有的btn
		for btn in self.btn_list:
			btn.deleteLater()

		self.px=0
		self.py=0
		self.btn_list=[]
		
		data=self.Headquarter.UserSetting().value("Desktop")
		if data==None:
			self.url_list=[]
			self.saveDesktop()
		else:
			self.url_list=json.loads(data)
		
		self.addButtons(self.url_list)

	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		event.acceptProposedAction()
	
	def dropEvent(self, event: QDropEvent):
		url_list=[url.toString() for url in event.mimeData().urls()]
		for url in url_list:
			if url not in self.url_list:
				self.url_list.append(url)
				self.addButtons([url])

		self.saveDesktop()
	
	def addButtons(self,url_list):
		def slot(url):
			self.url_list.remove(url)
			if self.Headquarter.cache.get(url)!=None:
				del self.Headquarter.cache[url]
			self.saveDesktop()
			self.refresh()

		for url in url_list:

			btn=DesktopButton(self,self.Headquarter,url)
			btn.deleteSignal.connect(slot)
			self.btn_list.append(btn)
			self.Layout.addWidget(btn,self.py,self.px)

			if self.px<4:
				self.px+=1
			else:
				self.px=0
				self.py+=1