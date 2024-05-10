testlst = ['T1-20-30',
           'T2-60-60',
           'T3-30-30',
           'T4-30-35'
           ]

for elm in testlst:
    t1,m1,m2 = elm.split("-")
    if int(m1)==int(m2):
        print('equal test =',t1)
    else:
        print('unequal test =',t1)
