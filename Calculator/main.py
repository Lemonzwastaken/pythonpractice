from operations import *
from art import *

logo(status="startup", number=None, operative=None)
calc_running = 0
operation = None

while True:  
    try:
        first_number = int(input("What is your first number: "))
        calc_running = True
        break
    except ValueError:
        print("Please enter an int value")
    

while calc_running:
    try:
        second_number = int(input("What is your second number: "))
        try:
            operation = int(input("Which operation would you like to perform" \
            "\nAddition(1)" \
            "\nSubtraction(2)" \
            "\nMultiplication(3)" \
            "\nDivision(4)\n"
            "\nSelection: "))


            if operation == 1:
                first_number = addition(first=first_number, second=second_number)
                operation = "+"
            elif operation == 2:
                first_number = subtraction(first=first_number, second=second_number)
                operation = "-"
            elif operation == 3:
                first_number = multiplication(first=first_number, second=second_number)
                operation = "x"
            elif operation == 4:
                first_number = division(first=first_number, second=second_number)
                operation = "%"
            
            logo(number=first_number, status=calc_running, operative=operation)

            conti = input("Do you wanna still continue using the calculator?(Enter anything for yes, EXIT for no)\n").lower()
            
            if conti == "exit":
                calc_running = False
            else:
                clear_screen()
                logo(number=first_number, status=calc_running, operative=operation)



        except ValueError:
            print("Please enter a proper value")
    except ValueError:
        print("Please enter an int value")

logo(number=first_number, status=calc_running, operative=operation)
