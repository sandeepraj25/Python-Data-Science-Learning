# string in python

# string is immutable so original value can't be change;

name = "Tony Stark"
grade = 'B'

# string opertaions
print(name.upper())
print(name.lower())
print(name)

# Find 
print(name.find("ark")) # return index +> position - 7
print(name.find("S")) # 5
print(name.find('T')) # 0

# Replace
print(name.replace("Tony Stark","Sandeep Raj"))
print(name)
print(name.replace("Stark","Raj"))
print(name.replace("T","S"))

# Check For Presence
print('T' in name) # True
print('X' in name) # False
