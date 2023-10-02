# This is a sample Python script.
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #reading data from file
data=pd.read_csv("D:\cats_vs_dogs.csv")
print(data)
#Explpring data
print(data.describe())
print(data.info)
print(data.head())
print("data is",data.tail())
#Know if we have null value at column or not
null_val=data.isnull().sum()
print(null_val)
#removing unwanted data or null data
# data.drop("avg_cats_per_household",inplace=True,axis=1)
# data.drop("cat_population",inplace=True,axis=1)
# data.drop("state",inplace=True,axis=1)
#univariate visualtion
convertedx_avgcatsperhousehold=np.array(data["avg_cats_per_household"])
convertedy_state=np.array(data["state"])
print(convertedx_avgcatsperhousehold)
print(convertedy_state)
plt.xlabel("Average of cat of one home")
plt.ylabel("state")
plt.plot(convertedx_avgcatsperhousehold,convertedy_state)
plt.show()
#quanatitve data anlize
x2=np.array(data["avg_cats_per_household"])
y2=np.array(data["cat_population"])
sns.barplot(x2)
plt.show()
sns.displot(y2)
plt.show()
#qualitive data using boxblot
sns.boxplot(convertedy_state)
plt.show()
#Finally we can discover that we cant using lenear regrssion model
#AI & Software Engineer Ahmed Ashraf Fayad




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
