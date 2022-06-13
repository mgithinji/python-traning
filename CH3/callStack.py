def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a() # run function 'a'

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def a_v2():
    
    print('a() starts')
    
    b()
        print('b() starts')
        c()
            print('c() starts')
            print('c() returns')
        print('b() returns')
   
    d()
        print('d() starts')
        print('d() returns')
    
    print('a() returns')