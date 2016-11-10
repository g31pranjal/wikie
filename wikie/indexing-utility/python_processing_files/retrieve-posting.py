

def posting(word):

	a = word[0]
	# print a
	a = a.upper()
	st = "F:/Inforet/final_stuff/posting/posting/TFmts"+a+".txt"
	# print string
	f = open(st,'r')

	post = []
	post = f.readlines()	
	i=0
	j=0
	list = []
	while i <len(post):
		temp = post[i].split()
		if temp[0] == word:
			# print "gotcha "
			temp1 = temp[1].split(",")
			# print temp1
			while j<len(temp1)-1:
				list.append(temp1[j])
				j+=1

			# print "------------------------------"
			# print list
		i+=1

	return list
