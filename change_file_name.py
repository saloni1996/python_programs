import os

def rename_file():
   file_list=os.listdir(r"xyz/prank") #the file where prank folder is saved
   saved_path=os.getcwd()
   #print(saved_path)
   os.chdir(r"xyz/prank") #the file location
   #print(file_list)
   for file_name in file_list:
	os.rename(file_name,file_name.translate(None,"0123456789"))


rename_file()
