a = "21-jan-2019,30-dec-2015,15-aug-147"
alst = a.split(",")
blst = [e.split("-")[2][-2:] for e in alst]
clst = [e.split("-")[1] for e in alst]
dlst = [e.split("-")[1][0].upper()+e.split("-")[1][-1].upper() for e in alst]
print(blst)
print(clst)
print(dlst)

