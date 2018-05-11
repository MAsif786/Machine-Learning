# Class 1 - Hello World to Machine Learning
This is Class-1 Code. Hello World to **Machine-Learning**. In this class we write simple code and Using of Decision Tree Classifier. It contain 2 following codes.

* Hello-World
* Iris Flower Data

***

## Hello-World
In this code we treated our Decision Tree as a blackbox. Six lines of Python is all it takes to write our first machine learning program! In this code, I'll briefly introduce how to cede for writing program.

## Iris Flower Data

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.

In this program we are importing Iris data-set and make prediction on training data.

***

## Code
In both codes I use **Sklearn** Library.

`from sklearn import tree`

Then we declear our Decision Tree Classifier

`clf = tree.DecisionTreeClassifier()`

Train Data code

`clf = clf.fit(features,labels)`

Following code is used to pridict 

`result = clf.predict([[],[],[]])`