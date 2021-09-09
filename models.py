import os
import shutil
#print(os.system("date"))
#os.mkdir("/Users/yasi/Desktop/py")
#print(os.getcwd())
#print(os.path.exists("/Users/yasi/Desktop/py"))
#x=os.path.splitext('/Users/yasi/Desktop/py/file.py')
#print(x[1])
#print(os.listdir())
source = input("enter source folder: ")
des = input(" enter destination folder: ")
source = source+"/"
des = des+"/"
files = os.listdir(source)
for i in files: 
    shutil.copy((source+i), des)

