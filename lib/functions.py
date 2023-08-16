#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!") 

greet('Naureen')

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")  

greet_with_default()
greet_with_default('Sunny')

def add(num1, num2):
    sum = num1 + num2 
    return sum  

result = add(45, 55)
print(result)


def halve(number):
    if not isinstance(number, (int, float)):
        return None
    else:
        return number / 2 
