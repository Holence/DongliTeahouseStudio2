# # --
from DTPySide import *

from session import LobbySession
from module.Ui_LibraryCheck import Ui_LibraryCheck
class LibraryCheck(Ui_LibraryCheck,QWidget):
	"""写的跟狗屎一样

	Args:
		Ui_LibraryCheck (狗屎): 臭狗屎
		QWidget (狗屎): 臭狗屎
	"""
	def __init__(self,Headquarter:LobbySession):
		super().__init__()
		self.setupUi(self)
		self.Headquarter=Headquarter

		self.plainTextEdit.setStyleSheet("font-size: 10pt")
		
		self.initializeSignal()
		self.refresh()
	
	def initializeSignal(self):
		self.pushButton_refresh.clicked.connect(self.refresh)
		self.pushButton_erase.clicked.connect(self.erase)
		self.pushButton_add.clicked.connect(self.add)
		self.pushButton_replace.clicked.connect(self.replace)
		self.pushButton_move_replace.clicked.connect(self.move_replace)
	
	def erase(self):
		erase_list=[]
		for model_index in self.missing.selectionModel().selectedRows():
			row=model_index.row()
			y,m,d=map(int,self.missing.item(row,1).text().split("."))
			date=QDate(y,m,d)
			type=int(self.missing.item(row,0).text())
			name=self.missing.item(row,3).text()
			url=self.Headquarter.extractFileURL(self.missing.item(row,4).text())
			erase_list.append(self.Headquarter.generateDiaryConceptFileDict(date,type,name,url))
			self.plainTextEdit.appendPlainText("Erased %s\n"%name)
		
		self.Headquarter.deleteLibraryFile(erase_list,delete_operation=False)
		self.refresh()

	def add(self):
		for model_index in self.redundant.selectionModel().selectedRows():
			row=model_index.row()
			url=self.redundant.item(row).text()
			y,m,d,_=self.Headquarter.extractFileURL(url).split("/")
			date=QDate(int(y),int(m),int(d))
			self.Headquarter.addLibraryFile(date,"file:///"+url,[],move_from_outside=False)
			self.plainTextEdit.appendPlainText("Added %s\n"%url)
		
		self.refresh()
	
	def replace(self):
		if self.left.rowCount()!=self.right.count():
			DTFrame.DTMessageBox(self,"Warning","The files in Left and Right doesn't match!",DTIcon.Warning())
			return
		
		for row in range(self.left.rowCount()):
			y,m,d=map(int,self.left.item(row,1).text().split("."))
			date=QDate(y,m,d)
			origin_name=self.left.item(row,3).text()

			replicant_url=self.right.item(row).text()
			
			new_y,new_m,new_d=map(int,self.Headquarter.extractFileURL(replicant_url).split("/")[:3])
			new_date=QDate(new_y,new_m,new_d)
			
			if os.path.isdir(replicant_url):
				TYPE=0 # folder=0
			else:
				TYPE=1 # file=1
			
			new_name=os.path.basename(replicant_url)
			
			self.Headquarter.renameLibraryFile(date,origin_name,new_name,rename_operation=False,new_file_type=TYPE,new_date=new_date)
			self.plainTextEdit.appendPlainText("Replaced %s in %s.%s.%s to %s in %s.%s.%s\n"%(origin_name,y,m,d,new_name,new_y,new_m,new_d))
		
		self.refresh()
	
	def move_replace(self):
		if self.left.rowCount()!=self.right.count():
			DTFrame.DTMessageBox(self,"Warning","The files in Left and Right doesn't match!",DTIcon.Warning())
			return
		
		for row in range(self.left.rowCount()):
			y,m,d=map(int,self.left.item(row,1).text().split("."))
			date=QDate(y,m,d)
			origin_name=self.left.item(row,3).text()
			origin_url=self.left.item(row,4).text()

			replicant_url=self.right.item(row).text()
			
			if os.path.isdir(replicant_url):
				TYPE=0 # folder=0
			else:
				TYPE=1 # file=1
			
			try:
				origin_base=os.path.dirname(origin_url)
				if os.path.dirname(replicant_url)!=origin_base:
					Win32_Shellmove(replicant_url,origin_base)
			except Exception as e:
				DTFrame.DTMessageBox(self,"Error",str(e),DTIcon.Error())
			
			new_name=os.path.basename(replicant_url)
			
			self.Headquarter.renameLibraryFile(date,origin_name,new_name,rename_operation=False,new_file_type=TYPE)
			self.plainTextEdit.appendPlainText("Replaced %s to %s and moved from %s to %s\n"%(origin_name,new_name,origin_url,replicant_url))
		
		self.refresh()

	def refresh(self):
		self.missing.clearContents()
		self.missing.setRowCount(0)
		self.left.clearContents()
		self.left.setRowCount(0)
		self.redundant.clear()
		self.right.clear()

		data=self.Headquarter.getLibraryData()

		base=self.Headquarter.library_base

		# 判断library有，而basedir中没有的
		missing_file_list=[]
		for year in data:
			for month in data[year]:
				for day in data[year][month]:
					library_file_list=[file_name for file_name in data[year][month][day].keys() if data[year][month][day][file_name]["type"]!=2]
					
					if os.path.exists(base+"/%s/%s/%s/"%(year,month,day)):
						base_file_list=os.listdir(base+"/%s/%s/%s/"%(year,month,day))
					else:
						base_file_list=[]
					
					for file_name in List_Difference(library_file_list,base_file_list):
						file=data[year][month][day][file_name]
						missing_file_list.append(self.Headquarter.generateDiaryConceptFileDict(QDate(int(year),int(month),int(day)),file["type"],file_name,file["url"]))

		redundant_file_list=[]
		for year_dir in os.listdir(base):
			if str.isdigit(year_dir):
				year=year_dir
				year_dir=os.path.join(base,year_dir).replace("\\","/")
				if os.path.isdir(year_dir):
					for month_dir in os.listdir(year_dir):
						if str.isdigit(month_dir):
							month=month_dir
							month_dir=os.path.join(year_dir,month).replace("\\","/")
							if os.path.isdir(month_dir):
								for day_dir in os.listdir(month_dir):
									if str.isdigit(day_dir):
										day=day_dir
										day_dir=os.path.join(month_dir,day).replace("\\","/")
										if os.path.isdir(day_dir):
											for file_name in os.listdir(day_dir):
												try:
													data[year][month][day][file_name]
													# link名字和文件夹名相同
													if data[year][month][day][file_name]["type"]==2:
														redundant_file_list.append(os.path.join(day_dir,file_name).replace("\\","/"))
												except:
													redundant_file_list.append(os.path.join(day_dir,file_name).replace("\\","/"))
		row=0
		for file in missing_file_list:
			y=file["y"]
			m=file["m"]
			d=file["d"]
			type=file["type"]
			name=file["name"]
			url=file["url"]
			url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
			if type==0:
				ext="folder"
			elif type==1:
				url=os.path.join(self.Headquarter.library_base,url).replace("\\","/")
				ext=os.path.splitext(url)[1].lower()[1:]
			elif type==2:
				ext="link"

			self.missing.insertRow(row)
			self.missing.setItem(row,0,QTableWidgetItem(str(type)))
			self.missing.setItem(row,1,QTableWidgetItem("%s.%s.%s"%(y,m,d)))
			self.missing.setItem(row,2,QTableWidgetItem(ext))
			self.missing.setItem(row,3,QTableWidgetItem(name))
			self.missing.setItem(row,4,QTableWidgetItem(url))
			row+=1
		
		for i in redundant_file_list:
			self.redundant.addItem(i)