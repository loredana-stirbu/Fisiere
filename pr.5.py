with open ('numere.txt','r') as f:
    a=f.read()
x1='1*'+str(a)+'='+str(int(a)*1)
x2='2*'+str(a)+'='+str(int(a)*2)
x3='3*'+str(a)+'='+str(int(a)*3)
x4='4*'+str(a)+'='+str(int(a)*4)
x5='5*'+str(a)+'='+str(int(a)*5)
x6='6*'+str(a)+'='+str(int(a)*6)
x7='7*'+str(a)+'='+str(int(a)*7)
x8='8*'+str(a)+'='+str(int(a)*8)
x9='9*'+str(a)+'='+str(int(a)*9)
x10='10*'+str(a)+'='+str(int(a)*10)
with open('inmultire.txt') as f:
    f.write(str(x1)+" "+str(x2)+" "+str(x3)+" "+str(x4)+" "+str(x5)+" "+str(x6)+" "+str(x7)+" "+str(x8)+" "+str(x9)+" "+str(x10))