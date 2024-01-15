import string 
def call_str(str1,choice):
    if choice =="Upper":
        print(str1.upper())
    elif choice == "Lower":
        print(str1.lower())
    elif choice =='Count':
        print("lenght of the string {} is {}".format(str1,len(str1)))
    elif choice == 'Split':
        print("String spiting is:",end="\n")
        for i in str1:
            print(i,end=" ")
    elif choice == 'ascii':
        ascii_values = [ord(c) for c in str1]
        print(ascii_values)
        
    else:
        print("Invalid choice!!!")

if __name__=="__main__":
    print("Convert string to uppercase,lower,count,split,and ,ascii based on user the choice.",end="\n")
    user_str = input("Enter the string:")
    options = ["Upper","Lower","Count","Split","ascii"]
    for i,option in enumerate(options):
        print("{}.{}".format(i+1,option)) 
    choice = input("Enter the choice: ")
    if choice in['1','2','3','4','5']:
        op = options[int(choice)-1]
        print("You have selected the option {}".format(op))
        call_str(user_str,op)
    else:
        print("Invalid Input!!!")
    