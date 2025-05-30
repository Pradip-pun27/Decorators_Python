num=0
#Decorator function 
def Decorator(f):
    def wrapper(*args):
        print("Hello!")
        f(*args)
        print("Glad to see u.\n")
    return wrapper
    
class Std:
    def __init__(self,name,age):
        self.n=name
        self.a=age
        
    @Decorator    
    def Display_Info(self):
        print(f"{self.n} you are {self.a} years old.")

while True:
    num=num+1
    Name=input("Enter Name of a std:")
    Age=int(input("What's Age?:"))
    s1=Std(Name,Age)
    s1.Display_Info()
    if(num==4):
        break

