def Decorator(fx):
    def wrapper(*args,**kwargs):
        print("Starting")
        ans = fx(*args,**kwargs)
        print("Ended")
        return ans
    return wrapper


@Decorator
def add(n1,n2):
    print("Adding 2 nums")
    return n1+n2;
print(f"The Sum is : {add(11,14)}")

#This below one is actual one (Above one is shortcut)
'''
def add(n1,n2):
    print(f"Sum is {n1+n2}")
ans=Decorator(add) # This Decorator function returned Wrapper function 
result=ans(11,14) # This ans is Wrapper named function ans it also returned some value(Sum of 11 +14)
print(f"The Sum is :{result}")
'''

