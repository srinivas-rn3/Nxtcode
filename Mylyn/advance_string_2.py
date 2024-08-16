"""
Advanced Usage of string.Template
Custom Delimiters:You can create a subclass of Template to use custom delimiters instead of $.
This can be useful in scenarios where $ is already used frequently in the text.
"""
from  string import Template

class Customtemplate(Template):
    delimiter = '%'

template = Customtemplate("Hola , my name is %name and I'm from %place")
result =  template.substitute(name = "Rosila", place='Spain')
print(result)

'''
Escaping Special Characters:

If you need to include a $ character in the template string without it being treated as a placeholder, you can escape it using $$.
'''
template1 = Template("This is $$10")
result1 = template1.substitute()
print(result1)


'''
Combining with Other String Methods:

You can use Template alongside other string manipulation methods for more complex formatting needs.
'''

price = f"{0.5:.2f}"
template2 = Template("Item: $item | Price: $$${price}")
result2 = template2.substitute(item='Kiwi',price=0.5)
print(result2)

#Changing Delimiter Without Subclassing
# Original template string with custom delimiter (%)
template_str = "Hola, my name is ||name and I'm from ||place"

# Replace || with $ to match the default Template syntax
temp = template_str.replace('||','$')
# Create a Template object and substitute the values
tem = Template(temp)
r = tem.substitute(name='Rosila',place = 'Spain')
print(r)