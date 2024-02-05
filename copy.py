import random

indoraptor = []
itemnumber = 0
for i in range(100):
    

    x = random.randint(1, 100)

    indoraptor.append(x)

scorpiusrex = []
for i in range(100):

    y = indoraptor[itemnumber]
    itemnumber = itemnumber + 1
    scorpiusrex.append(y)
print(indoraptor)
print(scorpiusrex)
