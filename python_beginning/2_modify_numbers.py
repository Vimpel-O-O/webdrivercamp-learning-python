#!/usr/bin/python3
num = 3.141592653589793238
one = "'"
two = '"'

print('Learning Python is fun"%s - %.2f %s' % ("'", num, "%"))
print("Learning Python is fun{0}{2} - {1} %".format('"', format(num, ".2f") ,"'"))
print(f"Learning Python is fun{two}{one} - {num:.2f} %")
