import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()


clf = tree.DecisionTreeClassifier()
clf.fit(iris.data, iris.target)

print(clf.predict([[1.2,1.5,2.0,1.0]]))