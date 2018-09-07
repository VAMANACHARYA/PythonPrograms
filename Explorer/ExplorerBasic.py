import os 
#To get current directory
os.getcwd() 
#To change the directory
#os.chdir("DirName:\\dirname")
os.chdir("D:\\temp")
print ("Current Directory is: " + os.getcwd())

#to open explorer
os.system('explorer')
#open particular folder or file in explorer
os.startfile('D:\\PythonProg\Explorer.py')
#create dir in the current directory
os.mkdir("Vam_Created")
os.mkdir("Vam1_Deleted")
#Delete dir in the current directory
os.rmdir("Vam1_Deleted")
