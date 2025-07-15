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

# main routine

# make_statement("Recipe Cost Calculator", "*")

# print()
# want_instructions = string_check("Would you like to see the instructions? ")

# if want_instructions == "yes":
# instructions()

# print()
# print("program continues")
