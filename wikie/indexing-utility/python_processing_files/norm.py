import sqlite3 as sql
from os import listdir
from os.path import isfile, join
import math

def weights():
	connect = sql.connect('cntrl/weights.db')
	cursor  = connect.cursor()
	
	st = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	doc_tf = []
	i=1
	j=0
	lst = [0]*106000
	while j<26:
		print "Entering loop----------------------------> "
		print j
		temp = str("tf-idf_"+st[j])
		#print temp
		cursor.execute("SELECT `Doc_id`,`tf-idf` from '"+temp+"' ")
		# cursor.exe
		# change value of tf_idf to tf in the above table
		r= cursor.fetchone()
		print r[0]
		# print r 
		# tf_sqr = 0
		while r is not None:
			lst[r[0]] += r[1]*r[1]
			# print r[0]
			r= cursor.fetchone()
		# doc_total = doc_total + tf_sqr
		# print(doc_total)	
		j+=1

	i=0
	while i<106000:
		if lst[i] is not 0 :
			lst[i] = math.sqrt(lst[i])
			cursor.execute("insert into `wts` (`doc_id`, `mod`) values ( " + str(i) + "," + str(lst[i]) + " ) ")
		i+=1
	# tf_final = math.sqrt(doc_total)
	# print (tf_final)
	# doc_tf.append(tf_final)
	print lst[1]
	connect.commit()

weights()