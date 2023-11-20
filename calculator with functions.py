#CALCULATOR
import os

sky_is_blue = True   



def Multiplication(a, b):   #multiplication function
    product = a * b
    return product

def Addition(a, b):         #addition function
    summation = a + b
    return summation

def Modulus(a,b):           #for modulus
    remainder = a % b
    return remainder

while sky_is_blue:      #while loop for whole function to keep iterating
    print("-------------SUICALC--------")
    print("Please choose")
    print("1. Addition")
    print("2. Mulitplication")
    print("3. Modulus")


    choice = int(input("Enter choice: "))
    os.system('cls')



    while choice > 3 or choice < 1: #while loop to reprompt user incase of invalid entry
        choice = int(input('Please enter value 1-3: '))
            

    if choice == 1:
        a = int(input("Enter first no.: "))
        b = int(input("enter second no.: "))
        answer = Addition(a, b)
        print(answer)
    elif choice == 2:
        a = int(input("Enter first no.: "))
        b = int(input("enter second no.: "))
        answer = Multiplication(a, b)
        print(answer)
    elif choice == 3:
        a = int(input("Enter first no.: "))
        b = int(input("enter second no.: "))
        answer = Modulus(a, b)
        print(answer)

    continu = input('Continue calc, y or n: ')  #prompt user if he wants to continue playing
    if not continu == 'y':
            sky_is_blue = False 
print('Thanks for playing')