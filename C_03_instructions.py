# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1, allow_exit=True):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        if allow_exit and response == "xxx":
            return "xxx"

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}.")


def instructions():
    print(make_statement("Instructions", "📋"))
    print('''
Welcome to the Bakery Ordering Assistant!

You will:
- Enter your name.
- Enter your budget between $3 & $50 (whole numbers only).
- View a numbered menu of bakery items.
- Enter the number of the item you want to buy (one item at a time).
- After each purchase, your budget updates and you be asked if you'd like to make another purchase.
- Keep buying until you're finished or out of money.
- At any time after entering your name, you can type 'xxx' to exit to your receipt.

A final receipt will be shown at the end.
        ''')


# Main routine goes here

print(make_statement("Bakery Ordering Assistant", "🍞"))

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ", allow_exit=False)

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
