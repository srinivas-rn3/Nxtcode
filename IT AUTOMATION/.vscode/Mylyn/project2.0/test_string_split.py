'''
s = 'srini'
for i in s:
    print(i,end=',')
print(len(s),end='\n')
'''
'''
def ascii(str1):
  input_string = str1
  ascii_values = [ord(char) for char in input_string]
  print(ascii_values)
ascii("srinivas")
'''
input_str = "Srinivas"
ascii_st = ""
for char in input_str:
    ascii_st += str(ord(char)) + " "
    
    
print(ascii_st) 