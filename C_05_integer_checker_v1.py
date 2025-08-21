# functions goes here
def int_check(question):
    """"Checks that users enter an integer  that is more than zero
    (or the optional exit code)"""

    error = "Oops - please enter an integer more than zero."

    while True:
        response = input(question).lower()

        if response == "xxx":
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# loop for testing purposes...
while True:
    print()

    my_float = int("Please enter a number more than 0: ", float)
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = int("Please enter an integer more than 0", "integer", "")

    if my_int == "":
        print("You have chose infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")