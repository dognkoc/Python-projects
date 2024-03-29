MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False 
    
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}")

    elif choice == "espresso":
        if resources["water"]>=50 and resources["coffee"]>=18:
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            change= quarters*0.25+dimes*0.1+nickles*0.05+ pennies*0.01
            
            if change>=1.5:
                money +=1.5
                resources["coffee"] -=18
                resources["water"] -=50
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: {money}")
                print(f"Change amount is {round(change,3)}")
                print(f"Here is your {choice}. Enjoy!")            

            else:
                print("Sorry that's not enough money. Money refunded.")
                print(change)

        elif resources["water"]<50 and resources["coffee"]>=18: 
            print("Sorry there is no enough water.")
        elif resources["water"]>=50 and resources["coffee"]<18:
            print("Sorry there is not enough Coffee.")
    
    elif choice == "latte":
        if resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"]>=150:
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            change= quarters*0.25+dimes*0.1+nickles*0.05+ pennies*0.01
            if change>=2.5:
                money +=2.5
                resources["coffee"] -=24
                resources["water"] -=200
                resources["milk"] -=150
                print(f"Water: {resources['water']}ml")
                print(f"Milk: {resources['milk']}ml")
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: {money}")
                print(f"Change amount is {round(change,3)}")
                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
                print(change)

        elif resources["water"]<200 and (resources["coffee"]>=24 or resources["milk"]>=150): 
            print("Sorry there is no enough water.")
        elif resources["coffee"]<24 and (resources["water"]>=200 or resources["milk"]>=150):
            print("Sorry there is not enough Coffee.")
        elif (resources["water"]>=200 or resources["coffee"]>=24) and resources["milk"]<150:
            print("Sorry there is not enough milk.")       
        
    elif choice == "cappuccino":
        if resources["water"]>=250 and resources["coffee"]>=24 and resources["milk"]>=100:
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            change= quarters*0.25+dimes*0.1+nickles*0.05+ pennies*0.01 -3
            if change>=3:
                money +=3
                resources["coffee"] -= 24
                resources["water"] -= 250
                resources["milk"] -= 100
                print(f'Water: {resources["water"]}ml')
                print(f'Milk: {resources["milk"]}ml')
                print(f"Coffee: {resources['coffee']}g")
                print(f"Money: {money}")
                print(f"Change amount is {round(change,3)}")
                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")
                print(change)

        elif resources["water"]<250 and (resources["coffee"]>=24 or resources["milk"]>=100): 
            print("Sorry there is no enough water.")
        elif resources["coffee"]<24 and (resources["water"]>=250 or  resources["milk"]>=100):
            print("Sorry there is not enough Coffee.")
        elif (resources["water"]>=250 or resources["coffee"]<24) and resources["milk"]<100:
            print("Sorry there is not enough milk.")