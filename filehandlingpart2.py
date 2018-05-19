k = dict()
i = 0
l = []
f = open("alfismacho.txt")
for x in f.readlines():


    if x[:-1] == "!":

        if len(l) == 0:
            continue
        else:
            k[i]= l
            i = i+1
            l=[]
    else:
        l.append(x[:-1])

k[i]=l
for i in k.values():
    print(i)




