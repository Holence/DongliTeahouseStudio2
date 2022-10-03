# # --
from DTPySide import *

class ImageLabel(QLabel):

	titleChange=Signal(str)
	
	def previous(self):
		if self.index>0:
			self.index-=1
		elif self.index==0:
			self.index=len(self.pic_list)-1
		self.set_pic(self.index)
		
	def next(self):
		if self.index<len(self.pic_list)-1:
			self.index+=1
		elif self.index==len(self.pic_list)-1:
			self.index=0
		self.set_pic(self.index)
	
	def wheelEvent(self,event):
		super().wheelEvent(event)
		
		xscrolls = event.angleDelta().x()
		yscrolls = event.angleDelta().y()
		#上一张
		if xscrolls>0 or yscrolls>0:
			self.previous()
		#下一张
		elif xscrolls<0 or yscrolls<0:
			self.next()
	
	def __init__(self,pic_list,index):
		super().__init__()
		self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored) #不撑大
		self.setAlignment(Qt.AlignCenter) #图片、文字内容居中显示
		self.pic_list=pic_list
		self.index=index

		QShortcut(QKeySequence(Qt.Key_Left),self,activated=self.previous)
		QShortcut(QKeySequence(Qt.Key_Up),self,activated=self.previous)
		QShortcut(QKeySequence(Qt.Key_Right),self,activated=self.next)
		QShortcut(QKeySequence(Qt.Key_Down),self,activated=self.next)
	
	def refresh(self):
		self.set_pic(self.index)

	def set_pic(self,index):
		if os.path.getsize(self.pic_list[index])/1024/1024<50:
			pix=QPixmap(self.pic_list[index])
			
			pw,ph=pix.width(),pix.height()
			lw,lh=self.width(),self.height()

			if pw/lw>ph/lh:
				pix=pix.scaledToWidth(lw, Qt.SmoothTransformation)
			else:
				pix=pix.scaledToHeight(lh, Qt.SmoothTransformation)
			
			self.titleChange.emit("Dongli Teahouse Image Viewer - %s"%os.path.basename(self.pic_list[index])+" [%s/%s]"%(self.index+1,len(self.pic_list)))
			self.setPixmap(pix)
		else:
			self.titleChange.emit("Dongli Teahouse Image Viewer - %s"%os.path.basename(self.pic_list[index])+" [%s/%s]"%(self.index+1,len(self.pic_list)))
			self.setPixmap(QPixmap())
			self.setText("Image larger than 50MB.")

class ImageViewerSession(DTFrame.DTMainWindow):
	"MyImageViewer(pic_list,index)，传入包含所有url的pic_list，以及双击打开时的index"

	def resizeEvent(self, event):
		super().resizeEvent(event)
		self.image_label.refresh()
	
	def closeEvent(self, event):
		super().closeEvent(event)
		self.deleteLater()

	def __init__(self,app,pic_list,index):
		super().__init__(app)
		self.image_label=ImageLabel(pic_list,index)

	def initializeWindow(self):
		super().initializeWindow()
		self.setWindowTitle("Dongli Teahouse Image Viewer")
		self.setCentralWidget(self.image_label)
		
		self.setMinimumSize(600,500)
		self.image_label.refresh()

		self.resize(self.minimumWidth(),self.minimumHeight())
		self.adjustSize()
		MoveToCenterOfScreen(self)
		
	def initializeSignal(self):
		super().initializeSignal()
		self.image_label.titleChange.connect(self.setWindowTitle)