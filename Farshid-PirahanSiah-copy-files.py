import csv
import os
import numpy as np
from shutil import copyfile
newList = list()
x = os.listdir('path main folder')
i=0
for files in x:
	strfilesrc='path main folder'
	strfiledst='files copy to'
	strfilesrc+=files
	strfiledst+=files
	if i< 'number of files you want to copy ':
		i=i+1
		copyfile(strfilesrc, strfiledst)
	else:
		break	

