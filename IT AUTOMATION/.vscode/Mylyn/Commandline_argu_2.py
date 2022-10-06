import argparse as a

p = a.ArgumentParser()
p.add_argument("--str1", help ="Enter the string1")
p.add_argument("--str2", help = "enter the string2")
p.add_argument("--case",help ="enter the case", choices=["upper","lower"])
args = p.parse_args()

s1 = args.str1
s2 = args.str2
print("Before conversion: " , end ='\n')
print(s1)
print(s2)
if args.case == "upper":
    print("Converted string to 'upper' case:", end = "\n")
    print("str1:",s1.upper())
    print("str2 :",s2.upper())

elif args.case == "lower":
    print("Converted string to 'lower' case:", end = "\n")
    print("str1: ",s1.lower())
    print("str2: ",s2.lower())
