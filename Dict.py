# Dictonary:- its is Mutable. its store in {keys: value}

marks= {"English":99, "Hindi":98, "Physics":99, "Biology":98}
print(marks,type(marks))

marks["English"] = 95
print(marks["Physics"])
print(marks["English"])

for key in marks:
 print(key,marks[key])