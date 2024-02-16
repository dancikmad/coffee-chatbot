def print_message():
    print(
        "I'm sorry, I did not understand your selection."
        "Please enter the corresponding letter for your response."
    )


# Functions that prompt the user to select coffee attributes such as size, type.
def get_size():
    res = input(
        "What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> "
    ).lower()

    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print_message()
        return get_size()


def get_drink_type():
    coffee_menu = "What type of drink would you like: "
    coffee_menu += "\n[a] Brewed Coffee"
    coffee_menu += "\n[b] Mocha"
    coffee_menu += "\n[c] Latte"
    coffee_menu += "\n[d] Flat White"
    coffee_menu += "\n[e] Americano"
    coffee_menu += "\n[f] Espresso \n: "
    
    res = input(coffee_menu).lower()
    if res == "a":
        return "brewed coffee"
    elif res == "b":
        return order_mocha()
    elif res == "c":
        return order_latte()
    elif res == "d":
        return "flat white"
    elif res == "e":
        return "americano"
    elif res == "f":
        return "espresso"
    else:
        print_message()

    return get_drink_type()


# Functions for processing coffee orders and selecting coffee types.
def order_latte():
    res = input(
        "And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> "
    ).lower()

    if res == "a":
        return "latte"
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print_message()
        return order_latte()


def order_mocha():
    mocha_menu = "Would you like to try our limited-edition white mocha? "
    mocha_menu += "\n[a] Sure!"
    mocha_menu += "\n[b] Maybe next time! \n: "
    
    while True:
        res = input(mocha_menu).lower()

        if res == "a":
            return "white mocha"
        elif res == "b":
            return "mocha"
        print_message()
