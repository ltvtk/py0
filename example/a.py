from math import *
import turtle
def add(a, b):
    return a + b
numTerms = 10
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
