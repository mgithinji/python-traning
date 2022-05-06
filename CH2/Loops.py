
print ("For Loop of numbers printing")
for i in range(1, 10):
    print(i)


print("While Loop alternative")
i=-2
while i<10:
    print(i)
    i = i+1

print("\nDemonstrating the break and continue statements")

print("printing from 1 to 9, break at 7")
for i in range(1, 10):
    if i == 7:
        break
    print(i)

print("printing from 1 to 9, continuing (skip) at 7")
for i in range(1, 10):
    if i == 7:
        continue
    print(i)

print("printing from 1 to 9, continuing (skip) at 7")
for i in range(1, 10):
    if i in (3,5,7):
        continue
    print(i)

# alternative to the 'in' statement
# print("printing from 1 to 9, continuing (skip) at 3,5,7")
# for i in range(1, 10):
#     if i==3 or i==5 or i==7:
#         continue
#     print(i)