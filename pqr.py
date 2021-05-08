s = input('enter a string  :- ')
p =s.split()
print(p)
l=(len(p))-1
for i in p:
   str = i
   j = len(str)-1
   while(j>=0):
       print(str[j],end='')
       j=j-1
   print(end=' ')
print()
while(l>=0):
     print(p[l])
     l =l-1


   



         
    