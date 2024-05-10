data = "10,20-30 40-50,60 70"
print("pass" if sum(int(e) for e in data.replace(',', '-').replace(' ', '-').split('-')) > 100 else "fail")

