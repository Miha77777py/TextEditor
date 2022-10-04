def files(name):
    dct = {}
    with open(name, 'r') as file:
        b = file.read()
        text = ''.join(i.lower() for i in b.split())
        for i in text:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        return dct
