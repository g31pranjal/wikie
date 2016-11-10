import sqlite3 as sql
from os import listdir
from os.path import isfile, join
import math

def weights():
	connect = sql.connect('cntrl/weights.db')
	cursor  = connect.cursor()
	#print "asda"
	content =[]
	lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	k=0
	while k<26:
		st = "F:/Inforet/final_stuff/idf/idf/IDFTFmts"+lst[k]+".txt"
		f1 = open(st,'r')
		print "doing it----------"
		print k
		idf= f1.readlines()

		#print tf
		i=0
		j=0
		N = 103637
		final=[]
		# print len(tf)
		# print len(idf)
		while i<len(idf): 
			temp = idf[i].split()
			temp[1] = (float(math.log10(float(N)/float(temp[1]))))	
			element = str(temp[0] +' '+ str(temp[1]))
			final.append(element)
			i+=1

		# print final[0]
		it = 0
		while it<len(final):
			half = final[it].split()
			temp = "idf_"+lst[k]
			cursor.execute("insert into `"+temp+"` (`name`, `idf`) values ( '" + half[0] + "'," + half[1] + " ) ")
			it+=1
		k+=1
		connect.commit()

weights()