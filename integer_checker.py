# functions
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


# main routine

# loop for testing
while True:
    print()

    # ask user for an integer
    my_num = int_check("Choose a number more than zero: ")
    print(f"You chose: {my_num}")