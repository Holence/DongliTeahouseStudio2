import os

def deepin(base):
	
	base=os.path.abspath(base)
	os.chdir(base)

	for i in os.listdir("./"):
		if os.path.isdir(i):
			deepin(i)
			os.chdir(base)
		else:
			ext=os.path.splitext(i)[1]
			if ext==".ui" or ext==".py":
				ui_list.append(" "+os.path.abspath(i))

ui_list=[]
base=os.getcwd()
deepin(base)
os.system("pyside2-lupdate %s -ts en@.ts"%("".join(ui_list)))