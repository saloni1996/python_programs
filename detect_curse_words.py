import urllib

def read_text():
	quotes = open("/media/mmps/E406FC9006FC64C8/lectures/udacity/python/quotes.txt")
	#Enter the location of your file whose contents have to be checked
	data = quotes.read()
	#print(data)
	quotes.close()
	check_profanity(data)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wydl.com?q="+text_to_check)
	output = connection.read()
	#to print output
	#print(output)
	connection.close()
	if "true" in output:
		print ("OOPS! Curse word present")
	elif "false" in output:
		print("Curse Word present!!")
	else:
		print("Couldn't scan the dataset")


read_text()
