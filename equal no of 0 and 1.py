n=input()
count0=0
count1=0
for i in n:
    if i=='0':
        count0=count0+1
for x in n:
    if x=='1':
        count1=count1+1
if(count0==count1):
    print("There are equal no of 0's and 1's.")
else:
    print("There are unequal no of 0's and 1's.")
