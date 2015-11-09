___author___= 'Yaw Adu-Boahene Jr.'



fhand = open ('/Users/darth_yaw/Documents/UseCases/Alexander-Graham-Bell-27-Oct-2015.ged','r')    #accesses file and opens to read
x= fhand.readlines() #reads file as list
fhand.close () 


hos= None
pos=None	
hos1= None
pos1= None	

for line in x [37:39]:
	if '2 GIVN' in line:
		pos = line.find('N')
		hos= line[pos+1:16]
	elif '2 SURN' in line:
		pos1= line.find ('N')
		hos1= line[pos1+1:14]
		print 'Name of person is:', hos+hos1

hos2= None
pos2= None		
for line1 in x [41:44]:
	if '2 DATE' in line1:
		pos2= line1.find('E')
		hos2= line1[pos2+7:17]
		print 'Age is:', 2015 - int(hos2)
		print x[44]
		
		
hos3= None
pos3=None	
hos4= None
pos4= None	

for line in x [47:49]:
	if '2 GIVN' in line:
		pos3= line.find('N')
		hos3= line[pos3+1:13]
	elif '2 SURN' in line:
		pos4= line.find ('N')
		hos4= line[pos4+1:11]
		print 'Name of person is:', hos3+hos4

hos5= None
pos5= None		
for line1 in x [51:53]:
	if '2 DATE' in line1:
		pos5= line1.find('E')
		hos5= line1[pos5+8:18]
		print 'Age is:', 2015 - int(hos5)
		print x[56]
		
		

hos6= None
pos6=None	
hos7= None
pos7= None	

for line in x [79:81]:
	if '2 GIVN' in line:
		pos6= line.find('N')
		hos6= line[pos6+1:10]
	elif '2 SURN' in line:
		pos7= line.find ('N')
		hos7= line[pos7+1:13]
		print 'Name of person is:', hos6+hos7

hos8= None
pos8= None		
for line1 in x [83:85]:
	if '2 DATE' in line1:
		pos8= line1.find('E')
		hos8= line1[pos8+7:17]
		print 'Age is:', 2015 - int(hos8)
		print x[86]
		
hos9= None
pos9=None	
hos10= None
pos10= None	

for line in x [107:109]:
	if '2 GIVN' in line:
		pos9= line.find('N')
		hos9= line[pos9+1:10]
	elif '2 SURN' in line:
		pos10= line.find ('N')
		hos10= line[pos10+1:13]
		print 'Name of person is:', hos9+hos10

hos11= None
pos11= None		
for line1 in x [111:113]:
	if '2 DATE' in line1:
		pos11= line1.find('E')
		hos11= line1[pos11+8:18]
		print 'Age is:', 2015 - int(hos11)
		print x[114]
	
hos12=None
pos12=None	
hos13=None
pos13=None	

for line in x [89:91]:
	if '2 GIVN' in line:
		pos12= line.find('N')
		hos12= line[pos12+1:11]
	elif '2 SURN' in line:
		pos13= line.find ('N')
		hos13= line[pos10+1:11]
		print 'Name of person is:', hos12+hos13

hos14= None
pos14= None		
for line1 in x [93:95]:
	if '2 DATE' in line1:
		pos14= line1.find('E')
		hos14= line1[pos14+8:18]
		print 'Age is:', 2015 - int(hos14)
		print x[95]
		
hos15=None
pos15=None	
hos16=None
pos16=None	

for line in x [98:100]:
	if '2 GIVN' in line:
		pos15= line.find('N')
		hos15= line[pos15+1:12]
	elif '2 SURN' in line:
		pos16= line.find ('N')
		hos16= line[pos16+1:11]
		print 'Name of person is:', hos15+hos16

hos17= None
pos17= None		
for line1 in x [102:104]:
	if '2 DATE' in line1:
		pos17= line1.find('E')
		hos17= line1[pos17+8:18]
		print 'Age is:', 2015 - int(hos17)
		print x[104]
