
a = float(input("enter a number"))
b = float(input("enter a number"))
c = input("enter your choice A = sum,B= diff ,C = multiply, D = division, P = power ")

if c == "A" :
    print(a+b)
elif c == "B":
    print(a-b)
elif c == "C":
    print(a*b)
elif c == "D":
    print(a//b)
elif c == "P":
    d =int(input("enter your choice/n 1 for ato b ,"))
    if d == 1:
        print(a**b)
    else :
        print(b**a)
else :
    print("try again")
    c = input("enter your choice A = sum,B= diff ,C = multiply, D = division, P = power ")
    if c == "A" :
       print(a+b)
    elif c == "B":
       print(a-b)
    elif c == "C":
       print(a*b)
    elif c == "D":
       print(a//b)
    elif c == "P":
        d =int(input("enter your choice/n 1 for ato b ,"))
        if d == 1:
            print(a**b)
        else :
            print(b**a)
    else:
        print("no of attempt fail")

    
   
    



