Question 1: From given data set print first and last five rows.

For First five rows
import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
df.head(5)

For last five rows
import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
df.tail(5)

Question 2: Clean data and update the CSV file.

df = pd.read_csv("Downloads\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})
print (df)

df.to_csv("D:\\Automobile_data.csv")

Question 3: Find the most expensive car company name.

import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df 

Question 4: Print All Toyota Cars details.

import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
car = df.groupby('company')
toyotadf = car.get_group('toyota')
toyotadf

Question 5: Count total cars per company.

import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
df['company'].value_counts()

Question 6: Find each company’s Higesht price car.

import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
car = df.groupby('company')
pricedf = car['company','price'].max()
pricedf

Question 7: Find the average mileage of each car making company.

import pandas as pd
df = pd.read_csv("Downloads\\Automobile_data.csv")
car = df.groupby('company')
mileagedf = car['company','average-mileage'].mean()
mileagedf

Question 8: Sort all cars by Price column.

import pandas as pd
carsdf = pd.read_csv("Downloads\\Automobile_data.csv")
carsdf = carsdf.sort_values(by=['price'], ascending=False)
carsdf.head(5)
Question 9: Concatenate two data frames using the following conditions

Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame.
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}


import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsdf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsdf2 = pd.DataFrame.from_dict(japaneseCars)

carsdf = pd.concat([carsdf1, carsdf2], keys=["Germany", "Japan"])
carsdf

Question 10: Merge two data frames using the following condition

Create two data frames using the following two Dicts, Merge two data frames, and append the second data frame as a new column to
the first data frame.
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPricedf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerdf = pd.DataFrame.from_dict(car_Horsepower)

carsdf = pd.merge(carPricedf, carsHorsepowerdf, on="Company")
carsdf









