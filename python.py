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

red, green, blue = range(3)
print(red, blue)
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)
L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)
seq = [1, 2, 3, 4]
a, *b = seq
print(a)
print(b)
*a, b = seq
print(a)
print(b)
a, *b, c = seq
print(a)
print(b)
print(c)
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z, sep='')
print(x, y, z, sep=', ')
print(x, y, z, end='')
print(x, y, z, end=''); print(x, y, z)
print(x, y, z, end='...\n')
print(x, y, z, sep='...', end='!\n')
print(x, y, z, sep='...', file=open('data.txt', 'w'))
print(x, y, z)
print(open('data.txt').read())
log = open('log.txt', 'a')
print(x, y, z, file=log)
print(x, y, z)
log = open('log.txt', 'w')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)
print(open('log.txt').read())

A = 't' if 'span' else 'f'
print(A)
A = 't' if '' else 'f'
print(A)

y = 13
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x = x - 1
else:
    print(y, 'is prime')
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(list(zip(L1, L2)))
for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)
S = 'spam'
for (offset, c) in enumerate(S):
    print(c, 'appears at offset', offset)
print([c * i for (i, c) in enumerate(S)])