print("Lets Study LOOPS")   
print("for loop::")
for x in range(6):
    print(x)
for x in range (4,8):
    print(x)
print("Following prints even numbers")
for x in range(20,30,2): 
    print(x)
    
print("While loop::")
count = 0
while count < 4:
    print(count)
    count += 1
print("Break & Continue ::")

while True:
    print(count)
    count +=1
    if count >=4:
       break
for x in range(10):
        if x%2 == 0:
           continue
        print(x)
