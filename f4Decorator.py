def Decorator(fx):
    def wrapper(*args,**kwargs):
        print("Starting")
        fx(*args,**kwargs)
        print("Ended\n")
    return wrapper
@Decorator
def print_name():
    print("Hello")
print_name()

'''
(behind the scene)Actual one (Above one is shortcut) is below:
ans=Decorator(print_name)
ans()
'''
@Decorator
def add(n1,n2):
    print(f"Sum is {n1+n2}")
add(11,14)

#This below one is actual one (Above one is shortcut)
# def add(n1,n2):
#     print(f"Sum is {n1+n2}")
# ans=Decorator(add)
# ans(11,14)

