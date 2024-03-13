import pandas as pd
import numpy as np 

df = pd.read_csv(r"D:/Desktop/PhoneBook.csv")

print(df.head())

phone = df.iloc[:10,2:3]
print(phone)

shape = np.shape(phone)
print(shape)

size = np.size(phone)
print(size)


