### PA3_LEGASPI

### Problem#1

A CSV file named cars.csv is imported into a dataframe using pandas. To quickly check the contents, the first and last five rows are shown. This is done by calling .head() and .tail(), which by default return five rows.

import pandas as pd

# load the cars dataset
cars = pd.read_csv("cars.csv")

# show first 5 rows
cars.head()

# show last 5 rows
cars.tail()

### Problem #2

Subsetting, Slicing, and Indexing
For this part, different indexing techniques were applied to the cars dataframe:

.iloc[:5, ::2] was used to grab the first five rows, but only every other column, which means it shows the odd-numbered columns.

To display the row for Mazda RX4, the condition cars['Model'] == 'Mazda RX4' was used with .loc[].

To find how many cylinders Camaro Z28 has, the same method was used, but only the cyl column was selected.

Lastly, a list of car models was stored in a variable called models. With .isin(), only those rows were returned, showing their cyl and gear values.

print(cars.iloc[:5, ::2])

print(cars.loc[cars['Model'] == 'Mazda RX4'])

print(cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']])

models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
print(cars.loc[cars['Model'].isin(models), ['cyl', 'gear']])
