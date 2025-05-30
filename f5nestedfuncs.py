# Greet Decorator printing the Name_Print function's content num times
def Greet(num):
    def Decorator(fx):
        def wrapper(a):
            for n in range(num):
                fx(a)
                print(f"{fx.__name__} is called {n+1} times")
        return wrapper
    return Decorator
@Greet(2)
def Name_Print(name):
    print(f"Hello Mr/Mrs.{name}")
Name_Print("Ram")

#behind the scene things:- below one is actual one (Above one is shortcut)
# ans=Greet(2)
# ans2=ans(Name_Print)
# ans2("Ram")

'''
Behind the scene things:-
ans=Greet(2)
ans2=ans(Name_Print)
ans2("Ram")
'''
