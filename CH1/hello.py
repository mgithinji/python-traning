# Python program that asks for your information and generates a report.
# Concepts: print(), input(), len(), str.format(), data types, operations, special string characters (\n, \t, \r)

print("Hello! This program asks for your information and generates a report.")

print("What is your first and last name?")
name = input()
name = name.upper()

print("How old are you?")
age = input()

print("How much do you weigh, in pounds?")
weight_lb = input()
weight_kg = float(weight_lb) * 0.4536

# generating user report
print("\n")
print("This is a report for " + name)
print("This is a report for {}".format(name))
print("\n")

print("Age:\t" + name + " is " + age + " years old.")
print("Age:\t{} is {} years old.".format(name, age))

print("Weight:\t{} weighs {} lbs, {} kg".format(name, weight_lb, weight_kg))
print("Weight:\t{n} weighs {w_lb} lbs, {w_kg} kg".format(w_lb=weight_lb, w_kg=weight_kg, n=name))