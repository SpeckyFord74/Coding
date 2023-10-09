import pandas as pd

wine_ratings = pd.read_csv("Learning Activities\\wine_reviews.csv", index_col=0) #Sets the csv file into a variable and removes pandas auto index feature
print(wine_ratings.shape) #Printing how many rows and columns there are in the file. .shape is a property
print(wine_ratings.head(10)) #Printing the first 10 rows of the file
print(wine_ratings.tail(10)) #Printing the last 10 rows of the file

#Creates a data set that will be made into a csv file
my_data_set = {
    'names': ["Corey", "Lewis", "Ayo"],
    'Number': [1, 2, 3]
}

df_1 = pd.DataFrame(my_data_set) #Makes my_data_set a DataFrame
df_1.to_csv("Learning Activities\\df_1.csv") #Uses a builtin pandas function to make a DataFrame a csv file
