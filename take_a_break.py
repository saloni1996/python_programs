import time
import webbrowser

num = 1
while( num <=3 ):
	time.sleep(20)
	print("Current system time is:"+ time.ctime())
	webbrowser.open("http://www.google.com/")
	num +=1

