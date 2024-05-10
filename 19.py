plst = ['e1-10,20,30-30,60,10',
        'e2-60,80,50-10,20,30',
        'e3-15,60,20-10,0,0',
        'e4-10,20,40-30,60,50'
        ]

for elm in plst:
    a,b,c = elm.split("-")
    print(sum([int(e) for e in b.split(",")]))
    print(sum([int(e) for e in c.split(",")]))

