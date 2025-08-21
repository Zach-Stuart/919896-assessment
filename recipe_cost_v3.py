import pandas
import random


# functions
def make_statement(statement, decoration):
    """"emphasises headings by adding decoration on the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """checks that users enter the full word
    or the 'n' letter/s of the word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if response is the entire word
            if response == item:
                return item

            # check if it's the "n" letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    make_statement("Instructions", "🔍")

    print('''

    Please enter:
    - The name of each ingredient of the recipe
    - The amount of each ingredient needed (in grams)
    - The cost of each ingredient
    - The serving size of the recipe

    The program will then use this information to calculate the total cost of the recipe, as well as the cost per serving.

    ''')


def not_blank(question):
    """checks that user response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again\n")


def int_check(question):
    """checks users enter an integer"""

    error = "Oops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        # check for exit code
        if response == "xxx":
            return response

        try:
            # change response to an integer and check it's more than 0
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def float_check(question):
    """checks users enter a float"""

    error = "Oops - please enter a float more than zero."

    while True:
        response = input(question).lower()

        # check for exit code
        if response == "xxx":
            return response

        try:
            # change response to an integer and check it's more than 0
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine

# lists to hold ingredient details
all_names = []
all_amounts = []
all_prices = []

ingredients_dict = {
    'Name': all_names,
    'Amount (in grams)': all_amounts,
    'Price': all_prices
}

make_statement("Recipe Cost Calculator", "*")

# ask user if they want to see instructions
print()
want_instructions = string_check("Would you like to see the instructions? ")

if want_instructions == "yes":
    instructions()

# ask user for the name of their recipe
print()
recipe_name_ask = not_blank("What is the name of your recipe? ")

print()
print("Awesome. Now, please enter the following details for each ingredient...")

# ingredient details loop
while True:

    print()
    # ask for the name of ingredient
    ingredient_name_check = not_blank("Ingredient Name: ")

    # ask for ingredient amount in grams
    ingredient_amount_gram_check = int_check("Amount (in grams): ")

    # ask for ingredient price
    ingredient_price_check = float_check("Price (per 100g): ")

    print()
    # ask if there are more ingredients
    more_ingredients_check = string_check("Is there another ingredient you'd like to list? ")

    # add ingredient name, amount in grams and price per 100g
    all_names.append(ingredient_name_check)
    all_amounts.append(ingredient_amount_gram_check)
    all_prices.append(ingredient_price_check)

    # if there are no more ingredients, break the loop
    if more_ingredients_check == "no":
        break

# ask for serving size
print()
serving_size = float_check("What is the serving size of your recipe? ")

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
print(f"The total price of your recipe. {recipe_name_ask} is: ${total_price:.2f}")

# print cost per serving
print()
print(f"The cost per serving of your recipe, {recipe_name_ask} is ${cost_per_serving:.2f}")