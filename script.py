import sys
import mymodule
import math
import random

print(sys.platform)
print(2**100)
x = 'spam!'
print(x*8)
print(mymodule.title)
print(dir(mymodule))
exec(open('mymodule.py').read())
print(math.pi)
print(math.sqrt(85))
print(random.random())
print(random.choice([1, 2, 3, 4]))

s = 'shrubbery'
l = list(s)
print(l)
l[1] = 'c'
print(''.join(l))

b = bytearray(b'spam')
b.extend(b'eggs')
print(b)
print(b.decode())

s = 'spam'
print(s.find('pa'))
print(s.replace('pa', 'XYZ'))

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))
s = 'spam'
print(s.upper())
print(s.isalpha())
line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())
print(line.rstrip().split(','))

print(dir(line))
print(help(line.replace))

l = [123, 'spam', 1.23]
print(len(l))
print(l[0])
print(l[:-1])
l = l + [4, 5, 6]
print(l)
l = l * 2
print(l)

l.append('NI')
print(l)
l.pop(2)
print(l)

m = ['bb', 'aa', 'cc']
m.sort()
print(m)
m.reverse()
print(m)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in m]
print(col2)
print(m)

col2 = [row[1] + 1 for row in m]
print(col2)
col2 = [row[1] for row in m if row[1] % 2 == 0]
print(col2)

diag = [m[i][i] for i in [0, 1, 2]]
print(diag)
doubles = [c * 2 for c in 'spam']
print(doubles)

print(list(range(4)))
print(list(range(-6, 7, 2)))
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

G = (sum(row) for row in m)
print(next(G))
print(next(G))
print(next(G))

print(list(map(sum, m)))
print({sum(row) for row in m})
print({i : sum(m[i]) for i in range(3)})

d = {'food' : 'spam', 'quantity' : 4, 'color' : 'pink'}
print(d)
print(d['food'])
d['quantity'] += 1
print(d)

d = {}
d['name'] = 'Bob'
d['job'] = 'dev'
d['age'] = 40
print(d)
print(d['name'])

bob1 = dict(name = 'Bob', job = 'dev', age = 40)
print(bob1)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)

rec = {'name' : {'first' : 'Bob', 'last' : 'Smith'}, 'jobs' : ['dev', 'mgr'], 'age' : 40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['jobs'])
print(rec['jobs'][-1])
rec['jobs'].append('janitor')
print(rec)

d = {'a' : 1, 'b' : 2, 'c' : 3}
print(d)
d['e'] = 99
print(d)
print('f' in d)
if not 'f' in d:
    print('missing')
value = d.get('x', 0)
print(value)
value = d['x'] if 'x' in d else 0
print(value)

t = (1, 2, 3, 4)
print(len(t))
print(t + (5, 6))
print(t[0])
print(t.index(4))
print(t.count(4))
t = (2, ) + t[1:]
print(t)
t = 'spam', 3.0, [11, 22, 33]
print(t[1])
print(t[2][1])

f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt')
text = f.read()
print(text)
print(text.split())

for line in open('data.txt'):
    print(line)

x = set('spam')
y = {'h', 'a', 'm'}
print(x, y)
print(x & y)
print(x | y)
print(x - y)
print(x > y)
print({n ** 2 for n in [1, 2, 3, 4]})
print(list(set([1, 2, 1, 3, 1])))
print(set('spam') - set('ham'))
print(set('spam') == set('asmp'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1 / 3)
print((2 / 3) + (1 / 2))

import decimal

d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction

f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))

print(1 > 2, 1 < 2)
print(bool('spam'))
x = None
print(x)
l = [None] * 100
print(l)

print(type(l))
print(type(type(l)))

if type(l) == type([]):
    print('yes')
if type(l) == list:
    print('yes')
if isinstance(l, list):
    print('yes')

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(0.10)
print(sue.pay)

print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
from fractions import Fraction

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(Decimal(1) / Decimal(7))
decimal.getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))
print(1999 + 1.33)
decimal.getcontext().prec = 2
pay = Decimal(str(1999 + 1.33))
print(pay)
print((1 / 3) + (6 / 12))
print(Fraction(6, 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))
print(1000.0 / 1234567890)
print(Fraction(1000, 1234567890))

print(8 % 7)

x = set('abcde')
y = set('bdxyz')
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)
z = x.intersection(y)
print(z)
z.add('SPAM')
print(z)
z.update(set(['X', 'Y']))
print(z)
z.remove('b')
print(z)
for item in set('abc'): print(item * 3)
s = set([1, 2, 3])
print(s | set([3, 4]))
print(s.union([3, 4]))
print(s.intersection((1, 3, 5)))
print(s.issubset(range(-5, 5)))
print({x ** 2 for x in [1, 2, 3, 4]})
print({x for x in 'spam'})
print({x * 4 for x in 'spam'})
print({x * 4 for x in 'spamham'})
s = {x * 4 for x in 'spam'}
print(s | {'mmmm', 'xxxx'})
print(s & {'mmmm', 'xxxx'})

a = 3
a = 'spam'
a = 1.23

l1 = [1, 2, 3]
l2 = l1
print(l1)
print(l2)
l1[0] = 24
print(l1)
print(l2)

l1 = [1, 2, 3]
l2 = l1[:]
print(l1)
print(l2)
l1[0] = 24
print(l1)
print(l2)

import sys
print(sys.argv)

s = 'spam'
s = s + 'SPAM!'
print(s)
s = s[:4] + 'Burger' + s[-1]
print(s)
s = 'splot'
s = s.replace('pl', 'pamal')
print(s)
print(dir(s))

line = 'The knights who say Ni!\n'
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))
print(line.find('Ni') != -1)
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))
print(line[-len(sub):] == sub)

print(list(map(abs, [-1, -2, 0, 1, 2])))
l = ['spam', 'Spam', 'SPAM!']
l[1] = 'eggs'
print(l)
l[0:2] = ['eat', 'more']
print(l)
l = [1, 2, 3]
l[1:2] = [4, 5]
print(l)
l[1:1] = [6, 7]
print(l)
l[1:2] = []
print(l)
l = [1]
l[:0] = [2, 3, 4]
print(l)
l[len(l):] = [5, 6, 7]
print(l)
l.extend([8, 9, 10])
print(l)
l = ['eat', 'more', 'SPAM!']
l.append('please')
print(l)
l.sort()
print(l)
l = ['spam', 'eggs', 'ham', 'toast']
del l[0]
print(l)
del l[1:]
print(l)

d = {x : x * 2 for x in range(10)}
print(d)
d = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
print(list(d.values()))
print(list(d.items()))
print(d.get('spam'))
print(d.get('toast'))
print(d.get('toast', 88))
d2 = {'toast' : 4, 'muffin' : 5}
d.update(d2)
print(d)
d.pop('muffin')
d.pop('toast')
print(d)
print([y for (x, y) in d.items() if x == 'spam'])

matrix = {}
matrix[(2, 3, 4)] = 88
matrix[(7, 8, 9)] = 99
x = 2
y = 3
z = 4
print(matrix[(x, y, z)])
print(matrix)
try:
    print(matrix[(2, 3, 5)])
except KeyError:
    print(0)
print(matrix.get((2, 3, 4), 0))
print(matrix.get((2, 3, 6), 0))

myfile = open('myfile.txt', 'w')
myfile.write('Hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()
myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
print(open('myfile.txt').read())
for line in open('myfile.txt'):
    print(line)

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a' : 1, 'b' : 2}
L = [1, 2, 3]
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()
chars = open('datafile.txt').read()
print(chars)
F = open('datafile.txt')
line = F.readline()
print(line)
print(line.rstrip())
line = F.readline()
print(line)
parts = line.split(',')
print(parts)
numbers = [int(p) for p in parts]
print(numbers)
line = F.readline()
print(line)
parts = line.split('$')
print(parts)
print(eval(parts[0]))
objects = [eval(p) for p in parts]
print(objects)

D = {'a' : 1, 'b' : 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)

print(open('datafile.pkl', 'rb').read())

name = dict(first = 'Bob', last = 'Smith')
rec = dict(name = name, job = ['dev', 'mgr'], age = 40.5)
print(rec)
import json
print(json.dumps(rec))
S = json.dumps(rec)
print(S)
O = json.loads(S)
print(O)
print(O == rec)
json.dump(rec, fp = open('testjson.txt', 'w'), indent = 4)
print(open('testjson.txt').read())
P = json.load(open('testjson.txt'))
print(P)

import csv
rdr = csv.reader(open(r'd:\data\user_data.csv.txt'))
for row in rdr: print(row)

with open(r'd:\data\user_data.csv.txt') as myfile:
    for line in myfile: print(line)

myfile = open(r'd:\data\user_data.csv.txt')
try:
    for line in myfile: print(line)
finally:
    myfile.close()

s = 'eggs' * 5
print(s[:0])
l = [1, 2, 3, 4]
l[3:1] = ['?']
print(l)
l[2] = []
print(l)
l[2:3] = []
print(l)
del l[0]
print(l)
del l[1:]
print(l)
l[1:2] = [1]
print(l)
d = (1, 2, 3)
print(l + d)