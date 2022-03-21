import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0)
y = y/100


def sigmoid (x):
    return 1/(1 + np.exp(-x))


def dersig(x):
    return x * (1 - x)


e=7000
lr=0.1 
iln = 2 
hln = 3
oln = 1 

wh=np.random.uniform(size=(iln,hln))
bh=np.random.uniform(size=(1,hln))
wout=np.random.uniform(size=(hln,oln))
bout=np.random.uniform(size=(1,oln))

for i in range(e):
    h1=np.dot(X,wh)
    h=h1 + bh
    hla = sigmoid(h)
    oi1=np.dot(hla,wout)
    oi= oi1+ bout
    op = sigmoid(oi)
    
    EO = y-op
    og = dersig(op)
    dop = EO* og
    EH = dop.dot(wout.T)
    hg = dersig(hla)
    dhl = EH * hg
    wout += hla.T.dot(dop) *lr
    wh += X.T.dot(dhl) *lr
print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" ,op)
