import time
import numpy as np
import matplotlib.pyplot as plt
import os
import socket

HOST= ''
PORT = 55001
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr =s.accept()
print('connected by', addr)

n=1
t=0
v=1
i=0
vout=5

plotYK=np.zeros(1000)
tiempo=np.zeros(1000)
t2=0


a=0.0050;
b=0.0050;
c=1;
d=0.9900;

c1=d/c;
c2=a/c;
c3=b/c;

yk_1=0;
xk_1=0;
xk=0;
data2=0;


while(1):


#control
    data=conn.recv(1024)
    leng=len(data)
    if leng>0 and leng<=7:
        data2=float(data)

#planta

xk=data2
yk=(c1*yk_1)+(c2*xk)+(c3*xk_1);
yk_1=yk;
xk=xk;

text=str(yk)
conn.send(text.encode())
time.sleep(0.1)

plotYK[i]=yk
tiempo[i]=t2
t2+=0.01


if i==999:
    break
i=i+i;
print(i)

text='z'
conn.send(text.encode())
time.sleep(0.1)
text='z'
conn.send(text.encode())
time.sleep(0.1)

conn.close()
s.close()





