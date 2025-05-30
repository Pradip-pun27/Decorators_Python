import time
import os
def Decorator(fx):
    def New_Func(*args, **kwargs):
            print("Started to reading.")
            begin=time.time()
            fx(*args,**kwargs)
            print("Finished reading.")
            print(f"The time taken is {time.time()-begin:.4f} sec.");
    return New_Func
      
@Decorator
def File_Read(filename):
    if not os.path.exists(filename):
         print("Error:File not exist")
         return
    try:
        with open(filename,'r') as file:
            file.read()
    except Exception as e:
         print(f"Error reading file:{e}")

if __name__ =="__main__":       
    File_Read('file.txt');    

