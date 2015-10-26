___author___= 'Yaw Adu-Boahene Jr.'



fhand = open ('/Users/darth_yaw/Documents/UseCases/Alexander-Graham-Bell-5-Oct-2015.ged','r')    #accesses file and opens to read
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
pos2= None		
for line1 in x [21:23]:
	if '2 DATE' in line1:
		pos2= line1.find('E')
		hos2= line1[pos2+1:17]
		print 'He died on:', hos2


hos3= None
pos3=None	
hos4= None
pos4= None	
for line2 in x [46:48]:
	if '2 GIVN' in line2:
		pos3 = line2.find('N')
		hos3= line2[pos3+1:13]
	elif '2 SURN' in line2:
		pos4= line2.find ('N')
		hos4= line2[pos4+1:11]
		print 'Name of person is:', hos3+hos4
		
hos5= None
pos5= None		
for line3 in x [52:54]:
	if '2 DATE' in line3:
		pos5= line3.find('E')
		hos5= line3[pos5+1:18]
		print 'He died on:', hos5
		

hos6= None
pos6=None	
hos7= None
pos7= None	
for line4 in x [58:60]:
	if '2 GIVN' in line4:
		pos6 = line4.find('N')
		hos6= line4[pos6+1:11]
	elif '2 SURN' in line4:
		pos7= line4.find ('N')
		hos7= line4[pos7+1:11]
		print 'Name of person is:', hos6+hos7
		
hos8= None
pos8= None		
for line5 in x [64:66]:
	if '2 DATE' in line5:
		pos8= line5.find('E')
		hos8= line5[pos8+1:18]
		print 'She died on:', hos8
		
