import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model,metrics

#load the boston dataset
boston=datasets.load_boston(return_X_y=False)
X=boston.data
Y=boston.target

#defininf feature natrix(X) and response vector (Y)
from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.4,random_state=1)

#create linear regression object
reg=linear_model.LinearRegression()

#train the model using the training sets
reg.fit(Xtrain,Ytrain)

#regression coefficients
print("cofficient:\n",reg.coef_)

#variance score: 1 means perfect prediction
print("Variance score:{}".format(reg.score(Xtest,Ytest)))

#plot for residual error#setting plot style
plt.style.use('fivethirtyeight')

#plotting residual errors in training data
plt.scatter(reg.predict(Xtrain),reg.predict(Xtrain)-Ytrain,color="blue",s=10,label='Train data')

#plotting residual errors in test data
plt.scatter(reg.predict(Xtest),reg.predict(Xtest)-Ytest,color="green",s=10,label='Test data')

#plotting line for zero residual error
plt.hlines(y=0,xmin=0,xmax=50,linewidth=2)

#plotting legend
plt.legend(loc="upper right")
plt.title("Residual errors")
plt.show()
