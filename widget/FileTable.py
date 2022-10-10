# # --
from DTPySide import *

class FileTable(DTWidget.DTHorizontalTabel):

	fileDropped=Signal(list,list)
	fileDelete=Signal()
	fileSorted=Signal()
	
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
			
			type=int(self.item(row,0).text())
			y,m,d=map(int,self.item(row,1).text().split("."))
			name=self.item(row,3).text()
			url=self.Headquarter.extractFileURL(self.item(row,4).text())
			file_list.append(self.Headquarter.generateDiaryConceptFileDict(QDate(y,m,d),type,name,url))

			if type!=2:
				url="file:///"+self.item(row,4).text()
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
		if event.mimeData().objectName()==self.objectName() and "Library" not in self.objectName():
			# 拖到自己
			# event.ignore()
			event.acceptProposedAction()
		elif event.mimeData().objectName()!="" and self.objectName()=="LibraryFileTable":
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
		if event.mimeData().objectName()==self.objectName():
			super().dropEvent(event)
			self.fileSorted.emit()
		else:
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

				type=int(self.item(row,0).text())
				y,m,d=map(int,self.item(row,1).text().split("."))
				name=self.item(row,3).text()
				url=self.Headquarter.extractFileURL(self.item(row,4).text())
				file=self.Headquarter.generateDiaryConceptFileDict(QDate(y,m,d),type,name,url)
				
				from widget.FileTab import LoadThumbnailThread
				loading_thread=LoadThumbnailThread(self,self.Headquarter,file,row,force=True)
				loading_thread.finished.connect(loading_thread.deleteLater)
				loading_thread.start()
		
		def slotRename():
			row=self.currentRow()
			y,m,d=map(int,self.item(row,1).text().split("."))
			date=QDate(y,m,d)
			old_name=self.item(row,3).text()

			dlg=DTFrame.DTDialog(self.window(),"Rename")
			w=QWidget()
			l=QVBoxLayout(w)
			l.setMargin(0)
			
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
			dlg.setMinimumWidth(400)

			dlg.adjustSize()
			MoveToCenterOfScreen(dlg)

			if dlg.exec_():
				new_name=line_edit2.text()
				res=self.Headquarter.renameLibraryFile(date,old_name,new_name)
				if res!=False:
					self.window().refresh()
		
		def slotDate():
			row=self.currentRow()
			y,m,d=map(int,self.item(row,1).text().split("."))
			old_date=QDate(y,m,d)
			name=self.item(row,3).text()
			url=self.item(row,4).text()

			dlg=DTFrame.DTDialog(self.window(),"Edit Date")
			w=QWidget()
			l=QVBoxLayout(w)
			l.setMargin(0)
			
			lable1=QLabel("Old Date")
			l.addWidget(lable1)

			date_edit1=QDateEdit()
			date_edit1.setDisplayFormat("yyyy.MM.dd")
			date_edit1.setReadOnly(True)
			date_edit1.setDate(old_date)
			l.addWidget(date_edit1)

			lable2=QLabel("New Date")
			l.addWidget(lable2)

			date_edit2=QDateEdit()
			date_edit2.setDisplayFormat("yyyy.MM.dd")
			date_edit2.setDate(old_date)
			l.addWidget(date_edit2)

			w.setLayout(l)

			dlg.setCentralWidget(w)
			dlg.setMinimumWidth(300)

			dlg.adjustSize()
			MoveToCenterOfScreen(dlg)

			if dlg.exec_():
				new_date=date_edit2.date()
				if new_date!=old_date:
					
					if url[:4]!="http":
						if not os.path.exists(url):
							DTFrame.DTMessageBox(self.window(),"Error","Cannot access to Library at %s"%url,DTIcon.Error())
							return
						
						try:
							new_base=self.Headquarter.library_base+"/%s/%s/%s"%(new_date.year(),new_date.month(),new_date.day())
							if not os.path.exists(new_base):
								os.makedirs(new_base)
							Win32_Shellmove(url,new_base)
						except Exception as e:
							DTFrame.DTMessageBox(self.window(),"Error",str(e),DTIcon.Error())
							return
					
					res=self.Headquarter.renameLibraryFile(old_date,name,name,new_date=new_date)
					if res!=False:
						self.window().refresh()
		
		def slotImage():
			url=self.item(self.currentRow(),4).text()
			if os.path.exists(url):
				pic_list=[self.item(row,4).text() for row in range(self.rowCount()) if self.item(row,2).text().lower() in image_extension]
				index=pic_list.index(url)
				from session import ImageViewerSession
				self.imageviewer=ImageViewerSession(self.Headquarter.app,pic_list,index)
				self.imageviewer.initialize()
				ShowUp(self.imageviewer)
			else:
				DTFrame.DTMessageBox(self.window(),"Error","%s does not exist! Try running Check Library."%url,DTIcon.Error())

		def slotLocation():
			url=self.item(self.currentRow(),4).text().replace("/","\\")#呵window得用反斜线
			try:
				os.popen("explorer /select,\"%s\""%url)
			except Exception as e:
				DTFrame.DTMessageBox(self.window(),"Warning","%s does not exist! Try running Check Library.\n\n%s"%(url,e),DTIcon.Warning())

		# def slotCopy():
		# 	copy_list=[]
		# 	for model_index in self.selectionModel().selectedRows():
		# 		row=model_index.row()
		# 		type=int(self.item(row,0).text())
		# 		url=self.item(row,4).text().replace("/","\\")
		# 		if type!=2:
		# 			copy_list.append(url)
			
		# 	if copy_list==[]:
		# 		DTFrame.DTMessageBox(self.window(),"Warning","There is nothing can be copied.",DTIcon.Warning())
		# 		return
			
		# 	dlg=QFileDialog(self)
		# 	dst=dlg.getExistingDirectory().replace("/","\\")
		# 	if dst!="":
		# 		try:
		# 			res=Win32_Shellcopy(copy_list,dst)
		# 			if res==True:
		# 				os.startfile(dst)
		# 			else:
		# 				DTFrame.DTMessageBox(self.window(),"Error","Copy Failed",DTIcon.Error())
		# 		except Exception as e:
		# 			DTFrame.DTMessageBox(self.window(),"Error","Error occured: %s\n\nTry running Check Library."%e,DTIcon.Error())
		
		def slotDelete():
			self.fileDelete.emit()

		def slotCopyPath():
			text=""
			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()
				url=self.item(row,4).text().replace("/","\\")#呵window得用反斜线
				text+=url+"\n"
			clip=QGuiApplication.clipboard()
			clip.setText(text[:-1])
		
		def slotCopyFile():
			url_list = []
			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()
				
				type=int(self.item(row,0).text())
				url=self.Headquarter.extractFileURL(self.item(row,4).text())

				if type!=2:
					url="file:///"+self.item(row,4).text()
					url_list.append(QUrl(url))
			
			mime=QMimeData()
			mime.setUrls(url_list)
			clip=QGuiApplication.clipboard()
			clip.setMimeData(mime)
		
		def slotOpenInNewLibrary():
			file_list=[]
			for model_index in self.selectionModel().selectedRows():
				row=model_index.row()
				
				type=int(self.item(row,0).text())
				y,m,d=map(int,self.item(row,1).text().split("."))
				name=self.item(row,3).text()
				
				file_dict=self.Headquarter.generateLibraryFileDict(QDate(y,m,d),type,name)
				file_list.append(file_dict)
			
			self.Headquarter.lobby.summon("library","Library")
			library=self.Headquarter.library_heap[-1].library_module
			library.fileTab.setFileList(file_list)

			MoveToCenterOfScreen(self.Headquarter.library_heap[-1])
	
		if "Bookmark" in self.objectName():
			super().mousePressEvent(event)
			return

		pos=event.pos()
		if event.button()==Qt.RightButton:
			
			if len(self.selectionModel().selectedRows())==0:
				super().mousePressEvent(event)

			if len(self.selectionModel().selectedRows())>0:
				menu=QMenu()

				ext=self.item(self.currentRow(),2).text()
				if len(self.selectionModel().selectedRows())==1:
					actionRename=QAction(QCoreApplication.translate("Library", "Rename"))
					actionRename.triggered.connect(slotRename)
					actionRename.setIcon(IconFromCurrentTheme("edit-3.svg"))
					menu.addAction(actionRename)

					actionEditDate=QAction(QCoreApplication.translate("Library", "Eidt Date"))
					actionEditDate.triggered.connect(slotDate)
					actionEditDate.setIcon(IconFromCurrentTheme("calendar.svg"))
					menu.addAction(actionEditDate)

					from filetype import image_extension
					if ext.lower() in image_extension:
						actionViewImage=QAction(QCoreApplication.translate("Library", "View in ImageViewer"))
						actionViewImage.triggered.connect(slotImage)
						actionViewImage.setIcon(IconFromCurrentTheme("image.svg"))
						menu.addAction(actionViewImage)

					if ext!="link":
						actionOpenLocation=QAction(QCoreApplication.translate("Library", "Open File Location"))
						actionOpenLocation.triggered.connect(slotLocation)
						actionOpenLocation.setIcon(IconFromCurrentTheme("folder.svg"))
						menu.addAction(actionOpenLocation)
				
				actionOpen=QAction(QCoreApplication.translate("Library", "Open In New Library"))
				actionOpen.setIcon(IconFromCurrentTheme("external-link.svg"))
				actionOpen.triggered.connect(slotOpenInNewLibrary)
				menu.addAction(actionOpen)

				actionCopyFile=QAction(QCoreApplication.translate("Library", "Copy File"))
				actionCopyFile.triggered.connect(slotCopyFile)
				actionCopyFile.setIcon(IconFromCurrentTheme("copy.svg"))
				menu.addAction(actionCopyFile)

				actionCopyPath=QAction(QCoreApplication.translate("Library", "Copy File Path"))
				actionCopyPath.triggered.connect(slotCopyPath)
				actionCopyPath.setIcon(IconFromCurrentTheme("code.svg"))
				menu.addAction(actionCopyPath)
				
				# if ext!="link":
				# actionCopy=QAction(QCoreApplication.translate("Library", "Copy to..."))
				# actionCopy.triggered.connect(slotCopy)
				# actionCopy.setIcon(IconFromCurrentTheme("share.svg"))
				# menu.addAction(actionCopy)
				
				actionRefreshIcon=QAction(QCoreApplication.translate("Library", "Refresh Icon"))
				actionRefreshIcon.triggered.connect(slotRefresh)
				actionRefreshIcon.setIcon(IconFromCurrentTheme("refresh-cw.svg"))
				menu.addAction(actionRefreshIcon)

				actionDelete=QAction(QCoreApplication.translate("Library", "Delete"))
				actionDelete.triggered.connect(slotDelete)
				actionDelete.setIcon(IconFromCurrentTheme("trash-2.svg"))
				menu.addAction(actionDelete)
				
				pos=self.mapToGlobal(pos)+QPoint(0,self.horizontalHeader().height())
				menu.exec_(pos)
		else:
			super().mousePressEvent(event)

	def __init__(self, parent):
		super().__init__(parent=parent)
		
		self.setColumn([QCoreApplication.translate("Library", "Type"),QCoreApplication.translate("Library", "Date"),QCoreApplication.translate("Library", "Ext"),QCoreApplication.translate("Library", "File"),QCoreApplication.translate("Library", "Url")])
		self.setColumnHidden(4,True)
		self.setColumnWidth(1,100)

		self.setIconSize(QSize(32,32))

		self.lock=QMutex(QMutex.NonRecursive) # 更新icon时防止多线程在刷新完列表之前就去更新
		self.thread_list=[]

	def Clear(self):
		self.lock.lock()
		super().Clear()
		self.lock.unlock()