import data


def calculate_amount(quarters, dimes, nickles, pennies):
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    return quarters_total + dimes_total + nickles_total + pennies_total


drink = input("would you like? (espresso/latte/cappuccino): ")
if drink == "report":
    print(
        f"water: {data.resources['water']}\nmilk: {data.resources['milk']}\ncoffe: {data.resources['coffee']}")
else:
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickles = float(input("how many nickles? "))
    pennies = float(input("how many pennies? "))

    if data.MENU[drink]["cost"] > calculate_amount(quarters, dimes, nickles, pennies):
        print(
            f"Not enough money, {data.MENU[drink]['cost']} and you have: {calculate_amount(quarters,dimes,nickles,pennies)} Money refunded")
