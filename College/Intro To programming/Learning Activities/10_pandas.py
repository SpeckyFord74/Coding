import pandas as pd

#Creates a dictionary where the values are lists
my_data_set = {
    'Cars' : ["BMW", "Volvo", "Ford"],
    'Passings' : [3, 7, 2]
}

df = pd.DataFrame(my_data_set) #Uses the pandas package to make the dictionary a table to make looking at it easier
print(df)

#Creates a variable that is a table created by pandas using a dictionary and manually setting the indexes
df_2 = pd.DataFrame({
    'Bob': ["I liked it.", "It was awful."],
    'Sue': ["Pretty good.", "Bland."]
    },
    index=['Product A:', 'Product B:']
    )

print(df_2)

#Creates a series which is a series of data values. Unlike a DataFrame, Series does not make a table, rather a list of sorts
sr_1 = pd.Series([1, 2, 3, 4, 5])
print(sr_1)

#Creates a Series where the indexes are provided manually. Also a name is provided.
sr_2 = pd.Series([30, 35, 40],
                 index=['2015 Sales', '2016 Sales', '2017 Sales'],
                 name='Product A'
                 )

print(sr_2)