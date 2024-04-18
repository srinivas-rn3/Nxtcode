'''
This code defines a function mask_string that replaces each character in the input 
string with an asterisk (*). The unmask_string function then reveals characters
from the original string based on the positions of asterisks in the masked string.
'''

def mask_string(input_string):
    masked_string = '*' * len(input_string)
    return masked_string 

def unmasked_string(masked_string,original_string):
    unmasked_string = ''
    for i in range(len(masked_string)):
        if i < len(original_string):
            if masked_string[i] == '*':
                unmasked_string += original_string[i]
            else:
                unmasked_string  += masked_string[i]
    return unmasked_string

original = "srinivas.rn"
masked = mask_string(original)  
print("Masked Data:",masked)

# Simulating obscured input, e.g., from a password input field
obscured_data = "*****************"
unmasked = unmasked_string(masked,original)
print("Unmasked Data:",unmasked)