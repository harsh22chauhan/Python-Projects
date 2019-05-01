print("Pattern 1")
for i in range(0,10,1):
    for j in range(i):
        print("*",end="")

    print('')
print("Pattern 2:\n")
for k in range(8,2,-1):
    for l in range(1,k):
        print(l,end="")

    print('')
