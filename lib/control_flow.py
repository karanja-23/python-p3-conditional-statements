#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin"or username == "ADMIN") and password == "12345":
        return "Access granted"

    pass
print(admin_login("admin", "12345"))
print(admin_login("sudo", "12345"))
print(admin_login("ADMIN", "12345"))
def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"
    pass

print (hows_the_weather(33))
print (hows_the_weather(99))
print (hows_the_weather(75))

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz" 

    else:
        return num
    pass
print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(15))

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else :
        print("Invalid operation!")
        return None    
    pass
print (calculator("+", 1, 1))
print(calculator("-", 3, 1))
print (calculator("*", 3, 2))
print(calculator("/", 4, 2))
print (calculator("nope", 4, 2))
