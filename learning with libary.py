#Importing face detection libraries
from sklearn import tree
import os

#input = Distances of samples
#output = Feeling of sampels
input = []
output = []

#Reading feeling from feeling(i).txt
for i in range(202):
    with open("./feeling/feeling{}.txt".format(i) , 'r') as feeling:
        data = feeling.read()
        output.append(data)

#Reading distance from fasele(i).txt
for i in range(202):
    with open("./fasele/fasele{}.txt".format(i) , 'r') as fasele:
        data = fasele.readlines()
        fasele_tasvir = []
        for line in data:
            a = list(line.split("\n"))
            del a[-1]
            fasele_tasvir.append(a[0])
        input.append(fasele_tasvir)

#Defining clf as decision tree
clf = tree.DecisionTreeClassifier()

#Build a decision tree classifier from the training set (x, y)
clf = clf.fit(input,output)

new_data = []
with open("result.txt" , 'r') as result:
    data = result.readlines()
    result = []
    for line in data:
        a = list(line.split("\n"))
        del a[-1]
        result.append(a[0])
    new_data.append(result)

#Predict class or regression value for x
answer = clf.predict(new_data)
print(answer[0])

#try:
#    os.remove("./data.txt")
#    os.remove("./points.txt")
#    os.remove("./result.txt")
#except:
#    pass