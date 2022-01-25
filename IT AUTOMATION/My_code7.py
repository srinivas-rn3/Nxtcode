#Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
print("Srini master1 \n mastr2 lock is underhood")
'''end= ” ” statement
The end keyword is used to specify the content that is to be printed at the end of the execution 
of the print() function.By default, it is set to “\n”, which leads to the change of 
line after the execution of print() statement.
print("We are in planet Arcus!!!!")
print("Planet of dune attached by taskens", end="***")
print("send Parabrigade134")'''

'''Imagine you are building a countdown timer, which appends the 
remaining time to the same line every second. It would look something like below:
3>>>2>>>1>>>Start'''
import time
count_second = 3 
for i in reversed(range(count_second + 1)):
     if i > 0:
         print(i, end='>')
         time.sleep(1)
     else:
         print('Start')