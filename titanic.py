import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression 

model = LogisticRegression()	

df = pd.read_csv('titanic.csv')

df['male'] = df['Sex'] == 'male'

X =  df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values

Y = df['Survived'].values

#Y = tes.reshape(1,-1)
model.fit(X,Y)
pred =[[3,True,22.0,1,0,7.25]]
print(model.predict(pred))
print(model.predict(X[:5]))
print(Y[:5])
print(model.score(X,Y))
Passanger = Y.shape[0]
print(Passanger)
print(Y.shape[0])