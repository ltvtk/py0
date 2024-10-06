function fibonacci(n)
  if n <= 1 
      return n
  else 
      return fibonacci(n-2) + fibonacci(n-1)
  end
end

numTerms = 10

for i in range(numTerms) 
  print(fibonacci(i))
end