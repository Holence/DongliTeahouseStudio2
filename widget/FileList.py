# # --
from DTPySide import *

class FileList(QListWidget):

	fileDropped=Signal(list,list)
	fileDelete=Signal()

	def eventFilter(self, watched: QObject, event:QEvent) -> bool:
		if event.type()==QEvent.KeyPress:
			if event.key()==Qt.Key_Control:
				self.__ctrlPressed=True
		if event.type()==QEvent.KeyRelease:
			if event.key()==Qt.Key_Control:
				self.__ctrlPressed=False
		return False # 这里是让继续延续event的处理，不要被filter掉了

	def wheelEvent(self, event: QWheelEvent):
		if self.__ctrlPressed==True:
			xscrolls = event.angleDelta().x()
			yscrolls = event.angleDelta().y()
			
			#放大
			if xscrolls>0 or yscrolls>0:
				icon_size=self.iconSize()+QSize(self.step,self.step)
				grid_size=self.gridSize()+QSize(self.step,self.step)
			#缩小
			elif xscrolls<0 or yscrolls<0 and self.iconSize().width()-self.step>32:
				icon_size=self.iconSize()-QSize(self.step,self.step)
				grid_size=self.gridSize()-QSize(self.step,self.step)
			else:
				return False
			
			self.setIconSize(icon_size)
			self.setGridSize(grid_size)
		else:
			super().wheelEvent(event)
		
	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# text/url_list: 来自内部，["file:///E:/dlcw/2021/7/21/a.txt","https://www.google.com"]；
		#                来自外部，则为windows explorer的drag event自带的url_list
		# FileList: 来自内部，[{
		# 	"y":y,
		# 	"m":m,
		# 	"d":d,
		# 	"type":type,
		# 	"name":name,
		# 	"url":url
		# }]
		#                来自外部，为[]
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)
		
		url_list = []
		file_list=[]
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			
			url=self.item(row).toolTip().replace(self.Headquarter.library_base+"/","")
			if url[:4]=="http":
				name=self.item(row).text()
				date=QDate().fromString(name[name.rfind("|")+1:][1:-1],"yyyy.M.d")
				name=name[:name.rfind("|")]
			else:
				y,m,d=url.split("/")[:3]
				date=QDate(int(y),int(m),int(d))
				name=self.item(row).text()

			type=self.Headquarter.getLibraryFile(date,name)["type"]
			file_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))

			if type!=2:
				url="file:///"+self.item(row).toolTip()
			url_list.append(QUrl(url))
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setUrls(url_list)
		mime.setData("FileList",bytes(json.dumps(file_list),encoding="utf-8"))
		
		drag = QDrag(self)
		drag.setPixmap(IconFromCurrentTheme("inbox.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().objectName()==self.objectName():
			# 拖到自己
			event.ignore()
		elif event.mimeData().objectName()!="" and self.objectName()=="LibraryFileList":
			# 内部不允许拖到LibraryFileTable\LibraryFileList
			if "Bookmark" in event.mimeData().objectName():
				# Bookmark的算作外来，可以拖到LibraryFileTable\LibraryFileList
				event.acceptProposedAction()
			else:
				event.ignore()
		elif event.mimeData().hasUrls():
			event.acceptProposedAction()
		elif event.mimeData().hasText():
			# Text形式的url批量导入
			if [False for url in event.mimeData().text().split() if "http" not in url].count(False)==0:
				event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 淦！为什么接受资源管理器拖进来的文件，还得implement这个event。
		# 找这个Bug花了我将近一个小时的时间？！茶屋工作室1.0里就不用的？！！
		event.acceptProposedAction()

	def dropEvent(self, event:QDropEvent):

		if event.mimeData().hasUrls():
			url_list=[url.toString() for url in event.mimeData().urls()]
		elif event.mimeData().hasText():
			url_list=[url.strip() for url in event.mimeData().text().split()]
		
		if "Bookmark" not in event.mimeData().objectName():
			try:
				file_list=json.loads((event.mimeData().data("FileList").data().decode("utf-8")))
			except:
				file_list=[]
		else:
			# BookmarkParser中拖出来的，先把标准型filedict放在url_list，在再drop的时候把filedict付给url_list，再把filedict置空（得算作外部的来对待），最后在headquarter的addLibraryFile的时候侦测类型
			file_list=json.loads((event.mimeData().data("FileList").data().decode("utf-8")))
			url_list=copy.deepcopy(file_list)
			file_list=[]
		
		self.fileDropped.emit(url_list,file_list)
	
	def mousePressEvent(self, event: QMouseEvent):
		def slotRefresh():

			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()

				url=self.item(row).toolTip().replace(self.Headquarter.library_base+"/","")
				if url[:4]=="http":
					name=self.item(row).text()
					date=QDate().fromString(name[name.rfind("|")+1:][1:-1],"yyyy.M.d")
					name=name[:name.rfind("|")]
				else:
					y,m,d=url.split("/")[:3]
					date=QDate(int(y),int(m),int(d))
					name=self.item(row).text()

				type=self.Headquarter.getLibraryFile(date,name)["type"]
				file=self.Headquarter.generateDiaryConceptFileDict(date,type,name,url)
				
				from widget.FileTab import LoadThumbnailThread
				loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,force=True)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
		
		def slotRename():
			url=self.currentItem().toolTip().replace(self.Headquarter.library_base+"/","")
			if url[:4]=="http":
				name=self.currentItem().text()
				date=QDate().fromString(name[name.rfind("|")+1:][1:-1],"yyyy.M.d")
				old_name=name[:name.rfind("|")]
			else:
				y,m,d=url.split("/")[:3]
				date=QDate(int(y),int(m),int(d))
				old_name=self.currentItem().text()

			dlg=DTFrame.DTDialog(self.window(),"Rename")
			w=QWidget()
			l=QVBoxLayout(w)
			
			lable1=QLabel("Old Name")
			l.addWidget(lable1)

			line_edit1=QLineEdit(old_name)
			line_edit1.setReadOnly(True)
			l.addWidget(line_edit1)

			lable2=QLabel("New Name")
			l.addWidget(lable2)
			line_edit2=QLineEdit(old_name)
			l.addWidget(line_edit2)

			w.setLayout(l)

			dlg.setCentralWidget(w)
			dlg.setMinimumSize(600,300)

			if dlg.exec_():
				new_name=line_edit2.text()
				res=self.Headquarter.renameLibraryFile(date,old_name,new_name)
				if res!=False:
					self.window().refresh()

		def slotImage():
			url=self.item(self.currentRow()).toolTip()
			if os.path.exists(url):
				pic_list=[self.item(row).toolTip() for row in range(self.count()) if os.path.splitext(self.item(row).text())[1][1:].lower() in image_extension]
				index=pic_list.index(url)
				from session import ImageViewerSession
				self.imageviewer=ImageViewerSession(self.Headquarter.app,pic_list,index)
				self.imageviewer.initialize()
				self.imageviewer.show()
			else:
				DTFrame.DTMessageBox(self.window(),"Error","%s does not exist! Try running Check Library."%url,DTIcon.Error())
		
		def slotLocation():
			url=self.item(self.currentRow()).toolTip().replace("/","\\")#呵window得用反斜线
			try:
				os.popen("explorer /select,\"%s\""%url)
			except Exception as e:
				DTFrame.DTMessageBox(self.window(),"Warning","%s does not exist! Try running Check Library.\n\n%s"%(url,e),DTIcon.Warning())
		
		def slotCopy():
			copy_list=[]
			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()
				url=self.item(row).toolTip().replace("/","\\")
				if url[:4]!="http":
					copy_list.append(url)
			
			if copy_list==[]:
				DTFrame.DTMessageBox(self.window(),"Warning","There is nothing can be copied.",DTIcon.Warning())
				return
				
			dlg=QFileDialog(self)
			dst=dlg.getExistingDirectory().replace("/","\\")
			if dst!="":
				try:
					res=Win32_Shellcopy(copy_list,dst)
					if res==True:
						os.startfile(dst)
					else:
						DTFrame.DTMessageBox(self.window(),"Error","Copy Failed",DTIcon.Error())
				except Exception as e:
					DTFrame.DTMessageBox(self.window(),"Error","Error occured: %s\n\nTry running Check Library."%e,DTIcon.Error())
		
		def slotDelete():
			self.fileDelete.emit()
		
		if "Bookmark" in self.objectName():
			super().mousePressEvent(event)
			return
		
		pos=event.pos()
		if event.button()==Qt.RightButton:
			
			if len(self.selectionModel().selectedRows())==0:
				super().mousePressEvent(event)
			
			if len(self.selectionModel().selectedRows())>0:
				menu=QMenu()
				menu.setStyleSheet("font-size:12pt")

				name=self.item(self.currentRow()).text()
				ext=os.path.splitext(name)[1][1:]
				if len(self.selectionModel().selectedRows())==1:
					actionRename=QAction(QCoreApplication.translate("Library", "Rename"))
					actionRename.triggered.connect(slotRename)
					actionRename.setIcon(IconFromCurrentTheme("edit-3.svg"))
					menu.addAction(actionRename)
					
					from filetype import image_extension
					if ext.lower() in image_extension:
						actionViewImage=QAction(QCoreApplication.translate("Library", "View in ImageViewer"))
						actionViewImage.triggered.connect(slotImage)
						actionViewImage.setIcon(IconFromCurrentTheme("image.svg"))
						menu.addAction(actionViewImage)
					
					if "|" not in name:
						actionOpenLocation=QAction(QCoreApplication.translate("Library", "Open File Location"))
						actionOpenLocation.triggered.connect(slotLocation)
						actionOpenLocation.setIcon(IconFromCurrentTheme("folder.svg"))
						menu.addAction(actionOpenLocation)

				# if "|" not in name:
				actionCopy=QAction(QCoreApplication.translate("Library", "Copy to..."))
				actionCopy.triggered.connect(slotCopy)
				actionCopy.setIcon(IconFromCurrentTheme("copy.svg"))
				menu.addAction(actionCopy)
				
				actionRefreshIcon=QAction(QCoreApplication.translate("Library", "Refresh Icon"))
				actionRefreshIcon.triggered.connect(slotRefresh)
				actionRefreshIcon.setIcon(IconFromCurrentTheme("refresh-cw.svg"))
				menu.addAction(actionRefreshIcon)

				actionDelete=QAction(QCoreApplication.translate("Library", "Delete"))
				actionDelete.triggered.connect(slotDelete)
				actionDelete.setIcon(IconFromCurrentTheme("trash-2.svg"))
				menu.addAction(actionDelete)
				
				pos=self.mapToGlobal(pos)
				menu.exec_(pos)
		else:
			super().mousePressEvent(event)
	
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(150)
		
		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setDragEnabled(True)
		self.setDragDropMode(QAbstractItemView.DragDrop)
		self.setViewMode(QListView.IconMode)

		self.setStyleSheet("""
		QListWidget::item:!selected{
			background:transparent;
			border:none;
		}
		""")
		
		self.step=4
		self.setIconSize(QSize(self.step*10,self.step*10))
		self.setGridSize(QSize(self.step*15,self.step*20))
		self.setWordWrap(True)
		
		self.setResizeMode(QListView.Adjust)
		self.__ctrlPressed=False
		self.installEventFilter(self)

		self.lock=QMutex(QMutex.NonRecursive) # 更新icon时防止多线程在刷新完列表之前就去更新
		self.thread_list=[]
	
	def Clear(self):
		self.lock.lock()
		super().clear()
		self.lock.unlock()