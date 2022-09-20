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
#https://www.youtube.com/watch?v=hNddJ3_hahk&ab_channel=codebasics