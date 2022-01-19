"""# Using for loop
for i in range(10):
    print(i, end=" ")
 # break the loop as soon it sees 6
    if i ==6:
        break
print()

# break the loop as soon it sees 6
"""
"""i = 0       
while i<10:
     # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        i+= 1
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end= " ")
    i+=1 
    """

# Python program to illustrate if-elif-else ladder

i = 20

if (i == 10):
    print("i is 10")
elif(i == 20):
    print("i is 20")
else:
    print("i is not present!!!")        