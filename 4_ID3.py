import csv 
import pprint 
from math import * 
lines= list(csv.reader(open('4train.csv', 'r'))) 

data= lines.pop(0) 
print(data) 
print() 
print(lines) 

def entropy(pos, neg): 
    if pos==0 or neg==0: 
        return 0 
    tot= pos+ neg 
    return -pos/tot* log(pos/tot,2)-neg/tot*log(neg/tot,2) 
 
def gain(lines, attr, pos, neg): 
    d,E,acu= {}, entropy(pos,neg), 0 
    for i in lines: 
        if i[attr] not in d: 
            d[i[attr]]={} 
        d[i[attr]][i[-1]]= 1+d[i[attr]].get(i[-1],0) 
    for i in d: 
        tot= d[i].get('yes',0)+d[i].get('no',0) 
        acu+= tot/(pos+neg)*entropy(d[i].get('yes',0),d[i].get('no',0)) 
    return E-acu 

def build(lines, data): 
    pos= len([x for x in lines if x[-1]=='yes']) 
    sz= len(lines[0])-1 
    neg= len(lines)- pos 
    if neg==0 or pos==0: 
        return 'yes' if neg==0 else 'no' 
    root= max([[gain(lines,i,pos,neg),i] for i in range(sz)])[1] 
    fin, res= {},{} 
    uniq_attr= set([x[root] for x in lines]) 
    print(">>>", uniq_attr) 
    for i in uniq_attr: 
        res[i]= build([x[:root]+x[root+1:] for x in lines if x[root]==i], data[:root]+data[root+1:]) 
    fin[data[root]]=res 
    return fin 

tree= build(lines,data) 
pprint.pprint(tree) 
 
def classify(instance, tree, default= None): 
    attribute= next(iter(tree)) 
    if instance[attribute] in tree[attribute].keys(): 
        result= tree[attribute][instance[attribute]] 
        if isinstance(result, dict): 
            return classify(instance, result) 
        else: 
            return result 
    else: 
        return default 

import pandas as pd 

df_new= pd.read_csv('4test.csv') 
df_new['predicted']= df_new.apply(classify, axis=1, args=(tree,'?')) 
print(df_new) 
