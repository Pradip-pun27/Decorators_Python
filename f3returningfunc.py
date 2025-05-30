#Returning value as a  function to caller
def Func():
    def inner():
        print("Gdm Guys")
    return inner
f=Func()
f()
print(f"Actual Name of f is {f.__name__}") # f is actually a inner named function which is returned by Func function
