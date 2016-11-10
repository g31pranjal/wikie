import sqlite3 as sql
from os import listdir
from os.path import isfile, join
import math
import urllib2
from bs4 import BeautifulSoup as bs
def sanitise(word):
	newword=''
	for i in word:
		if i=='?' or i=='#' or i=='%' or i=='$' or i=='(' or i==')':
			continue
		newword+=i	
	return word

def function(url):
	tl=url.split('/')
	
	tk=tl[2].split('_')
	tokens=[]
	for i in tk:
		tf=sanitise(i)
		tokens.append(tf)
	newurl=''
	for i in range(0,len(tokens)):
		newurl+=tokens[i]+' ' 
	return newurl

def weights():
	lst = []
	lst1=[]
	connect = sql.connect('cntrl/worker.db')
	cursor  = connect.cursor()
	cursor.execute("SELECT `url` from `pages`")
	r = cursor.fetchone()
	print 'selecting tupples'
	l=0
	while r is not None:
		string  = r[0]
		l+=1
		print l
		temp=function(string)
		#temp = soup.title.string
		print temp
		lst.append(temp)
		lst1.append(string)

		r = cursor.fetchone()

	print 'read the table'	
	for i in range(0,len(lst)):
		print i
		cursor.execute("UPDATE `pages` SET `title` ='"+ lst[i]+"' WHERE `url`='"+lst1[i]+"'")
	connect.commit()	


weights()
#print function('/wiki/Football_at_the_1964_Summer_Olympics')



	