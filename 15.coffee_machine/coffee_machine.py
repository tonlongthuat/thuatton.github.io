MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":1
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
    "money":0
}

# print(MENU['espresso'])
def report(resources):
    water = resources['water']
    milk=resources['milk']
    coffee= resources['coffee']
    money= resources['money']
    print(f'water: {water}')
    print(f'milk: {milk}')
    print(f'coffee: {coffee}')
    print(f'money: {money}')

def drink_cost():
    quarters=int(input('how much quarters you want to process:  '))
    dimes=int(input('how many dimes you want to process:  '))
    nickles=int(input('how many nickles you want to process:  '))
    pennies=int(input('how many pennies you want to process:  '))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    
def check_transaction(coin_in,drink):
    if coin_in >= MENU[drink]['cost']:
        resources['money']= resources['money']+ MENU[drink]['cost']
        # coin_back=drink_cost-MENU[drink]['cost']
        # print(f'here is {coin_back} in change')
        return True
    else:
        print(f'sorry not enough coin, here is your coin  {coin_in} ,please insert again')
        return False

def make_coffee(resources):
    turn_on=True
    while turn_on:
        drink=input('What would you like? (espresso/latte/cappuccino) or type off to turn off:  ')
        if drink == 'espresso'or drink == 'latte' or drink == 'cappuccino' or drink == 'off' or drink == 'report':
            pass
        else:
            continue    
        if drink == 'off':
            break
        if drink == 'report':
            report(resources)
            break
        water=MENU[drink]['ingredients']['water']
        milk=MENU[drink]['ingredients']['milk']
        coffee= MENU[drink]['ingredients']['coffee']
        coin_in=drink_cost()
        # check_transaction(coin_in,drink)
        if check_transaction(coin_in,drink) == True:
            if water > resources['water'] or milk > resources['milk'] or coffee > resources['coffee']:
                turn_on=False
                print("we don't have enough sufficient")
                print(f"here is your coin  {coin_in}")
            else:
                coin_back=coin_in - MENU[drink]['cost']
                resources['water'] = resources['water'] - water
                resources['milk'] = resources['milk'] - milk
                resources['coffee'] = resources['coffee'] - coffee
                print('here you are')
                print(f'here is {coin_back} in change')
                if input('do you want more (y/n):  ') == 'y':
                    turn_on=True
                else:
                    turn_on=False


# n=input('What would you like? (espresso/latte/cappuccino):  ')
make_coffee(resources)

