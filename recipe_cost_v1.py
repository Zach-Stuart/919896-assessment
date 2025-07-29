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


# main routine

# lists to hold ingredient details
all_names = []
all_amounts = []
all_prices = []

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
    ingredient_amount_gram_check = not_blank("Amount (in grams): ")

    # ask for ingredient price
    ingredient_price_check = not_blank("Price (per 100g): ")

    print()
    # ask if there are more ingredients
    more_ingredients_check = string_check("Is there another ingredient you'd like to list? ")

    # if there are no more ingredients, break the loop
    if more_ingredients_check == "yes":
        break