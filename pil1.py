#!/usr/bin/env python3
from PIL import Image

name = input("Enter image path:")
try:
    im = Image.open(name)
except:
    print("File not found/Invalid name.")
    exit()    
x = 0
while x != "5":
    x = input("1.Rotate, 2.Resize, 3.Show, 4.Save as, 5.Close:")
    if x == "1":
        r = int(input("Rotate by?(degree)"))
        im = im.rotate(r)
    elif x == "2":
        w = int(input("Enter the width:"))
        h = int(input("Enter the height:"))
        im = im.resize((w,h))
    elif x == "3":
        im.show()
    elif x == "4":
        new_name = input("Enter name/path to save:")
        if new_name == None: new_name = name
        im.save(new_name)
    elif x == "5": im.close()
    else:
        print("Invalid choice.")

