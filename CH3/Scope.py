
# global scope

# local scope

a = "global"

# global function -- accessible anywhere
def spam():

    # local function -- only accesible within the 'spam()' function
    def recipes():
        print("pork")
        print("cheese")
        print("salt")
    
    recipes()


spam()
recipes()