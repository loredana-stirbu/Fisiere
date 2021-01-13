with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=int(a)*2
    y=int(b)*3
if int(b)>int(a):
    x=int(a)*3
    y=int(b)*2
if int(a)==int(b):
    x=y='Numere egale'
with open('produs.txt','w') as f:
    f.write(str(x))        
    f.write('\n')   
    f.write(str(y))  