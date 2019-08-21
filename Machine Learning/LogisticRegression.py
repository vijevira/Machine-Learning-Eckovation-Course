import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font",size=14)


from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid",color_codes=True)

data=pd.read_csv('bank.csv',header=0)
print(data.shape)
data.dropna(inplace=True)
print(data.shape)
print(list(data.columns))

data['education'].unique()
data['y'].unique()
