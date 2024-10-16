from math import *
import turtle
def add(a, b):
    return a + b
i=2
numTerms = 10 if i>10 else i
for i in range(numTerms):
    print(add(10, i))
    print("OK")
x = int(input())
if x >= 10:
    print("2 chữ số")
elif x < 0:
    print("Số âm")
else:
    print("1 chữ số")
while x > 0:
    print(x)
    x -= 1
