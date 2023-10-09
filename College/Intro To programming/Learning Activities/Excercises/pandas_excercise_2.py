import pandas as pd

wine_rev = pd.read_csv("Learning Activities\\wine_reviews.csv")

desc = wine_rev.loc[:, "description"]
print(desc)

first_description = wine_rev.loc[0, "description"]
print(first_description)

first_row = wine_rev.iloc[1]
print(first_row)

first_description = wine_rev["description"].head(10)
print(first_description)

sample_reviews = wine_rev.iloc[[1,2,3,5,8]]
print(sample_reviews)

df = wine_rev.loc[[0,1,10,100], ["country", "province", "region_1", "region_2"]]
print(df)

df = wine_rev.loc[:99, ["country", "variety"]]
print(df)

italian_wines = wine_rev.loc[wine_rev["country"] == "Italy"]
print(italian_wines)

top_oceanic_wines = wine_rev.loc[(wine_rev["points"] >= 95) & (wine_rev["country"].isin(["Australia", "New Zealand"]))]
print(top_oceanic_wines)