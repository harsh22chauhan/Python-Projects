
n=(11,12,14,18,22,13,21,54,55)
odd=0
even=0

for i in n:
   if i%2==0:
      odd=odd+1
   else:
      even=even+1
   

print("even=" ,even)
print("odd=",odd)

#input list

list=[]
number = int(input("how many value you want in a list: "))
for i in range(0,number):
   numbers = int(input("enter your choice number:"))
   list.append(numbers)
 
print(list)
