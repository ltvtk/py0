from math import *
import turtle

// Arrow function với nhiều tham số
add = (a, b) => a + b

// Arrow function một tham số
square = x => x * x

// Arrow function không tham số
getPi = () => 3.1415

numTerms = 10

for i in range(numTerms)
  // Sử dụng arrow function inline
  print(((x) => x * x)(i))
  print(add(10, i))
  print(square(i))
  print(getPi())
  print("OK")
end

x = int(input())

if x >= 10
  print("2 chữ số")
else if x < 0
  print("Số âm")
else
  print("1 chữ số")
end

while x > 0
  print(x)
  x -= 1
end