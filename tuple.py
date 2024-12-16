tup=(1,2,3,45,6,3,223,"green",True)#the only dif is it is not changable
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-3])

if 5 in tup:
    print("yes present")
else:
    print("no ")


tup2 = tup[1:4]
print(tup2)