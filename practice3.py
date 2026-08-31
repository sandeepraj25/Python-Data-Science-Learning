# Print All Odd Number from 1 to 20.
for i in range(1,21):
 if i%2 != 0:
    print(i)

# Print the Table of 57;
num = 57
for i in range(1,11):
  print(num*i)

# Print All Multiple of 3 From 1 to 50 But Skip 15

for i in range (1,51):
  if i % 3 ==0:
   if i==15:
    continue
   print(i)

# Take Input From a and b as Input. 
# Find and Print the First Number between 1 to 1000 that is divisible by both numbers

a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))

for i in range(1,1001):
 if i%a==0 and i%b==0:
   print(i)
   break