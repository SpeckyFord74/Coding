import pandas as pd

fruits = pd.DataFrame({
    'Apples': [30],
    'Bananas': [21]
})
print(fruits)

fruit_sales = pd.DataFrame({
    'Apples': [35, 41],
    'Bananas': [21, 34]
}, index=['2017 Sales', '2018 Sales'])
print(fruit_sales)

print("\n")

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)

print("\n")

reviews = pd.read_csv("Learning Activities\\wine_reviews.csv")
print(reviews)

print("\n")

animals = pd.DataFrame({
    'Cows': [12, 20],
    'Goats': [22, 19]
}, index=['Year 1', 'Year 2'])
print(animals)
animals.to_csv("Learning Activities\\Excercises\\cows_and_goats.csv")