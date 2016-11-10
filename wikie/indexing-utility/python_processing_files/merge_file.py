from os import listdir
from os.path import isfile, join
filenames = [f for f in listdir('A/') if isfile(join('A/', f))]
print filenames
# Enter the filenames here 
#sfilenames = ['file1.txt', 'file2.txt']
with open('A/output.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

# changing the content of the files to the list 
content =[]
res = 0
f = open('output.txt','r')
content = f.readlines()

#content.remove('\n')
#print content
#print len(content)
i=0
with open('final.txt', 'w') as f1:
	while i < (len(content)):
		temp1 = content[i].split()
		if i is not len(content)-1:
			temp2 = content[i+1].split();
		res = int(temp1[2])
		if i is not len(content)-1:
			if temp1[0] == temp2[0] and temp1[1] == temp2[1] :
				while temp1[0] == temp2[0] and temp1[1] == temp2[1]:
					res = res+int(temp2[2])
					i+=1						
					#print i
					#print temp1
					#print temp2 
					temp2 = content[i+1].split()
				
				temp = str(temp1[0] + ' ' + temp1[1] + ' ' + str(res) )
				f1.write("%s\n"%temp)
				i+=1
			
			else:
				#print i
				#print temp1
				#print temp2
				if i is len(content) - 2: 
					temp = str(temp2[0] + ' ' + temp2[1] + ' ' + temp2[2] )
					f1.write("%s\n"%temp)
					i+=1;
				else:
					temp = str(temp1[0] + ' ' + temp1[1] + ' ' + temp1[2] )
					f1.write("%s\n"%temp)
					i+=1;
		else:
			#print i
			#print temp1
			#print temp2
			temp = str(temp1[0] + ' ' + temp1[1] + ' ' + temp1[2] )
			f1.write("%s\n"%temp)
			i+=1		
