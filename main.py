# Importing the libraries

import pandas as pd

# dataset imported

dataset = pd.read_csv('BankCustomers.csv')
X = dataset.iloc[:, 3:13]
y = dataset.iloc[:, 13]

# categorical feature into dummy variables

states = pd.get_dummies(X['Geography'], drop_first=True)
gender = pd.get_dummies(X['Gender'], drop_first=True)

# dropping the columns as it is not required now

X = X.drop(['Geography', 'Gender'], axis=1)

# merging the remaining dummies columns

X = pd.concat([X, states, gender], axis=1)

# Splitting the dataset into the Training and Test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Ann starting

from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

# Adding the input layer and the first hidden layer

classifier.add(Dense(activation="relu", input_dim=11, units=6, kernel_initializer="uniform"))

# Adding the second hidden layer

classifier.add(Dense(activation="relu", units=6, kernel_initializer="uniform"))

# Adding the output hidden layer

classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))

# Compile

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ANN to the Training set

classifier.fit(X_train, y_train, batch_size=10, epochs=100)

# Test set results

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Confusion Matrix

from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
