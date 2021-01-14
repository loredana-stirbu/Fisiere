with open('input.txt','r') as f:
    s=f.readline()
n=0
d=0
b=0
c=0    
for litere in s:
    if litere.isupper():
        n+=1
with open('litereA.txt','w') as f:
    f.write(str(n))    
for lit in s:
    if lit.islower():
        d+=1   
with open('litereB.txt','w') as f:
    f.write(str(d))           
for a in s:
    if ord(a) in range(48,58):
        c+=1 
with open('operatori.txt','w') as f:
    f.write(str(c)) 
for i in s:
    if ((ord(i) in range (32,48)) or (ord(i) in range(58,65)) or (ord(i) in range (91,9)) or (ord(i) in range (123,127))):
        b+=1         
with open('cifre.txt','w') as f:
    f.write(str(b))      

  


