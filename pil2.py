#Python script that uses PIL to convert every file in a directory to .jpg format,
#rotate them and resize to 128*128.
import os
import sys
from PIL import Image

path = input("Enter directory path:")
opath = input("Enter the directory to save files:")
files = os.listdir(path)
for fil in files:
    f , e = os.path.splitext(fil) #separate file name from extension
    new = f + '.jpg'
    new = os.path.join(opath,new)
    old = os.path.join(path,fil)
    try:
        oldim = Image.open(old)
        newim = oldim.rotate(-90).convert("RGB").resize((128,128))
        newim.save(new)
        oldim.close()
    except:
        print("Cannot convert file: ",f)
        
        

