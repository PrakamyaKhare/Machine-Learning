from sklearn.linear_model import LinearRegression as LR
import pandas as pd

df = pd.read_csv('time.csv')
X = df[['Status','Hours']].values
Y = df['Result'].values
model = LR()
model.fit(X,Y)
print(X)
print(Y)
print(model.coef_,model.intercept_)
X_test = [[100,10]]
print(model.predict(X_test))