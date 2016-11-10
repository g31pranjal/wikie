
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import *


print 'accessing and stemming '+sys.argv[1]


with open('./temp/tf/'+sys.argv[1], 'r') as fin:
	contents = fin.readlines()
	word_list =[]
	ps = PorterStemmer()	
	with open('./temp/stemmed/m'+sys.argv[1],'w+') as fout:
		stop_words = set(stopwords.words("english"))

		for i in range(len(contents)-1):
			clear = contents[i].strip('1,2,3,4,5,6,7,8,9,0, ,\n')
			word_list.append(clear)
			cleaned_text = filter(lambda x: x not in stop_words, word_list)
			
			if cleaned_text !=[]:
				

				try:	
					final = [ps.stem(plural) for plural in cleaned_text]
					tokens = contents[i].split()
					temp = str(final[0] + ' ' + tokens[1] )

					fout.write("%s\n"%temp)					
					#print(temp)
				except Exception, e:
					pass				
				#fout.write("%s\n"%temp)
				final[:] = []
				cleaned_text[:] = []		

				word_list[:] = []

	fout.close()
fin.close()
			



