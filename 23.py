ptab = {
        'dvd':60,
        'mon':80,
        'cpu':75,
        'PRN':85,
        'KEB':40,
        'HDD':100
}
below70 = []
above70 = []
for k,v in ptab.items():
    if v<=70:
        below70.append(k)
    else:
        above70.append(k)
print(below70)
print(above70)

