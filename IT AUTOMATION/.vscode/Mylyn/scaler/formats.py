#Format in Python
#https://www.scaler.com/topics/format-in-python/
#Converting A decimal number to binary number
#val = 36
#binary_val = format(val,'b')
#print(binary_val)
#format(value, format_spec)
#The format() function returns a formatted representation of 
# the given value as per the format specifier. The return value is always a string, irrespective of the input.'
'''
val =12 #original value
print("orginal value(Decimal):")
print(val)
print()
#Binary value
print("Binary value:")
print(format(val,'b'))
print()
#Octane value
print("Octal value:")
print(format(val,'o'))
print()
print("Hexadecimal value:")
print(format(val,'x'))
'''
#print(format(4453,"*>+7,d"))
#print(format(933.3629,"^-09.3f"))
#Example 3: Using format() by Overriding __format__()
'''
class car:
    def __format__(self,format):
        if(format == 'colour'):
            return 'Red'
        return 'None'
print(format(car(), 'colour'))
'''
#txt = "Pizza  for {:.2f} dollars!"
#print(txt.format(20))
#print("everyone likes {}".format("pizza"))
'''
#my_string ="People who like {} also like {} with {}"
#print(my_string.format('pizzas','pasta','garlic bread'))
## Demonstrating the use of positional arguments in string format method.
my_string ="People who like {0} also like {1} with {2}."
print(my_string.format('Pizzas','Pasta','Garlic Bread'))
## Using positional arguments to change the default order of values.
my_string ="People who like {1} also like {0} with {2}."
print(my_string.format('Pizzas','Pastas','Garlic Bread'))
'''
#Here is an example of Keyword arguments in the str.format() method:

#my_string ="People who like {food1} also like {food2} with {food3}"
#print(my_string.format(food1 = "Pizzas",food2="Salad",food3 ="Garlic bread"))

#Both Keyword arguments and Positional arguments can also be used together.
#my_string ="People who like {0} also like {1} with {food3}"
#print(my_string.format("Pizzas","Salads",food3='Garlic Bread'))

#Converting decimal into binary in string format: Code:
#my_strings = "{:d} in binary= {:b}"
#print(my_strings.format(22,22))

#Limiting the number of decimal points in a floating integer: Code:
#my_string = "{:f} in 3 decimal  points ={:.3f}"
#print(my_string.format(43.23345,43.23354))
#print(my_string.format(43.54213, 43.54213))
my_string = "The AQI  in {0:10} today is {1:.2f}"
print(my_string.format('Delhi',450))

my_string = "The AQI  in {0:>10} today is {1:d}"
print(my_string.format('Delhi',450))
#When handling and displaying data, organizing the data for easy reading, accessing,
# and management is always preferable. Formatters can help organize the data using align, sign, and width specifiers.

for i in range(1,10):
    print("{}-{}-{}".format(i , i*i, i*i*i))

for i in range(1,11):
    print("{:<5d}{:<5d}{:<5d}".format(i,i*i,i*i*i))