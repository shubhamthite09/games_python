from collections import Counter

espresso = {"water": 50, "coffee": 18 }
latte = {"water": 200, "milk": 150, "coffee": 24 }
cappuccino = {"water": 250, "milk": 100, "coffee": 24}
resources = { "water": 300, "milk": 200, "coffee": 100 }
def coin_counter():
    quarters_count = quarters * 0.25
    dime_count = dime * 0.10
    nikels_count = nikels * 0.05
    pennie_count = pennie * 0.01
    return quarters_count + dime_count +nikels_count + pennie_count
def espresso_blend ():
    updated_resources = resources.substract(espresso)
    resources.append(updated_resources)

def latte_blend ():
    st = counter(resources)
    vt = counter(latte)
    updated_resources = st - vt
    resources.update(updated_resources)
def cappuccino_blend ():
    updated_resources = resources.substract(cappuccino)
    resources.append(updated_resources)

# todo: 1. input from user to select type of coffe
# type_of_coffe  = input("choose your coffe espresso , latte or ingredients: ")
# print("enter coins for your coffe")
# quarters = int(input("how many of quarters:  "))
# dime = int(input("how many of dime:  "))
# nikels = int(input("how many of nikels:  "))
# pennie = int(input("how many of pennie:  "))
espresso_blend()
print(resources)


# todo: 2. 1