# Functions go here
def make_statement(statement, decoration, lines):
    """Emphasises heading by adding decoration
    at the start and end"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)


    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# Main routine goes here
make_statement("Progamming is fun", "=", 3)
print()
make_statement("Progamming is still fun", "+", 2)
print()
make_statement("Emoji in action", "👍", 1)
