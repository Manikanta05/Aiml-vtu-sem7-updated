import csv, numpy as np

list=np.array(list(csv.reader(open("3.csv","r"))))

concept = np.array(list[:,:-1])
target = np.array(list[:,-1])

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
                
indices=[i for i,val in enumerate(generic) if val == ['?','?','?','?','?','?']]
for i in indices:
    generic.remove(['?','?','?','?','?','?'])
print("Most General = {}".format( generic))
print("Most Specific = {}".format(specific))
