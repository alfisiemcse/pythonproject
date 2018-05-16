k = dict()
i = 0
l = []
f = open("alfis.txt")
for x in f.readlines():
    i = i+1
    if i >=2:
        l = list(x[:-1].split(","))
        k[l[22]]=l
print(sorted(k),end="")
print(i)

