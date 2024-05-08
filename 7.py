a = "10-20,30-40,50-60"
alst = a.split(",")
blst = [e.split("-")[0] for e in alst]
b = "|".join(blst)
print(b)
blst = [e.split("-")[1] for e in alst]
blst = "|".join(blst)
print(blst)
blst = [e.split("-")[0][0]+e.split("-")[1][0] for e in alst]
b = "|".join(blst)
print(b)
