def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question).strip()

        if response.lower() == "xxx":
            return "xxx"

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.")


# main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")
