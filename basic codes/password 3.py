pwd=input('enter')
d=a=u=s=l=sp=0
w="@#$%^&*"
for c in pwd:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        a=a+1
        if c.isupper():
           u=u+1
        elif c.islower():
           l=l+1    
    elif c in w:
        s=s+1
    elif c.isspace():
        sp=sp+1    
    else:
        pass
if d==0:
    print("invalid password no digits")
if sp>0:
    print("Invalid space not allowed")
elif a==0:
    print("INVALID ENTER SOME LETTERS")
elif u==0:
    print("INVALID ENTER one in uppercase")
elif l==0:
    print("INVALID ENTER one in lowercase")
elif s==0:
    print("INVALID enter special character")
elif len(pwd)<10:
    print("INVALID MINIMUM LENGTH SHOULD BE 9")
else:
    print("Valid pasword")
