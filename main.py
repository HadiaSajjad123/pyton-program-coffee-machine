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
profit=0;
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry you don't have enough {item}")
            return False
    return True
        

def process_coins():
    """this function returns the total from inserted coins"""
    
    print("Please insert coins:")
    total=int(input("How many quarters?\n")) * 0.25
    total+=int(input("How many dimess?\n")) * 0.1
    total+=int(input("How many nickels?\n")) * 0.05
    total+=int(input("How many pennies?\n")) * 0.01
    return total

def is_transaction_successful(money_recieved,drink_cost):
    """Returns True when payment is accepted or returns False when money is insufficient"""
    
    if money_recieved >= drink_cost:
        change= round(money_recieved - drink_cost ,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money Refunded")
        return False
    
    
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources  """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}")
    
    
is_on=True
while is_on:
    user_choice=input("What would you like (Espresso,Latte,cappuccino)?\n").lower()
    if user_choice=="off":
        is_on=False
    elif user_choice=="report":
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']} ml")
        print(f"coffee:{resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink=MENU[user_choice]
        if is_resource_enough(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
            
        