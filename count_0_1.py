n=input()
count0=0
count1=0
for i in n:
    if i=='0':
        count0=count0+1
for x in n:
    if x=='1':
        count1=count1+1
print("no of 0's in a string are :"+ str(count0))
print("no of 1's in a string are :"+ str(count1))
