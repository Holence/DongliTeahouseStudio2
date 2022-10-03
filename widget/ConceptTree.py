# # --
from DTPySide import *

from session.LobbySession import LobbySession
class ConceptTree(DTWidget.DTTree):
	
	conceptClicked=Signal(int)
	conceptDoubleClicked=Signal(int)
	conceptDropped=Signal(list)
	conceptDelete=Signal()

	def startDrag(self, actions:Qt.DropActions):
		######################################################################
		# MIME通信规则：
		# 
		# data/Key: bytes("DTC","utf-8")
		# 作为钥匙，在dragEnterEvent中检验，防止其他类型的drop进来
		# 
		# text/id_list: 495 9961 1
		# 其实不用这个，drop进来也完全可以和表格fit，只是这样方便处理数据，不用我再去一个个识别加进来的item了
		######################################################################
		
		indexes = self.selectedIndexes()
		mime = self.model().mimeData(indexes)
		
		id_list = ""
		for item in self.selectedItems():
			id=str(int(item.text(0)))
			id_list += id+" "
		
		#防止拖到自己的里面
		mime.setObjectName(self.objectName())
		mime.setData("Key",bytes("DTC","utf-8"))
		mime.setText(id_list)
		
		drag = QDrag(self)
		drag.setPixmap(IconFromCurrentTheme("hash.svg").pixmap(32,32))
		drag.setMimeData(mime)
		drag.exec_(actions)
	
	def dragEnterEvent(self, event:QDragEnterEvent):
		if event.mimeData().objectName()!=self.objectName():
			if event.mimeData().data("Key")==bytes("DTC","utf-8"):
					event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 统一一下
		event.acceptProposedAction()
	
	def dropEvent(self, event:QDropEvent):
		id_list=list(map(int,event.mimeData().text().split()))
		self.conceptDropped.emit(id_list)

	def mousePressEvent(self, event: QMouseEvent):
		if event.button()==Qt.RightButton:
			if len(self.selectionModel().selectedRows())==0:
				super().mousePressEvent(event)
			
			if len(self.selectionModel().selectedRows())>0:
				pos=event.pos()
				menu=QMenu()

				def slotOpenInNewWindow():
					for item in self.selectedItems():
						id=int(item.text(0))
						self.Headquarter.lobby.summon("concept","Concept")
						self.Headquarter.concept_heap[-1].concept_module.showConcept(id)
						MoveToCenterOfScreen(self.Headquarter.concept_heap[-1])
				
				actionOpen=QAction(QCoreApplication.translate("Concept", "Open In New Window"))
				actionOpen.setIcon(IconFromCurrentTheme("external-link.svg"))
				actionOpen.triggered.connect(slotOpenInNewWindow)
				menu.addAction(actionOpen)

				def slotDelete():
					self.conceptDelete.emit()
				
				actionDelete=QAction(QCoreApplication.translate("Concept", "Delete"))
				actionDelete.setIcon(IconFromCurrentTheme("trash-2.svg"))
				actionDelete.triggered.connect(slotDelete)
				menu.addAction(actionDelete)
							
				pos=self.mapToGlobal(pos)+QPoint(0,self.header().height())
				menu.exec_(pos)
		else:
			super().mousePressEvent(event)
	
	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(120)
		self.setColumn([QCoreApplication.translate("Concept", "ID"),QCoreApplication.translate("Concept", "Name")])

		self.itemClicked.connect(self.itemClickedSlot)
		self.itemDoubleClicked.connect(self.itemDoubleClickedSlot)

		self.setExpandCheckingColumn(0)

	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
	
	def itemClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.currentItem().text(0))
		self.conceptClicked.emit(id)
	
	def itemDoubleClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.currentItem().text(0))
		self.conceptDoubleClicked.emit(id)
	
	def setChildTree(self,root_id):
		
		def deepin(root_item,root_id):
			child_id_list=self.Headquarter.getConcept(root_id)["child"]

			if child_id_list!=[]:
				id_str_width=len(str(max(child_id_list)))
			else:
				id_str_width=0
			
			for child_id in child_id_list:
				if child_id not in stack:
					child_item=QTreeWidgetItem(root_item,[f"%{id_str_width}s"%child_id,self.Headquarter.getConcept(child_id)["name"]])
					child_item.setToolTip(1, self.Headquarter.getConceptTooltip(child_id))
					stack.append(child_id)
					deepin(child_item,child_id)
					stack.pop()
				else:
					child_item=QTreeWidgetItem(root_item,[f"%{id_str_width}s"%child_id,"*"+self.Headquarter.getConcept(child_id)["name"]])
					child_item.setToolTip(1, self.Headquarter.getConceptTooltip(child_id))
			
		self.StoreTreeStatus()
		self.clear()
		stack=[root_id]
		deepin(self.invisibleRootItem(),root_id)
		self.RestoreTreeStatus()