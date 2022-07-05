import operator
# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])

print(a)
#a.sort(key=lambda x:x[1])
a.sort(key=operator.itemgetter(1))
print(a)

# Dictionary sort
b = {"Nick": 30, "John": 8, "Paul": 22, "Mark": 66}
print(b)
#b = dict(sorted(b, key=lambda x: x[1]))
print(b.items())
for y in sorted(b.items(), key=lambda x: x[1]):
    print(y)
b = dict(sorted(b.items(), key=operator.itemgetter(1)))
print(b)


c = [("John", 31) ,("Bob", 10), ("Tim", 4), ("Mark", 12)]
#c.sort()
c.sort(key=lambda x:x[1])
print("c=", c)

