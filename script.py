def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print(f"Alright, that's a {size} {drink_type}")
    name = input("Can I get your name please? ")
    print(f"Thanks, {name}! Your drink will be ready shortly!")


# Functions
def print_message():
    """A function that is executed when wrong option is selected and prints a
    message"""
    print(
        "I'm sorry, I did not understand your selection."
        "Please enter the corresponding letter to your response."
    )


def get_size():
    """Prompts the user to enter the size of a coffee and returns the selected size."""
    res = input(
        "What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n"
    ).lower()
    size = ""

    if res == "a":
        size = "small"
    elif res == "b":
        size = "medium"
    elif res == "c":
        size = "large"
    else:
        print_message()
        # Utilizing recursion to persistently prompt until correct option selected
        size = get_size()

    return size


def get_drink_type():
    """Prompts the user to enter the coffee type and returns the selected value."""
    res = (
        "What type of drink can I get for you? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n"
    ).lower()

    drink_type = ""

    if res == "a":
        drink_type = "brewed coffee"
    elif res == "b":
        drink_type = "mocha"
    elif res == "c":
        drink_type = order_latte()
    else:
        print_message()
        # Utilizing recursion to persistently prompt until correct option selected
        drink_type = get_drink_type()

    return drink_type


def order_latte():
    res = input(
        "And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n"
    ).lower()
    latte_type = ""

    if res == "a":
        latte_type = "latte"
    elif res == "b":
        latte_type = "non-fat latte"
    elif res == "c":
        latte_type = "soy latte"
    else:
        print_message()
        # Utilizing recursion to persistently prompt until correct option selected
        latte_type = order_latte()

    return latte_type


# Call coffee_bot()
coffee_bot()
