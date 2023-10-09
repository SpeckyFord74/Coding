# Import the pandas library and alias it as 'pd'
import pandas as pd

# Read a CSV file named 'wine_reviews.csv' into a pandas DataFrame and assign it to 'wine_rev'
wine_rev = pd.read_csv("Learning Activities\\wine_reviews.csv")

print(wine_rev.country)
print("\n")

# Print the 'country' column of the 'wine_rev' DataFrame
print(wine_rev['country'])

# Print the value in the 'country' column at index 0 (first row)
print(wine_rev['country'][0])
print("\n")

# Print the data in the second row of the DataFrame
print(wine_rev.iloc[1])
print("\n")

# Print the entire 'country' column
print(wine_rev.iloc[:,1])
print("\n")

# Print the first 5 rows of the 'country' column
print(wine_rev.iloc[:5, 1])
print("\n")

# Print the values in the 'country' column for rows 2 and 3
print(wine_rev.iloc[1:3,1])
print("\n")

# Print a specific slice of rows and columns from the 'wine_rev' DataFrame.
# Rows 2 to 9 (inclusive) and columns 3 and 5 (with a step of 2).
print(wine_rev.iloc[1:10, 2:5:2])
print("\n")

# Print the 'country' column values for rows 0, 1, and 2
print(wine_rev.iloc[[0,1,2], 1])
print("\n")

# Print the last 5 values in the 'country' column
print(wine_rev.iloc[-5:,1])
print("\n")

# Print the value in the 'country' column at row 0 using the 'loc' function
print(wine_rev.loc[0,'country'])
print("\n")

# Print selected columns ('country', 'description', and 'points') for all rows using 'loc'
print(wine_rev.loc[:, ['country', 'description', 'points']])

print(wine_rev.loc[5:100:2, ['country', 'description', 'points']])