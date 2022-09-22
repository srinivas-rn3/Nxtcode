#1. Learning of Funcation
#2. Learning of Dictionaries
#3. Learning of Tuples
##############
# Funcations #
##############
'''
def calculate_exp(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

joe_exp_list = [100,200,400,800]
bee_exp_list = [230,450,150,800]

joe_exp = calculate_exp(joe_exp_list)
bee_exp = calculate_exp(bee_exp_list)

print("Joe's expenses are : ", joe_exp)
print("Bee's expenses are : ", bee_exp)
'''
'''
total = 0
def sum(a,b=0):
    print("a:" ,a)
    print("b:" ,b)
    total = a+b
    print("total inside the functions:", total)
    return total
s = sum(109,3444)
print("total outside the functions:",total)
'''
'''
def print_pattern(n):

    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)  
pat= print_pattern(100)
print(pat)
'''
#################
#  Dictionaries #
#################

d = {'zozo':894774747890,'bee':908462738361,"klara":67839495915}
print(d)
d['rose']=567838234
#print(d)
#del d['klara']
#for key in d:
#    print("Key:",key, "value is:",d[key] )
##print(d)
#for k,v in d.items():
#    print("key is:", k ,"value is :",v)

#print("zozo"in d)
#d.clear()
#print(d)

##########
# Tuples #
##########
point = (4,5)
print(point[0])
print(point[1])
#https://www.youtube.com/watch?v=DdGVBZv46PI&ab_channel=codebasics