import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn import tree

# Q no. 1

iris_file = pd.read_csv('iris.csv', names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
print(iris_file)

# Q no. 2

print('How many data points are there in this data set?')
print(len(iris_file))
print()
print('What is the shape of the data?')
print(iris_file.shape)
print()
print("What are the data types of the columns?")
print(iris_file.dtypes)
print()
print("What are the column names?")
print(iris_file['class'].unique())
print(iris_file.columns)
print()
print("How many species of flower are included in the data?")
print(len(iris_file['class'].unique()))
print()
print("What are the first 10 rows of the data?")
print(iris_file[0:10])

# Q no. 3

var = iris_file.iloc[35, :]
var1 = iris_file.iloc[38, :]
print(var)
print()
print(var1)


# Q no. 4

iris_file_new = iris_file.copy()
iris_file_new['petal-ratio'] = iris_file['petal-length']/iris_file['petal-width']
iris_file_new['sepal-ratio'] = iris_file['sepal-length']/iris_file['sepal-width']

print(iris_file_new);

# Q no. 5

iris_file_new.to_csv('E:\AI Asignment 01\iris_corrected.csv')

# Q no. 6

agg = iris_file_new.groupby('class')[['petal-ratio', 'sepal-ratio']].aggregate(['mean', 'median', 'min', 'max', 'std'])
print(agg)

# Q no. 7

iris_file.hist()
plt.show()

x = iris_file_new[iris_file_new['class'] == 'Iris-setosa']['petal-width']
y = iris_file_new[iris_file_new['class'] == 'Iris-setosa']['petal-length']

a = iris_file_new[iris_file_new['class'] == 'Iris-versicolor']['petal-width']
b = iris_file_new[iris_file_new['class'] == 'Iris-versicolor']['petal-length']

i = iris_file_new[iris_file_new['class'] == 'Iris-virginica']['petal-width']
j = iris_file_new[iris_file_new['class'] == 'Iris-virginica']['petal-length']

plt.scatter(x, y, color='red')  # setosa
plt.scatter(a, b, color='green')  # versicolor
plt.scatter(i, j, color='blue')  # virginica
plt.show()

scatter_matrix(iris_file)
plt.show()

# Q no. 8

array = iris_file.values
X = array[:, 0:4]
y = array[:, 4]
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print(X_test);
print(Y_test)

# Q. no 9

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

tree.plot_tree(clf)
plt.show()
