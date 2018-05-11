#Importing Tree from SK-Learn 
from sklearn import tree

#Sample DATA
#######################################################
# features: [WEIGHT_OF_OBJECT, OBJECT_SURFACE TYPE]
# labels: two types of object 
#######################################################
features = [[140,0],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]

# Train Classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

# Predict Result for WEIGHT_OF_OBJECT: 150 and OBJECT_SURFACE TYPE: 0
result = clf.predict([[150,0]])

print(result)
