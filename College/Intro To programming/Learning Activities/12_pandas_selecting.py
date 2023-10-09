import pandas as pd
import random as rd

wine_rev = pd.read_csv("Learning Activities\\wine_reviews.csv")

# print(wine_rev["country"] == "US")

print(wine_rev.loc[(wine_rev["country"] == "US") & (wine_rev["points"] == 90)])

print(wine_rev.loc[wine_rev["country"].isin(["US", "France"])])

wine_rev["Age"] = wine_rev.iloc[:, 4:6].sum(axis=1)
print(wine_rev)



print(wine_rev.loc[(wine_rev["country"] == "US") & (wine_rev["region_2"].isnull())])

