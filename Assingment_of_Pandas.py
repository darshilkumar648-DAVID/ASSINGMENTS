import pandas as pd

# 1) Create a series of three different colors
colors = pd.Series(['Red', 'Blue', 'Green'])

# 2) View the series of different colors
print("Colors Series:")
print(colors)


# 3) Create a series of three different car types and view it
cars = pd.Series(['BMW', 'Toyota', 'Honda'])

print("\nCars Series:")
print(cars)



# 4) Combine the Series of cars and colors into a DataFrame
car_data = pd.DataFrame({
    'Car': cars,
    'Color': colors
})

print("\nCar Data DataFrame:")
print(car_data)


# Add extra columns for later questions
car_data['Make'] = ['Germany', 'Japan', 'Japan']
car_data['Doors'] = [4, 4, 2]
car_data['Price'] = [50000, 30000, 25000]


# 5) Find the different datatypes of the car data DataFrame
print("\nData Types:")
print(car_data.dtypes)


# 6) Describe your current car sales DataFrame using describe()
print("\nDescribe DataFrame:")
print(car_data.describe())


# 7) Get information about your DataFrame using info()
print("\nInfo:")
print(car_data.info())


# 8) Create a Series of different numbers and find the mean
numbers_mean = pd.Series([10, 20, 30, 40, 50])
print("\nMean of numbers:", numbers_mean.mean())


# 9) Create a Series of different numbers and find the sum
numbers_sum = pd.Series([5, 15, 25, 35, 45])
print("Sum of numbers:", numbers_sum.sum())


# 10) List out all the column names of the car sales DataFrame
print("\nColumn Names:")
print(car_data.columns)


# 11) Find the length of the car sales DataFrame
print("\nLength of DataFrame:", len(car_data))


# 12) Show the first 5 rows
print("\nFirst 5 rows:")
print(car_data.head(5))


# 13) Show the first 7 rows
print("\nFirst 7 rows:")
print(car_data.head(7))


# 14) Show the bottom 5 rows
print("\nBottom 5 rows:")
print(car_data.tail(5))


# 15) Use .loc to select the row at index 3
# (Add one more row so index 3 exists)
car_data.loc[3] = ['Ford', 'Black', 'USA', 4, 40000]

print("\nRow at index 3 using loc:")
print(car_data.loc[3])


# 16) Use .iloc to select the row at position 3
print("\nRow at position 3 using iloc:")
print(car_data.iloc[3])


# 17) Create a crosstab of the Make and Doors columns
print("\nCrosstab (Make vs Doors):")
print(pd.crosstab(car_data['Make'], car_data['Doors']))