#1 what would you like espresso, latte, cappaccino
#     depending on answer print the following prompt - espresso, latte, cappachino, report, stop

# #2 compare recipe with current report
#     if not enough print "sorry not enough coffee, water, milk"

# #3 if enough ask for money
#     please insert coins
#     prompt how many quarters, dimes, nickels, pennies
#     compare against price of product
#         if greater than product - print the change
#         elif correct price make coffee
#         else not enought - sorry not enough money - end program
reserves = {
    "water": 200,
    "milk": 300,
    "coffee": 50
}

money = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01
}

menu = {
    'latte': 1.20,
    'espresso': 0.75,
    'cappuccino': 1.54
    }  

recipes = {
    'latte': {"water": 200, "coffee": 24, "milk": 150},
    'espresso': {"water": 50, "coffee": 18},
    'cappuccino': {"water": 250, "coffee": 24, "milk": 150}
    }

def coffee_machine():
    money_inserted = 0
    reserves = {"water": 200, "coffee": 50, "milk": 300}
    machine_on = True
    
    def deduct_resources(reserves, recipe):
         for ingredient, amount in recipe.items():
              reserves[ingredient] -= amount

    def calculate_total(money):
        total = 0
        print("Please insert coins.")
        for coin, value in money.items():
            count = int(input(f"How many {coin}s?: "))
            total += count * value
        return round(total, 2)

    def report(reserves, money_inserted):
            print(f"Water: {reserves["water"]} ml")
            print(f"Milk: {reserves["milk"]} ml")
            print(f"Coffee: {reserves["coffee"]} g")
            print(f"Money: $ {money_inserted}")

    def process_purchase(drink_name, price, money_inserted):
            if money_inserted < price:
                print("Sorry you do not have enough money")
                return None
            money_inserted -= price
            print(f"Here is your {drink_name}. Enjoy!")

            if money_inserted > 0:
                print(f"Your change is: {money_inserted}")
        
            return money_inserted     

    def missing_ingredient(resources, recipe):
        for ingredient, amount_needed in recipe.items():
            if resources.get(ingredient, 0) < amount_needed:
                return ingredient
        # for ingredient, amount in recipe.items():
        #     resources[ingredient] -= amount
        return None

    while machine_on:
        make_coffee = input("What would you like? (espresso/latte/cappuccino): ")
        
        if make_coffee == 'report':
            report(reserves, money_inserted)
        elif make_coffee in recipes:
            recipe = recipes[make_coffee]
            missing = missing_ingredient(reserves, recipe)
            if missing:
                print(f"Sorry there was not enough {missing}")
            else:
                money_inserted = calculate_total(money)
                money_left = process_purchase(make_coffee, menu[make_coffee], money_inserted)
                if money_left is None:
                     continue 
                deduct_resources(reserves, recipe)
        elif make_coffee == 'stop':
            print("Machine has turned off")
            machine_on = False

coffee_machine()