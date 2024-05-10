testlst = ['T1-20-30',
           'T2-60-60',
           'T3-30-30',
           'T4-30-35'
           ]
for elm in testlst:
    elm = elm.split(',')[0].split("-")[1:]
    if elm[0] == elm[1]:
        print("equal Test")
    else:
        print("unequal Test")
