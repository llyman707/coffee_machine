MENU = {
    'latte':
    { 'ingredients': {"water": 200, "coffee": 24, "milk": 150, }, 
    'cost': 1.20, },
    'espresso':
     {'ingredients': {"water": 50, "coffee": 18},
     'cost': 0.75, },
    'cappuccino':
    {'ingredients': {"water": 250, "coffee": 24, "milk": 150, },
     'cost': 1.54, },
    }

resources = {
    'water': 200,
    'milk': 300,
    'coffee': 50,
    'money': 0
}

def make_coffee(coffee_type, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_type}. Enjoy!")
    return 

def check_resources(coffee_type, ingredients, resources):
    for item in ingredients:
        if ingredients[item] > resources[item]:    
            print(f"Sorry there is not enough {item}")
    return process_coins(coffee_type, 0.25, 0.10, 0.05, 0.01)
            
def process_coins(coffee_type, quarter, dime, nickel, penny):
    total = 0
    print("Please input coins")
    quarters = int(input(f"How many quarters: "))
    dimes = int(input(f"How many dimes: "))
    nickels = int(input(f"How many nickels: "))
    pennies = int(input(f"How many pennies: "))
    total += quarters * quarter
    total += dimes * dime
    total += nickels * nickel
    total += pennies * penny
    if total > MENU[coffee_type]['cost']:
        change = total - MENU[coffee_type]['cost']
        print(f"Your change is {change}.")
        resources['money'] = total 
        return make_coffee(coffee_type, MENU[coffee_type]['ingredients'])
    elif total == MENU[coffee_type]['cost']:
        return make_coffee(coffee_type, MENU[coffee_type]['ingredients'])
    else:
        return
   
def coffee_machine():
    machine_on = True
    while machine_on:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        
        if coffee_type == 'report':
            print(f"Water:{resources.get('water')} ml")
            print(f"Milk:{resources.get('milk')} ml")
            print(f"Coffee:{resources.get('coffee')} g")
            print(f"Money: ${resources.get('money')}")
            return
        elif coffee_type == 'off':
            print("Coffee Machine is OFF")
            machine_on = False
        else:
            return check_resources(coffee_type, MENU[coffee_type]['ingredients'], resources)
            

coffee_machine()