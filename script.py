import utils


def coffee_bot():
    print("Welcome to the cafe!")

    order_drink = "y"

    drinks = []
    while order_drink == "y":
        size = utils.get_size()
        drink_type = utils.get_drink_type()

        drink = "{} {}".format(size, drink_type)
        print(f"Alright, that's a {size} {drink_type}")

        drinks.append(drink)
        while True:
            order_drink = input(
                "Would you like to order another drink? (y/n) \n "
            ).lower()
            if order_drink in ["y", "n"]:
                break

    print("Okay, so I have: ")
    for drink in drinks:
        print(f"- {drink}")

    name = input("Can I get your name please? ")
    print(f"Thanks, {name}! Your drink will be ready shortly!")


# Call coffee_bot()
coffee_bot()
