# "88AA6B7"
# "88 AA 6B 7"

# "44GHC672981JD"
# "44 GH C6 72 98 1J D"

s = "44GHC672981JD"
res = ""

for i in range(0, len(s), 2):
    if i+1 > len(s): # if we're on the last character, and string is odd
        res = res + s[i]
    else:
        res = res + s[i:i+2] + " " # what is already there, plus the 2 characters, plus a space

print(res)

# range(start, stop, step) step = 2 -> 0, 2, 4, 6 instead of 0, 1, 2, 3, 4, ...

def split_by_n(s: str, n: int):
    length = len(s)
    result = ""

    for i in range(0, length, n):
        if i + (n-1) > length:
            result = result + s[i:]
        else:
            result = result + s[i:i+n] + " "
    
    return result

print(split_by_n(s, 2))