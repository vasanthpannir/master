a = "arun-10,20,30|ravi-30,60,70|john-70,80,90"
alst = a.split("|")
blst = "-".join([e.split("-")[0][-1].upper()for e in alst])
clst = sum([int(e.split("-")[1].split(",")[0]) for e in alst])
dlst = [int(e.split("-")[1].split(",")[-1]) for e in alst]
print(blst)
print(clst)
print(dlst)