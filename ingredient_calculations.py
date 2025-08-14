import pandas

# lists to hold ingredient details
all_names = ["a", "b", "c"]
all_amounts = [150, 200, 100]
all_prices = [1.5, 2, 1]

# default serving size for testing
serving_size = 2.5

ingredients_dict = {
    'Name': all_names,
    'Amount (in grams)': all_amounts,
    'Price': all_prices
}

# create dataframe / table from dictionary
ingredients_frame = pandas.DataFrame(ingredients_dict)

# add all ingredient prices together
# multiply ingredient price by amount in grams (divide by 100 to get accurate result)
total_ingredient_price = (ingredients_frame['Price'] * ingredients_frame['Amount (in grams)'] / 100).sum()

# multiply total ingredient price by serving size
total_price = total_ingredient_price * serving_size

# cost per serving
cost_per_serving = total_price / serving_size

# print ingredients frame
print(ingredients_frame.to_string(index=False))

# print total price
print()
print(f"The total price of your recipe is: ${total_price:.2f}")

# print cost per serving
print()
print(f"The cost per serving of your recipe is ${cost_per_serving:.2f}")