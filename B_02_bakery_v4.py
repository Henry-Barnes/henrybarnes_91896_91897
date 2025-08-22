import pandas
import numpy


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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question).strip()

        if response.lower() == "xxx":
            return "xxx"

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.")


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


def currency(x):
    """Formats number as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main Routine goes here

# Initialise ticket numbers
MAX_SPEND = 50

# lists to hold ticket details
all_menu = ["Croissant", "Bagel", "Muffin", "Donut", "Sourdough Loaf", "Cupcake"]
all_bakery_costs = [6, 4, 3, 5, 8, 3]

bakery_dict = {
    'Item Name': all_menu,
    'Item Price': all_bakery_costs,
}

# create dataframe / table from dictionary
bakery_frame = pandas.DataFrame(bakery_dict)

# Rearranging index
bakery_frame.index = numpy.arange(1, len(bakery_frame) + 1)

# Currency Formatting (uses currency function)
add_dollars = ['Item Price']
for var_item in add_dollars:
    bakery_frame[var_item] = bakery_frame[var_item].apply(currency)

# Program main heading
print(make_statement("Bakery Ordering Assistant", "🍞"))

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ", allow_exit=False)

if want_instructions == "yes":
    instructions()

print()

# Ask user for their name
name = not_blank(f"What is your name? ")

# Ask for their budget and check it's between 3 and 50
budget = int_check(f"Welcome {name}. Please enter budget: ", 3, 50)
if budget == "xxx":
    print()
    print(make_statement(f"{name}'s Order Receipt", "🛒"))
    print()
    print("No Items purchased.")
    exit()

print(f"Budget accepted: ${budget}")

purchased_items = []
purchased_items_prices = []

# creating dictionary for receipt
purchased_dict = {
    'Item Name': purchased_items,
    'Item Prices': purchased_items_prices
}

# Loop to get name, age and budget details
while budget >= min(all_bakery_costs):

    print()

    # Display menu items
    print(make_statement("Bakery Menu", "📜"))
    print(bakery_frame)
    print()

    # Prompt the user to select a row using the index
    try:
        # ask for the user item
        choice = int_check("Enter the number of the item you would like to choose: ", 1, 6)
        if choice == "xxx":
            print(make_statement("Exiting Program", "❌"))
            break

        selected_row = all_menu[choice - 1]
        item_price = all_bakery_costs[choice - 1]

        if budget >= item_price:
            budget -= item_price

            purchased_items.append(selected_row)
            purchased_items_prices.append(item_price)

            # display user selection
            print(f"You selected: {selected_row} ${item_price}")

            print(f"Your new budget is: ${budget} ")

        else:
            print("You cannot afford this item. Please choose a different one.")
            continue

        #
        if budget < 3:
            print()
            print(f"Your remaining budget is ${budget}, this is too small to make another purchase.")
            print(f"You will now be taken to your receipt.")
            break

        repurchase = string_check("Would you like to make another purchase? ", allow_exit=False)
        if repurchase == "no":
            break

    except ValueError:
        print("Please enter a valid number.")
# End of Ticket Loop

# Receipt and Summary
print()
print(make_statement(f"{name}'s Order Receipt", "🛒"))
print()

if purchased_items:  # only show receipt if user bought something
    purchased_items_frame = pandas.DataFrame(purchased_dict)
    purchased_items_frame.index = numpy.arange(1, len(purchased_items_frame) + 1)
# Currency Formatting (uses currency function)
    add_dollars = ['Item Prices']
    for var_item in add_dollars:
        purchased_items_frame[var_item] = purchased_items_frame[var_item].apply(currency)
    print(purchased_items_frame)

    total_spent = sum(purchased_items_prices)
    print()
    print(f"Total spent: ${total_spent:.2f}")
    print(f"Remaining budget: ${budget:.2f}")
    print(f"Thank you {name} for using the Bakery Ordering Assistant.")
    print("Come back soon! 💖")
else:
    print("No items purchased.")
