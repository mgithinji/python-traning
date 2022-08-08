# data types: string, float, int, bool

name = "Chimdi" # string
age = 26 # int
weight = 160.5 # float
male = True # bool

# common python data structures: variable, dictionaries, tuples, sets, lists

# variable -> one element
# dictionary -> hold multiple elements that are indexed by keys
# list -> hold multiple elements indexed by value

classmates = ['Ugonna', 'Chimdi', 'Morgan', 'John']

firstclassmate = classmates[0] # get value in list by indexing

name1 = "Ugonna"
name2 = "Chimdi"
name3 = "Morgan"
name4 = "John"

for n in classmates:
    print(n)

for i in range(3):
    if i == 0:
        print(name1)
    elif i == 1:
        print(name2)
    elif i == 2:
        print(name3)
    elif i == 2:
        print(name4)

print(name1)
print(name2)
print(name3)
print(name4)

