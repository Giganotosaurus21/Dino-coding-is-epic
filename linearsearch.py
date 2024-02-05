import random

trexboys = []

for i in range(25):
    #i = 0,1,2...499

    x = random.randint(1, 100)

    trexboys.append(x)

for i in range(25):
    if trexboys[i] == 42:
        print("I found the meaning of life!")
        break
    
        
if trexboys[i] != 42:
    print("I did not find the meaning of life!")

 