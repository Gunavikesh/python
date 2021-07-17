import pandas as pd
import numpy as np
data = pd.read_csv("Diabities.csv")
data.head(10)
data.info()
data.isnull().sum()
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.10,random_state = 0)

from sklearn.ensemble import RandomForestClassifier
x_train = [[0, 0, np.nan], [np.nan, 1, 1]]
y_train = [0, 1]
classifier =RandomForestClassifier(n_estimators = 1000,random_state = 0)
classifier.fit(x_train, y_train)

y_pred = classifier.preddict(x_test)
