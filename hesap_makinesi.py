from audioop import mul
from decimal import DivisionByZero
from time import sleep

#instead of using math module I will be trying to use functions...

print("""

        ***********************************
        *                                 *
        *                                 *
        *      Welcome to Calculator      *
        *                                 *
        *                                 *
        ***********************************


    """)

def summation(number_1,number_2):
        return number_1+number_2

def extraction(number_1,number_2):
        return number_1-number_2

def multiplication(number_1,number_2):
        return number_1*number_2

def division(number_1,number_2):
        return number_1/number_2

def factorial(number):
        if number<=1:
                return 1
        return number*factorial(number-1)

while True:
        try:

                sleep(0.1)
                transaction_choice = input("""Please choose one of the following transactions: 
                
                
        List of Transactions
        
        1. Summation
        2. Extraction
        3. Multiplication
        4. Division
        5. Factorial
        6. Finish

        your choice: """)
                if (transaction_choice=='finish'):
                        sleep(0.5)
                        print("Calculator is closed!")
                        break

                elif (transaction_choice == 'summation'):
                        print("You chose summation")
                        sleep(0.5)
                        number_1 = int(input("Please type a number: "))
                        number_2 = int(input("Please type another number: "))
                        sleep(0.5)
                        print(f"The result of summation: {summation(number_1,number_2)}")
                        print('*'*50)
                
                elif (transaction_choice == 'extraction'):
                        print("You chose extraction")
                        sleep(0.5)
                        number_1 = int(input("Please type a number: "))
                        number_2 = int(input("Please type another number: "))
                        sleep(0.5)
                        print(f"The result of extraction: {extraction(number_1,number_2)}")


                elif (transaction_choice == 'multiplication'):
                        print("You chose multiplication")
                        sleep(0.5)
                        number_1 = int(input("Please type a number: "))
                        number_2 = int(input("Please type another number: "))
                        sleep(0.5)
                        print(f"The result of multiplication: {multiplication(number_1,number_2)}")
                        

                elif (transaction_choice == 'division'):
                        print("You chose division")
                        sleep(0.5)
                        number_1 = int(input("Please type a number: "))
                        number_2 = int(input("Please type another number: "))
                        sleep(0.5)
                        if number_2 == 0:
                                raise DivisionByZero("Number cannot divided by zero")
                        print(f"The result of division: {division(number_1,number_2)}")
                        

                elif (transaction_choice == 'factorial'):
                        print("You chose factorial")
                        sleep(0.5)
                        number_1 = int(input("Please type a number: "))
                        sleep(0.5)
                        print(f"{number_1} factorial is: {factorial(number_1)}")

        except Exception as e:
                print(e)