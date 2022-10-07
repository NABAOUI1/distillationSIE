import numpy as np

Z1=0.1
Z2=0.2
Z3=0.3
Z4=0.4
k1=4.2
k2=1.75
k3=0.74
k4=0.34
Tf=200
Pf=100
F=100
Qsi=0.1
Epsilon=0.001
def RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    r=(((Z1*(1-k1))/(1+Qsi*(k1-1)))+((Z2*(1-k2))/(1+Qsi*(k2-1)))+((Z3*(1-k3))/(1+Qsi*(k3-1)))+((Z4*(1-k4))/(1+Qsi*(k4-1))))
    return r
def RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    r1=(Z1*(1-k1)**2)/((1+Qsi*(k1-1)**2))+((Z2*(1-k2)**2)/((1+Qsi*(k2-1))**2))+((Z3*(1-k3)**2)/((1+Qsi*(k3-1))**2))+((Z4*(1-k4)**2)/((1+Qsi*(k4-1))**2))
    return r1
OF=RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4)
while abs(OF) >= Epsilon:
    Qsi1=Qsi-(OF/RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4))
    print(abs(OF), Qsi1)
    Qsi=Qsi1
    Epsilon=Epsilon+0.001





    # OF="RR"((Z1,Z2,Z3,Z4,k1,k2,k3,k4))

#
# print(abs(RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4)))
