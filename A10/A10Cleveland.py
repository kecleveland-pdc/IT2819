def outer_function():

    def inner_function():
        a = 30
        print ('a =',a)
    
    inner_function()

    a = 20
    print('a =',a)
   
a = 10
outer_function()
print('a =',a)

    
