import sqlite3 as sql
from os import listdir
from os.path import isfile, join
import math

def map():
	connect = sql.connect('cntrl/map_name.db')
	cursor  = connect.cursor()
	f = open('F:/Inforet/FileMap.txt','r')

	i=0
	temp = f.readlines()
	while i<len(temp):
		final = temp[i].split()
		i+=1

		cursor.execute("insert into `map` (`id`, `docid`) values ( " + final[0] + ",'" + final[1][:-4] + "' ) ")

	connect.commit()
map()