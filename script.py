import utils

def coffee_bot():
    print("Welcome to the cafe!")
    size = utils.get_size()
    drink_type = utils.get_drink_type()
    print(f"Alright, that's a {size} {drink_type}")
    name = input("Can I get your name please? ")
    print(f"Thanks, {name}! Your drink will be ready shortly!")


# Call coffee_bot()
coffee_bot()
