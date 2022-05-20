# <function_name> (<args>)

# f(x) = x^2
# f(2) = 4

# h(x) = x^3 + 2x
# h(2) = 12

# g(x) = f(x) + h(x)
# g(2) = 16

def f(x:int) -> int:
    res = x**2
    return res

def h(x):
    res = (x**3) + (2*x)
    return res

def g(x):
    res = f(x) + h(x)
    return res

def g(x):
    res = (x**2) + ((x**3) + (2*x))
    return res

f(2)
h(2)
g(2)

# print(f(2))
# print(h(2))
# print(g(2))