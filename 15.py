zonelist = ["north-q1,10,q2,80",
            "south-q1,160,q2,60",
            "east-q1,35,q2,60",
            "west-q1,60,q2,30"]

emplst = []
sales  = []

for elm in zonelist:
    elm = elm.split("-")[1].split(",")[1::2]
    alst = sum([int(e) for e in elm])
    emplst.append(alst)
    reslt = sum([int(f) for f in emplst])
print(reslt)





