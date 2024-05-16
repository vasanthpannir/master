alst = ["hello hai how are you",
        'some info',
        'is added now also ']

atab = {}
num = 1
for elem in alst:
        now = len(elem.split())
        key = 'line'+str(num)
        atab[key]=now
        num=num+1
print(atab)