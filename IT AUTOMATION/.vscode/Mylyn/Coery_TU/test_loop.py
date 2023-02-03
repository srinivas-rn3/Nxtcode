emp_str_1 = 'Srini-R-80000'
emp_str_2 = 'Nezuko-Chan-86000'
emp_str_3 = 'Tanjiro-Chan-90000'
l1 = ['Srini-R-80000', 'Nezuko-Chan-86000','Tanjiro-Chan-90000']
for i in l1 :
    first,last,pay = i.split('-')
    print(first,last,pay)