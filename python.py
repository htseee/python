x = ["Suraj","Gautam","Yash","Ram"]
if "Ram" in x:
    print("Ram is present")
x.insert(2, "2")
print(x)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
list1 = ["Tomatoes","Potato","Onion"]
list2 = ["Apple","Banana","Watermelon"]
l = list1 + list2
print(l)
l.pop(3)
print(l)
l.remove("Tomatoes")
print(l)
l.clear()
print(l)
l.append("Jupiter")
print(l)
l.pop()
print(l)
dictionary = {"Ram":24,"Rahul":12,"Karan":18}
y = dictionary.get("Rahul")
f = dictionary.get("Karan")
print(y)
print(f)
k = dictionary.values()
print(k)
k = dictionary.items()
print(k)
dictionary["Ram"] = 23
print(dictionary)
dictionary["Raf"] = 2
print(dictionary)
dictionary.pop("Karan")
print(dictionary)
del dictionary["Ram"]
print(dictionary)
dictionary.clear()
print(dictionary)
fruit = ["Apple","Grape","Melon","Kiwi","Banana"]
for x in fruit:
    print(x)
for x in fruit:
    if x == "Kiwi":
        continue
    print(x)
a = "Antarctica"
for x in a:
    print(x)
for x in range(25):
    print(x)
for x in range(3, 15):
    print(x)
for x in range(20, 45, 2):
    print(x)
for x in range(20, 45, 2):
    if x == 30:
        break
    print(x)
for x in range(1, 11):
    print("10 x ", x, "=", 10 * x)
x = 1
while x < 6:
    print(x)
    x = x + 1
x = 0
while x < 15:
    x = x + 1
    if x == 11:
        continue
    print(x)
number = 6
for row in range(number):
    for column in range(row + 1):
        print(column + 1, end="")
    print("")
number = 10
for x in range(number):
    print(x / 2, x // 2)
A = 30
B = 45
C = 36
print(max(A, B, C))
print(min(A, B, C))
print(abs(A - C))
print(abs(C - A))
D = 6
E = 9
print(A % D)
print(A % E)