'''
Password strenght checker
--------------------------------------------------------------
'''
import string,getpass 

def check_password_strength():
    password = getpass.getpass("Enter the password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = speacial_count = 0
    
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char  in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            speacial_count +=1
    
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength +=1
    if speacial_count >= 1:
        strength += 1
    
    if strength == 1:
        remarks =('That\'s a very bad password.'
                  'Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a week password.'
                   'Change it to something hard password')
    elif strength == 3:
        remarks = ("Your password is okay,but it can be improved")
    elif strength == 4:
        remarks = ("Your password is hard  to guess."
                   "but can be improved even more")
    elif strength == 5:
        remakrs = ("Now that\'s the password hard to crack it!!!!")
    print("Your password has:-  ")
    print(f'{lower_count} lower cases')
    print(f'{upper_count} uppercases')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{speacial_count} special charcaters')
    print(f"Password score: {strength /5}")
    print(f"Remraks: {remarks}")
    
def check_pwd(another_pw =False):
    valid = False
    if another_pw:
         choice = input('Do you want to check another password\'s strength (y/n)' )
    else:
        choice = input( 'Do you want to check your password\'s strength (y/n) : ')
    
    while not valid:
        if choice.lower() == 'y':
            return True 
        elif choice.lower() == 'n':
            print('Exiting...')
            return False 
        else:
            print("INVALID inputs!!!!")
if __name__ == "__main__":
    print("============== Welcome to password Strength Cheker ========================",end='\n')
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)
        
    