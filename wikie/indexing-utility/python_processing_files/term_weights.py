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
		st = "F:/Inforet/final_stuff/tf/tf/TFmts"+lst[k]+".txt"
		st1 = "F:/Inforet/final_stuff/idf/idf/IDFTFmts"+lst[k]+".txt"
		f = open(st,'r')
		f1 = open(st1,'r')
		
		tf = f.readlines()
		idf= f1.readlines()

		#print tf
		i=0
		j=0
		N = 103637.00
		final=[]
		# print len(tf)
		# print len(idf)
		while i<len(idf) : 
			# pass
			temp = idf[i].split()
			temp[1] = (float(math.log10(float(N)/float(temp[1]))))	
			xyz = tf[j].split()
			while j<len(tf) and temp[0] == xyz[0]:	
				xyz[2] = float(1+float(math.log10(int(xyz[2]))))
				value = float(xyz[2]*temp[1])
				# neel[0] = xyz[0]
				# neel[1] = xyz[1]
				# neel[2]=  value
				element = str(xyz[0] + ' ' + xyz[1] + ' ' + str(value))
				j+=1
				#print j
				if(j is not len(tf)):
					if j >= len(tf) :
						print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ index out of bound '+str(j)
						continue
					xyz = tf[j].split()
				# print (xyz)
				#print element
				final.append(element)
			i+=1
			
		#print(final)
		lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

		i = 65
		it = 0
		while it<len(final):
			half = final[it].split()
			temp = str("tf-idf_"+lst[k])
			cursor.execute("insert into `"+temp+"` (`Name`, `Doc_id`, `tf-idf`) values ( '" + half[0] + "'," + half[1] + " , " + half[2] + " ) ")
			# cursor.execute("insert into `idf` (`Name`, `idf`) values ( '" + half[0] + "'," + temp[1] + " ) ")
			it+=1

		connect.commit()
		k+=1

weights()