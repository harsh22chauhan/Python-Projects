#Code to generate & print dictonary
n=int(input("Input a number "))
d = {}
for x in range(1,n+1):
    d[x]=x*x #value is square of number
print(d) 
print("*"*20)
#merge two dict
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = d1.copy()
d.update(d2)
print(d)
print("*"*20)
#sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original  ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)
print("*"*20)
#add a key to a dictionary.
d = {0:10, 1:20,3:30}
print(d)
d.update({2:40})
print(d)
print("*"*20)
#Concatenate two dictinaries
dic1={'a':1, 'b':2}
dic2={'c':3, 'd':4}
dic3={'e':5,'f':6,'g':7}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
print("*"*20)
#Sum all values in a dict
my_d = {'d1':100,'d2':-4,'d3':12}
print( "sum=",sum(my_d.values()))
print("*"*20)
#iterate dictinary over loop
d = {'name' : 00, 'ash': 1, 'ashi': 2, 'sid': 3} 
for dict_key, dict_value in d.items():
    print(dict_key,':',dict_value)
print("*"*20)    
#Map two list into dictionaries
keys = ['red', 'green', 'blue']
values = [0,1,2]
d1 = dict(zip(keys, values))
print(d1)
print("*"*20)
