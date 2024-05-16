plst = ["dvd-50,60",
        "Mon-15,1",
        "Cpu-20,70",
        "kEB-15,10"
        ]

print("atab={")
for e in plst:
        print('\t','"',e.split('-')[0],'"',':',sum([int(f) for f in e.split('-')[1].split(',')]))
print('\t','}')

