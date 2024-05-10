plst = ['dvd-60','cpu-30','PRN-10']

for elm in plst:
    a,b = elm.split("-")
    if int(b)>50:
        print("above 50")
    else:
        print("less tha 50")

