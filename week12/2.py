from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = load_digits()

# print(digits.DESCR)

# print(digits.data.shape)

# print(digits.target.shape)

# print(digits.images[13])

x_train, x_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.2,random_state=1)

knn = KNeighborsClassifier()

knn.fit(x_train,y_train)

predicted = knn.predict(x_test)
expected = y_test

print(knn.score(x_test,y_test))


conf = confusion_matrix(y_true=expected,y_pred=predicted)

print(conf)