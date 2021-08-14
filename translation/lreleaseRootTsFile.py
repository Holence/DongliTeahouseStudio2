import os

os.chdir(os.path.dirname(__file__))
for i in os.listdir("./"):
    name=os.path.splitext(i)[0]
    ext=os.path.splitext(i)[1]
    if ext==".ts":
        os.system("lrelease %s -qm %s.qm"%(i,name))