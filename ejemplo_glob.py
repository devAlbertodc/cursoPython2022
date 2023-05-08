import glob
import fnmatch
import os

for fichero in glob.glob("../*/*.py"):
    pass
    #print(fichero)

patron = 'ej*.py'
print(patron)

fichero = os.listdir('./')
for i in fichero:
    print(i, fnmatch.fnmatch(i,patron))