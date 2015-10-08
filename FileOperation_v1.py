__author__="Fei Hou"

#Read file
def readFile(path):
    try:
        fileOpen=open(path)
    except:
        print ('File could not be opened:',path)
        exit()
    return fileOpen

#Print each line
def generateLine(fopen):
    for line in fopen:
        yield line

#Split each word
def splitLine(lines):
    lines=lines.rstrip()
    words=lines.split()
    return words

__author__="Limaye Siddharth"

import sys
import re
from datetime import datetime

# Read Person Information
def readPersonInformation(gedData):
    try:        
        indiInformation = re.findall(r'0 @I.*?1 FAM[A-Z] @F',gedData,re.S|re.I)
    except:
        print 'Cannot read Person Information'
        exit()
    return indiInformation

__author__="Limaye Siddharth"

# Check DataType :: make generic
def checkDataType(temp):
    try:
        if isinstance(temp , types.StringType):
            return;
    except:
        print 'Data Type Mismatch'
        exit()
        
__author__="Limaye Siddharth"            
# Get Index position of input string,
# slice list and get the desired sliced list
def getSlicedList(lst,targetTAG,start,stop):
    try:
        # check data type        
        tagIndex = tempList.index(str(targetTAG))
        slicedList = tempList[tagIndex+int(start):tagIndex+int(stop)]        
    except:
        print 'ERROR:'
    return slicedList


__author__="Limaye Siddharth"
#Compare Dates
def compareDates(date1,date2):
    dic={'JAN':12,'FEB':11,'MAR':10,'APR':9,'MAY':8,'JUN':7,\
	'JUL':6,'AUG':5,'SEP':4,'OCT':3,'NOV':2,'DEC':1}
    d1 = int(date1[0])
    d2 = int(date2[0])
    m1= dic.get(date1[1])
    m2= dic.get(date2[1])
    y1 = int(date1[2])
    y2 = int(date1[2])
    try:
        if datetime(y1,m1,d1) < datetime(y2,m2,d2):
            return 'Date1 is less than Date2'
            #return 'Date1 is less than Date2'
        if datetime(y1,m1,d1) == datetime(y2,m2,d2):
            print 'Dates are Equal'
        if datetime(y1,m1,d1) > datetime(y2,m2,d2):
            print 'Date1 is greater than Date2'
    except:
        print 'ERROR:Dates cannot be compared'
        exit()
        return True
        


    

