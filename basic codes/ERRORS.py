#ZeroDivisionError
#KeyboardInterruptError
#IOError
#ImportError
#ValueError

try:
    x=int(input("Enter First Number"))
    #y=int(input("Enter Zero Number"))
    #print("sum is:", x+y)
    #print("answer is:",x/y)

except  ZeroDivisionError as e:

        print("oops!!you are dividing by zero")




