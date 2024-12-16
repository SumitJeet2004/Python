s1= {8,4,3,2,7,2}
s2={5,7,3,5,10}
s3=s1.symmetric_difference(s2)
print(s3)
s3=s1.symmetric_difference_update(s2)
print(s3)
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
s3=s1.symmetric_difference(s2)
print(s3)
cities= {"kolkata","bbsr","chennai","bombay"}
cities.remove("bbsr")
print(cities)
item=cities.pop()
print(cities)
print(item)
