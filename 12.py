alst = ["a-10","b-20","c-30"]
print(sum([int(e.split(",")[0].split("-")[1]) for e in alst]))
