# Inner function can access the variables of outer function but outer function can't access the variables of inner function
def outer():
    a=100
    def inner():
        b=900
        print(a,b)
    inner()
    print(a) # ! print(b) #NameError: name 'b' is not defined
outer()
