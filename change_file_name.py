import os

def rename_file():
   file_list=os.listdir(r"/media/mmps/E406FC9006FC64C8/lectures/udacity/python/prank")
   saved_path=os.getcwd()
   #print(saved_path)
   os.chdir(r"/media/mmps/E406FC9006FC64C8/lectures/udacity/python/prank")
   #print(file_list)
   for file_name in file_list:
	os.rename(file_name,file_name.translate(None,"0123456789"))


rename_file()                                                                      
