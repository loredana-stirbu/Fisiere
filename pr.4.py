with open('input.txt','r') as f:
    x=f.readline()
    a=int(x)-2
    b=int(x)-1
    c=int(x)+1
    d=int(x)+2
with open('output.txt','w') as f:
    s=f.write(str(int(a))+" "+str(int(b))+" "+ x +" "+str(int(c))+" "+str(int(d)))