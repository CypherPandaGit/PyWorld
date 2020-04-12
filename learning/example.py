print(dir())

for obj in dir(__name__):
    if obj[0] != '_':
        print(obj)
