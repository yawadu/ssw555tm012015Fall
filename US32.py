___author___= 'Yaw Adu-Boahene Jr.'



fhand = open ('/Users/darth_yaw/Documents/UseCases/Alexander-Graham-Bell-16-Nov-2015.ged','r')    #accesses file and opens to read
x= fhand.readlines() #reads file as list
fhand.close () 

hos= None
pos=None	
hos1= None
pos1= None	

for line in x [15:17]:
	if '2 GIVN' in line:
		pos = line.find('N')
		hos= line[pos+1:16]
	elif '2 SURN' in line:
		pos1= line.find ('N')
		hos1= line[pos1+1:11]
		print 'Name of person is:', hos+hos1

hos2= None
pos2=None		
for line1 in x [19:21]:
	if '2 DATE' in line1:
		pos2 = line1.find('E')
		hos2= line1[pos2+1:17]
		print 'Was born on:', hos2
		

hos3= None
pos3=None	
hos4= None
pos4= None	

for line in x [140:142]:
	if '2 GIVN' in line:
		pos3= line.find('N')
		hos3= line[pos3+1:14]
	elif '2 SURN' in line:
		pos4= line.find ('N')
		hos4= line[pos4+1:11]
		print 'Name of person is:', hos3+hos4
		
		
hos5= None
pos5=None		
for line1 in x [144:146]:
	if '2 DATE' in line1:
		pos5 = line1.find('E')
		hos5= line1[pos5+1:17]
		print 'Was born on:', hos5
		print 'They were both born on the same day'
		
