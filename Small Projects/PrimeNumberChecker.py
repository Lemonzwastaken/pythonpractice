def is_prime(num):
    numbers_divisible = 0
    for number in range(1,100):
        if num%number == 0:
            numbers_divisible+=1
        
    if numbers_divisible == 2:
        print("True")
    else:
        print("False")
    
is_prime(int(input("Please enter the number you wish to check\n")))