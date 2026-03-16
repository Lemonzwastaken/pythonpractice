while True:
    try:
        pennies = int(input("Please enter the quarters you have(Worth $0.25): "))
        dimes = int(input("Please enter the dimes you have(worth $0.10): "))
        nickels = int(input("Please enter the nickels you have(worth $0.05): "))
        pennies = int(input("Please enter the pennies you have(worth $0.01): "))
        break
    except ValueError:
        print("Enter a proper value\n")

total = 0.25*pennies + 0.10*dimes + 0.05*nickels + 0.01*pennies
print(total)