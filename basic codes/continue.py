a="This is Python class"
print(a)
for i in a:
    if i=="s"or i =="h":
       continue
    print(i)
print("This is for Break")       
for j in a:
    if j=="s"or j=="h":
       break
    print(j)
print("This is for Pass:")
for j in a:
    if j=="s"or j=="h":
       pass
    print(j)
