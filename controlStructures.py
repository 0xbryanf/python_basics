# 1. Conditional Statements
# a. If-Else Statements
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than 10")
    
    
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than or equal to 10")

# Ternary operator in If-Else statement
# condition_if_true ? value_if_true : value_if_false

x = print("x is greater than 10") if x > 10 else print("x is less than 10")

# For Loops
# For loops are used to iterate over a sequence (such as a list, tuple, or string) using an index.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
fruits = [{"fruit": "apple", "price": 2.5}, {"fruit": "banana", "price": 10}, {"fruit": "cherry", "price": 0}]
for fruitas in fruits:
    print(fruitas["fruit"])
    
# While Loops
# While loops are used to repeat a block of code until a specific condition is met.
x = 0
while x <= 10:
    print(x)
    x += 1

#Loop Variations
fruits = ["apple", "banana", "cherry", "manga"]
found_fruit = False

for fruit in fruits:
    if fruit == "manga":
        found_fruit = True
        print("manga found")

if not found_fruit:
    print("No Manga found")