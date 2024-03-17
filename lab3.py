import numpy as np
import pandas as pd
import os

titanic_train= pd.read_csv("/home/eren/İndirilenler")
titanic_train.shape
(891,12)

titanic_train.head()

#del titanic_train("PassangerId")

#new_pclass = pd.Categorical(titanic_train("Pclass"),ordered=True)
#new_pclass you = new_pclass.rename_categories(["Class1","Class2","Class3"])
#new_pclass.describe()
#titanic_train["Pclass"] = new_pclass

#titanic_train["Pclass"]
#titanic_train["Age"].describe()

#missing = np.where(titanic_train["Age"].isnull()==True)
#missing()

#len(missing[0])

#177

#titanic_train(column = "Age", figsize(9,6),bins=20)

#new_age_var = np.where(titanic_train["Age"].isnull(),28,titanic_train["Age"])
#titanic_train["Age"]= new_age_var
#titanic_train["Age"].describe()

#titanic_train.hist(column= "Age")
