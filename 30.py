date = {
        1:'Jan',
        2:'Feb',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
}

a = input("enter the date:\n")
if '/' in a:
    e = a.split("/")
    print(e[0],'-',date.get(int(e[1])),'-',e[-1])
else:
    e = a.split("-")
    print(e[0], '-', date.get(int(e[1])), '-', e[-1])