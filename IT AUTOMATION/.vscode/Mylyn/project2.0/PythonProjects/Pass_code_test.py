
import getpass,string 
password = getpass.getpass("Enter the password:")
strength = 0
remarks = ''
upper_count = lower_count = num_count = wspace_count = special_count = 0
for char in list(password):
    if char in string.ascii_lowercase:
        lower_count += 1
    elif char in string.ascii_uppercase:
        upper_count += 1
    elif char in string.digits:
        num_count += 1
    elif char in  ' ':
        wspace_count += 1
    else:
        special_count += 1
'''
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
'''
print(f"Lower count is : {lower_count}")
print(f"uppper count is : {upper_count}")
print(f"Special count : {special_count}")
print(f"White spaces : {wspace_count}")
print(f"Strength is: {strength}")
print(f"strength of pass score is: {strength/5} ")
#if __name__ == "__main__":
    
    