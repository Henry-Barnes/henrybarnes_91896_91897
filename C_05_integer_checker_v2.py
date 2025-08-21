# functions goes here
def int_check(question, low, high):
    """Checks users enter an integer between two values / float that is more than zero (or the 'xxx' exit code)"""

    error = f"Oops - please enter a whole number between {low} and {high}, or type 'xxx' to exit the program."

    while True:
        response = input(question).strip()

        if response == "xxx":
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = int(response)

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for integer
    my_num = int_check("Choose a number: ", 1, 10)
    print(f"You chose {my_num}")
