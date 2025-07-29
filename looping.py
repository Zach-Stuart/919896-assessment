def not_blank(question):
    """checks that user response isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again\n")


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


# main routine

# ingredient loop
while True:
    print()
    # ask for the name of ingredient
    ingredient_name_check = not_blank("Ingredient Name: ")

    print()
     # ask if there are more ingredients
    more_ingredients_check = string_check("Is there another ingredient you'd like to list? ")

    # if there are no more ingredients, break the loop
    if more_ingredients_check == "no":
        break
