data = "20,30,40-a|b|c|d"

alst = data.split("-")[1].split("|")
blst = data.split("-")[0].split(",")
result = sum([int(e) for e in blst])
print(result)


