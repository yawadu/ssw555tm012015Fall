___author___= 'Yaw Adu-Boahene Jr.'



fhand = open ('/Users/darth_yaw/Documents/UseCases/Alexander-Graham-Bell-5-Oct-2015.ged','r')    #accesses file and opens to read
x= fhand.readlines() #reads file as list
fhand.close () 
		
hos= None
pos=None	
hos1= None
pos1= None	
for line in x [28:30]:
	if '2 GIVN' in line:
		pos = line.find('N')
		hos= line[pos+1:12]
	elif '2 SURN' in line:
		pos1= line.find ('N')
		hos1= line[pos1+1:14]
		print 'Name of person is:', hos+hos1




hos2= None
pos2= None		
for line1 in x [72:74]:
	if '2 DATE' in line1:
		pos2= line1.find('E')
		hos2= line1[pos2+1:18]
		print 'She got married on:', hos2
