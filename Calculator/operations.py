import os

def addition(first, second):
    """Adds two given numbers"""

    return first + second


def subtraction(first, second):
    """Subtracts two numbers"""

    return first - second


def multiplication(first, second):
    """Multiplies two numbers"""

    return first * second

def division(first, second):
    """Divides two numbers"""

    return first/second

def clear_screen():
    """Clears the screen"""

    os.system('cls' if os.name=='nt' else 'clear')