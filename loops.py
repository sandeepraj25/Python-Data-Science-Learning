# Range

nums = range(5)
print(nums)
# output = [1,2,3,4]

# Range 1 to 6
range(1,6) # output 1,2,3,4,5,6

range(start=0, stop = 6, step = 1)

# while Loop
i = 1
while i<=5:
    print(i)
    i+=1
print("Program is End Here: ")

# For Loops

# 0 to 4
for i in range(10):
  print(i)

# 1 to 5
for i in range(1,6):
  print(i)  

# Print 1 to 10 even number
for i in range(1,11):
   if i%2==0:
      print(i)

# Print 1 to 10 even number- Another way
for i in range(2,11,2):
   print(i)

# Break:- Stop
# Continue:- Skip

for i in (1,51):
   if(i==21):
     continue
    # Break
if(i%3==0):
  print(i)





