marks = [8,4,2,3,2,7]
print(marks)
print(marks[1])
print(type(marks))
marks.append(6)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.count(2))
l=marks.copy()
l[0]=0
print(l)
marks.insert(2,30)
print(marks)
l=[30,5555,33]
k=l+marks#or marks.extend(l)
print(k)
k=marks+l
print(k)



