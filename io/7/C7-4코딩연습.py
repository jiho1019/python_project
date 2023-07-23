def mutiply(num,x):
  i = 0
  while i < len(num):
    num[i] = num[i] * x
    i = i + 1

numbers = [10,20,30,40,50]

mutiply(numbers,10)
print(numbers)
mutiply(numbers,10)
print(numbers)
