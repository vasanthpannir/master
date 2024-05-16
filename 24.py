stab = {'arun':['math',60,'sci',70,'sco',80],
        'Vasanth':['math',80,'sci',60,'sco',50],
        'Ajay':['math',30,'sci',33,'sco',30],
        'Sunil':['math',20,'sci',10,'sco',40]
        }
name = input("Enter the name:\n").lower()
if name in stab:
    marks = sum(stab[name][1::2])
    avg = marks/3
    print(marks,avg)
else:
    print("not found")


