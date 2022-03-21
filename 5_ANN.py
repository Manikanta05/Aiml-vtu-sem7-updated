import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0)
y = y/100

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def dersig(x):
    return x * (1 - x)

e,lr,iln,hln,oln=7000,0.1,2,3,1

wh=np.random.uniform(size=(iln,hln))
bh=np.random.uniform(size=(1,hln))
wout=np.random.uniform(size=(hln,oln))
bout=np.random.uniform(size=(1,oln))

for i in range(e):
    hla = sigmoid(np.dot(X,wh)+bh)
    op = sigmoid(np.dot(hla,wout)+bout)
    
    dop = (y-op)*dersig(op)
    dhl = dop.dot(wout.T) * dersig(hla)
    wout += hla.T.dot(dop) *lr
    wh += X.T.dot(dhl) *lr
print("Input: \n",str(X))
print("Actual Output: \n",str(y))
print("Predicted Output: \n" ,op)
