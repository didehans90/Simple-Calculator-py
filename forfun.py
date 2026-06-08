import time
import random

def slow_print(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.03)

    print()

slow_print("Calculator Test - By Karl")
time.sleep(2)
numbers1 = float(input("Add first number: "))
time.sleep(1)
numbers2 = float(input("Add second number: "))
time.sleep(2)
slow_print("Select mode: [Add +] | [Subtract -] | [Multiply *] | [Divide /]")
time.sleep(1)
operators = input("> ")

# addition = numbers1 + numbers2
# subtracting = numbers1 - numbers2

if operators == "+":
    slow_print(f"Result is: {numbers1 + numbers2}")

elif operators == "*":
    slow_print(f"Result is: {numbers1 * numbers2}")

elif operators == "/":

    if numbers2 == 0:
        slow_print("Nuh uh, you can't divide it by zero")

    else:
        slow_print(f"Result is: {numbers1 / numbers2}")

elif operators == "-":
    slow_print(f"Result is: {numbers1 - numbers2}")

else:
    slow_print("Clear")