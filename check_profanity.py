#! /usr/bin/env python
import urllib

def read_text():
	quotes = open('/home/rodrigo/Documentos/python/doc')
	contents_of_file = quotes.read()
	# print(contents_of_file)
	quotes.close()
	check_profanity_function(contents_of_file)

def check_profanity_function(text):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text)
	output = connection.read()
	#print(output)
	connection.close()

	if "true" in output:
		print(">>>>>>ALERT>>>>>>>Profanity Alert")
	elif "false" in output:
		print(">>>>>>Document all right>>>>>>>>>")
	else:
		print(">>>>>>Document not inspect>>>>>>>")

read_text()
