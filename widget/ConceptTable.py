# # --
from DTPySide import *

from session.LobbySession import LobbySession
class ConceptTable(DTWidget.DTHorizontalTabel):
	
	conceptClicked=Signal(int)
	conceptDoubleClicked=Signal(int)
	conceptDropped=Signal(list)
	conceptReturnPressed=Signal(int)
	conceptDelete=Signal()
	conceptSort=Signal()

	def keyPressEvent(self, event: QKeyEvent):
		if event.key()==Qt.Key_Return:
			if self.currentRow()!=-1:
				id=int(self.item(self.currentRow(),0).text())
				self.conceptReturnPressed.emit(id)
		super().keyPressEvent(event)

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
		for model_index in self.selectionModel().selectedRows():
			row=model_index.row()
			id=str(int(self.item(row,0).text()))
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
		
		if event.mimeData().data("Key")==bytes("DTC","utf-8"):
			event.acceptProposedAction()
	
	def dragMoveEvent(self, event: QDragMoveEvent):
		# 统一一下
		event.acceptProposedAction()
	
	def dropEvent(self, event:QDropEvent):
		if event.mimeData().objectName()==self.objectName():
			super().dropEvent(event)
			self.conceptSort.emit()
		else:
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
					for model_index in self.selectionModel().selectedRows():
						row=model_index.row()
						id=int(self.item(row,0).text())
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
				
				pos=self.mapToGlobal(pos)+QPoint(0,self.horizontalHeader().height())
				menu.exec_(pos)
		else:
			super().mousePressEvent(event)

	def __init__(self, parent):
		super().__init__(parent=parent)
		self.setMinimumHeight(120)
		self.setColumn([QCoreApplication.translate("Concept", "ID"),QCoreApplication.translate("Concept", "Name")])

		self.itemClicked.connect(self.itemClickedSlot)
		self.itemDoubleClicked.connect(self.itemDoubleClickedSlot)

		# sort取消，手动重新赋值
		self.sortReset.connect(lambda:self.setConceptIDList(self.concept_id_list))
	
	def setHeadquarter(self,Headquarter: LobbySession):
		self.Headquarter=Headquarter
	
	def itemClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.item(self.currentRow(),0).text())
		self.conceptClicked.emit(id)

	def itemDoubleClickedSlot(self):
		"""双击table中的元素，emit附带concept id的conceptClicked信号（用于出去跳转展示concept）
		"""
		id=int(self.item(self.currentRow(),0).text())
		self.conceptDoubleClicked.emit(id)

	def appendConcept(self, id:int, name:str):

		self.StoreTableStatus()

		id=f"%{len(str(self.rowCount()))}s"%id
		id_item=QTableWidgetItem(id)
		name_item=QTableWidgetItem(name)
		name_item.setToolTip(self.Headquarter.getConceptTooltip(int(id)))
		self.addRow(self.rowCount(),[id_item,name_item])

		self.RestoreTableStatus()
		self.clearSelection()
		self.selectRow(self.rowCount()-1)
	
	def setConceptIDList(self, concept_id_list):
		"""设置concepttable为concept_id_list对应的concept_list，适用于diary、file的concept链接列表，以及concept的parent、relative的concept链接列表

		Args:
			concept_id_list (list): 是concept id的列表
		"""
		
		self.concept_id_list=concept_id_list

		self.StoreTableStatus()
		self.Clear()

		if concept_id_list!=[]:
			id_str_width=len(str(max(concept_id_list)))
		else:
			id_str_width=0
		
		row=0
		for concept_id in concept_id_list:
			concept=self.Headquarter.getConcept(concept_id)
			id=f"%{id_str_width}s"%concept["id"]
			name=concept["name"]
			id_item=QTableWidgetItem(id)
			name_item=QTableWidgetItem(name)
			name_item.setToolTip(self.Headquarter.getConceptTooltip(concept["id"]))
			self.addRow(row,[id_item,name_item])
			row+=1

		self.RestoreTableStatus()