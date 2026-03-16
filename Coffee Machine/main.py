from requirements import *
from functions import *

machine_running = True


print("Please deposit coins")
resources['cash'] = calculate_money()

while machine_running:
    order = take_order()

    if order == "exit":
        print("Shutting down the machine. Goodbye! 👋")
        print(f"Here is the remaining change: ${resources['cash']}")
        machine_running = False
        break

    else:
        resource_sufficient = check_resource_sufficient(order)
        if resource_sufficient:
            make_coffee(order)


    while True:
        Continue = input("Do you wish to use the coffee machine again? ('y' for yes and 'n' for no)\n").lower()
        if Continue == 'y':
            break

        elif Continue == 'report':
            generate_report()


        elif Continue == 'n':
            print("Shutting down the machine. Goodbye! 👋")
            print(f"Here is the remaining change: ${resources['cash']}")
            machine_running = False
            break

        else:
            print("Please enter a valid prompt")
