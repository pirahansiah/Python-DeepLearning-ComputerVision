import csv
import numpy as np
from shutil import copyfile
newList = list()
with open('file.csv', 'r') as f:
	reader = csv.reader(f, dialect='excel', delimiter=',')
	newList= f.readlines();		
	for i in newList:
		strfilesrc=' put source folder '
		strfiledst=' set distance folder'	
		stra=i
   		strb=stra.split(',')		
		checkIf= int(strb[1]) # which column need to check  		
		if(checkIf==1):		
			print strb[0] # file name 
			strfilesrc+=strb[0]
			strfiledst+=strb[0]
			copyfile(strfilesrc, strfiledst)
