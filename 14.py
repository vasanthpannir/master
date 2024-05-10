import itertools

plst = ['dvd-60',
        'cpu-70',
        'mon-40',
        'keb-80'
        ]

emplst = []
for elm in plst:
    name,qty = elm.split("-")
    emplst.append(int(qty))
print(sum(emplst))
