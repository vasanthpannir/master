alst = ['one.txt',
        'new.doc',
        'hello.py',
        'some.txt'
        ]
for filename in alst:
    name,ext = filename.split('.')
    print(ext)
    if ext=='txt':
        print(name)