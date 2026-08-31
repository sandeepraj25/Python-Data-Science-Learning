# List - Mutable
marks = [98,99,45,12,63]
print(marks,type(marks))

#Length
print(len(marks))

#Index
print(marks[2])
print(marks[-1]) # Last Number Print ho jayega

# Slicing in List
print(marks[0:3])
print(marks[-3:]) # Last reverse me access karega

marks.append(20) # Last me add ho jayega
marks.insert(1,50) # Insert at specific Index
print(marks)

print(97 in marks) # Check exist or not in array

marks.clear() # Clear Entire Array elements