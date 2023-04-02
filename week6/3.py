import pandas as pd

# data = pd.read_excel("uscities.xlsx")

a=pd.Series([1,2,3,4,5,6])

b=pd.Series(3,range(4))

b.index=["q","w","e","f"]

dataframe = pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]})
print(dataframe)
print(dataframe.iloc[:2])

