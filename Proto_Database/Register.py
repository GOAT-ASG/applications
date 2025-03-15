import pandas as pd

data = open('Proto_Database/base.txt').read()
data = data.replace('{','').replace('}','')

def retrieve(data):
    stuff = {}
    temp = []
    used = []
    temp = data.split(',')

    for i in range(len(temp)):
        name = temp[i].split(":")[0].replace("'",'').replace(' ','')
        value = temp[i].split(":")[1].replace(' ','')
        stuff[name] = int(value)
        used.append(int(temp[i].split(":")[1].replace(' ','')))

    return stuff, used

stuff, used = retrieve(data)

while True:
    choice = int(input('1 - input\n2 - insert\n3 - table\n4 - delete'))

    if choice == 1:
        val = int(input(''))

        for key in stuff:
            if val >= stuff[key]:
                res = key
            else:
                break
        print(res)

    elif choice == 2:
        id = 0
        while id in used:
            id += 1
        used.append(id)
        name = str(input('NAME: '))
        key = str(name)
        val = id

        stuff[key] = val

        data = open('Proto_Database/base.txt','w')
        data.write(str(stuff))
        data.close()

    elif choice == 3:
        frame = {
        "NAME": stuff.keys(),
                }

        print(pd.DataFrame(frame))

    else:
        dell = str(input('NAME:'))
        used.remove(stuff[dell])
        stuff.pop(dell)

        data = open('Proto_Database/base.txt','w')
        data.write(str(stuff))
        data.close()




