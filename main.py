import data


def calculate_amount(quarters, dimes, nickles, pennies):
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    return quarters_total + dimes_total + nickles_total + pennies_total


def check_resources(resources, drink):
    for key in resources:
        if drink[key] > resources[key]:
            not_enough.append(key)
            return False
        else:
            return True


should_continue = True
not_enough = []


while should_continue:
    drink = input("would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "report":
        print(
            f"water: {data.resources['water']}\nmilk: {data.resources['milk']}\ncoffe: {data.resources['coffee']}")
        should_continue = False
        break

    elif drink == "off":
        should_continue = False
        break

    print("Please insert coins: ")
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickles = float(input("how many nickles? "))
    pennies = float(input("how many pennies? "))

    if data.MENU[drink]["cost"] > calculate_amount(quarters, dimes, nickles, pennies):
        print(
            f"Not enough money, {data.MENU[drink]['cost']} and you have: {calculate_amount(quarters,dimes,nickles,pennies)} Money refunded")

    elif check_resources(data.resources, data.MENU[drink]["ingredients"]) == False:
        print(
            f"Sorry, not enough resources: {not_enough}, Money refunded: {calculate_amount(quarters,dimes,nickles,pennies)}")
        not_enough.clear()
    else:
        for key in data.resources:
            data.resources[key] = data.resources[key] - \
                data.MENU[drink]["ingredients"][key]
        money = calculate_amount(quarters, dimes, nickles, pennies)
        print(
            f"here is your drink {drink} and here is your money {round(money - data.MENU[drink]['cost'],2)} ")
