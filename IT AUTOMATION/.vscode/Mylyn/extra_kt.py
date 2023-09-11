'''
x = 5 
y = 10
x ,y = y,x 
print("After Swappping values of x and y are",x,y)
'''
'''
__name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
__name__ is a built-in variable which evaluates to the name of the current module. 
'''
'''
import os
print("File__name__=%s"%__name__)
if __name__ == '__main':
    print("file is being run directory")
else:
    print(" File1 is being imported")
print(os.path.basename(__file__))
import sys  
print(sys.argv[0])
'''
from dataclasses import dataclass 
@dataclass 
class shop:
    product: str
    category1 : str
    quantity : int=0
    cost_per_unit : int=0
    #total_cost :int=0

    def gst_shop(self):
        total_cost=  self.quantity * self.cost_per_unit
        print("total cost of prodcts is {0}".format(f"{total_cost:,}"))
elx = shop("Iphone","mobile",1300,100000)
print(elx)
total_x = elx.gst_shop()

