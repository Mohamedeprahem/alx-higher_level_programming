#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number <0:
last number = number %-10
if number >0:
last number = number %10
if last number > 5:
print(f"Last digit of {number}is {last number} greater than 5")
elif last number == 0:
print(f"Last digit of {number} is {last number} and is 0")
else
print(f"Last digit of {number} is {last number}is less than 6 and not 0")
