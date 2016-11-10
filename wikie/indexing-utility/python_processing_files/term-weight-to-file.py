import sqlite3 as sql
import os
from os import listdir
from os.path import isfile, join
import math

def weights():
	connect = sql.connect('cntrl/weights.db')
	cursor  = connect.cursor()

	
	lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	k=0
	while k<26:
		st = "F:/Inforet/final_stuff/tf/value_"+lst[k]+".txt"
		fout = open(st,'w+')
		temp = str("tf-idf_"+lst[k])
		cursor.execute("SELECT * from '"+temp+"'")

		r = cursor.fetchone()
		while r is not None:
			val = str(r[0]+" "+str(r[1])+" "+str(r[2]))
			fout.write("%s\n"%val)
			r = cursor.fetchone()

		k+=1
	connect.commit
	
weights()	
