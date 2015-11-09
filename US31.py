___author___= 'Yaw Adu-Boahene Jr.'



fhand = open ('/Users/darth_yaw/Documents/UseCases/Alexander-Graham-Bell-27-Oct-2015.ged','r')    #accesses file and opens to read
x= fhand.readlines() #reads file as list
fhand.close () 

hos= None
pos=None	
hos1= None
pos1= None	
for line in x [89:91]:
	if '2 GIVN' in line:
		pos = line.find('N')
		hos= line[pos+1:11]
	elif '2 SURN' in line:
		pos1= line.find ('N')
		hos1= line[pos1+1:11]
		print 'Name of single person is:', hos+hos1

hos2= None
pos2= None		
for line1 in x [93:95]:
	if '2 DATE' in line1:
		pos2= line1.find('E')
		hos2= line1[pos2+8:18]
		print 'Age is:', 2015 - int(hos2)
		

hos3= None
pos3=None	
hos4= None
pos4= None	
for line2 in x [98:100]:
	if '2 GIVN' in line2:
		pos3 = line2.find('N')
		hos3= line2[pos3+1:12]
	elif '2 SURN' in line2:
		pos4= line2.find ('N')
		hos4= line2[pos4+1:11]
		print 'Name of single person is:', hos3+hos4
		
hos5= None
pos5= None		
for line3 in x [102:104]:
	if '2 DATE' in line3:
		pos5= line3.find('E')
		hos5= line3[pos5+8:18]
		print 'Age is:', 2015 - int(hos5)
