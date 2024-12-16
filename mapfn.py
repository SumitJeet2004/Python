def cube(x):
    return x**3

print(cube(2))
l=[1,2,3,4,5,6,7]
newl=list(map(cube,l))
newl2=list(map(lambda x:x*x,l))
print(newl)
print(newl2)

#filter
def filter_function(a):
    return a>2

newnewl=list(filter(filter_function,l))
print(newnewl)

#reduce
from functools import reduce
def mysum(x,y):
    return x+y
sum = reduce(mysum,l)
print(sum)

