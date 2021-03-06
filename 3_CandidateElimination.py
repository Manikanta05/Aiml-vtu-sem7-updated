import csv, numpy as np,copy

data=np.array(list(csv.reader(open("3.csv","r"))))

concept = np.array(data[:,:-1])
target = np.array(data[:,-1])

for i in range(len(target)):
    if(target[i] == "Y"):
        specific = concept[i]
        break

generic = [["?" for i in range(len(specific))] for i in range(len(specific))]

for i in range(len(target)):
    if(target[i] == "Y"):
        for j in range(len(specific)):
            if(specific[j] != concept[i][j]):
                specific[j] = "?"
                generic[j][j] = "?"

    else:
        for j in range(len(specific)):
            if specific[j] != concept[i][j]:
                generic[j][j] = specific[j]
            else:
                generic[j][j] = "?"
    str=copy.copy(generic)
    indices1=[i for i,val in enumerate(str) if val == ['?','?','?','?','?','?']]
    for j in indices1:
        str.remove(['?','?','?','?','?','?'])
    print("G{} = {}".format(i, str))
    print("S{} = {}".format(i, specific))

print("Final G  = {}".format(str))
print("Final S = {}".format(specific))
