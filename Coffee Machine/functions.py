from requirements import *
import time
import os
from art import *

def generate_report():
    """Generates report of the remaining cash, coffee, water and milk left in the machine"""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    cash = resources['cash']


    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${cash}")

def calculate_money():
    """Takes the number of pennies, dimes, nickels and quarters and converts them into dollars"""

    while True:
        try:
            quarters = int(input("Please enter the quarters you have(Worth $0.25): "))
            dimes = int(input("Please enter the dimes you have(worth $0.10): "))
            nickels = int(input("Please enter the nickels you have(worth $0.05): "))
            pennies = int(input("Please enter the pennies you have(worth $0.01): "))
            os.system('cls' if os.name=='nt' else 'clear')
            break
        except ValueError:
            print("Enter a proper value\n")

    total = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    return total

def check_resource_sufficient(drink):
    """Checks if the order made by the user is resource sufficient as per the machine"""

    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
            print("Im sorry this order cannot be processed due to lack of resources")
            return False
        
        else:
            return True

def make_coffee(drink):
    """Makes the coffee while depleting resources"""

    if MENU[drink]['cost'] <= resources['cash']:

        resources['cash'] -= MENU[drink]['cost']
        round(resources['cash'], 2)
        for ingredient in MENU[drink]['ingredients']:

            resources[ingredient] -= MENU[drink]['ingredients'][ingredient]

        print("Dispensing Beverage.........☕")
        time.sleep(10)
        os.system('cls' if os.name=='nt' else 'clear')
        print("Dispensed")
        print(coffee)
        print("Enjoy your coffee \n")

    else:
        print("We cannot process this change ")


def take_order():
    print(logo)
    while True:
        try:
            print(f"Available balance: ${resources['cash']}")
            order = input(f"Available Drinks\n"
                          f"Espresso(1), Cost = ${MENU['espresso']['cost']}\n"
                          f"Latte(2), Cost = ${MENU['latte']['cost']}\n"
                          f"Cappucino(3), Cost = ${MENU['cappuccino']['cost']}\n"
                          "Please enter what you would wish to have: ")

            if order.lower() == "exit":
                return "exit"
            if order.lower() == "report":
                generate_report()

            order = int(order)
            
            if order > 3 or order < 1:
                print("Please enter a value between 1 to 3\n")

            elif order == 1:
                return 'espresso'
            elif order == 2:
                return 'latte'
            elif order == 3:
                return 'cappuccino'

        except ValueError:
            print("Please enter a numeric value from 1 to 3\n")