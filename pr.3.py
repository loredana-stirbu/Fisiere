with open('globulet.txt','r') as f:
    b=f.readline()
a = int(b) + 3 
c = int(a) + b - 2 
t = int(a) + int(b) + int(c)
    
with open('bradut.txt','w') as f:
    f.write(str(t))