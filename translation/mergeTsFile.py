import os

os.chdir(os.path.dirname(__file__))
for i in os.listdir("./"):
	name=os.path.splitext(i)[0]
	ext=os.path.splitext(i)[1]
	if ext==".ts" and "@" not in name:
		if os.path.exists("./%s@.ts"%name):
			os.system("lrelease %s %s -qm %s.qm"%(i,name+"@.ts",name))