'''
import sys
san1 = sys.argv[1]
common_name = 'microfocus1.com'
if san1 == '' or san1 == " ":
     san1 = common_name
     print(san1)
else:
     san1 = san1.split(',')
     print(san1)
'''
'''
lists = ['Vegges','Bread','Fruits','Flowers']
print(lists)
lists.append("oil")
print(lists)
lists.insert(2, "Oats")
print(lists)
bathroom = ["Shampoo","Soap","Dettol"]
print(bathroom)
new_list = lists+bathroom
print(new_list)
print(len(new_list))
print('Soda' in new_list)
'''
'''
num = input("Enter the No.")
num = int(num)
if num%2 == 0:
     print("Given Number is", num )
     print("And it's Even")
else:
     print("Given number is", num)
     print("And it's odd")
'''
'''
indian = ["Samosa","Daal","Bhel Puri"]
chinese = ["Fried Rice", "Rolls","Fried veg"]
italian = ["Pizza","Pasta","risotto"]
print("Enter the dish name ... Based on that we will identify cuisine type.")
print(" ")
dish = input("Enter your Dish:")

if dish in indian:
     print("Given Dish is Indian:", dish)
elif dish in chinese:
     print("Given DIsh is Chinese:", dish)
elif dish in italian:
     print("Given Dish is Italian:", dish)
else:
     print("Given Dish is not sure of the cuisine:", dish)
'''

from ast import Continue


exp = [2350,2500,2700,2890,3010]
'''
#total = exp[0]+exp[1]+exp[2]+exp[3]
total =0 
for i in exp:
     total=total+i
print("Grand Total is expenses is :" ,total)

'''
'''
for i in range(1,11):
     print(i)
     print("square root of ",end='\n')
     print(i*i)
'''
'''
total = 0
for i in range(len(exp)):
     print("Month:",(i+1),'Expense:',exp[i])
     total = total+exp[i]
print("Grand total is :", total)
'''
'''
#break
key_location = ["chair","living room","closet","car","garage","starbucks"]
location  = "garage"
for i in key_location:
     if i == location:
          print("Key found in:",i)
          break
     else:
          print("Key is not found in:",i)
'''
'''
#continue
for i in range(1,11):
     if i%2==0:
          continue
     print(i*i)
'''
#while
i=5
while i<=5:
     print(i)
     i=i+1
#https://www.youtube.com/watch?v=3ykIpmAxdoY&ab_channel=codebasics