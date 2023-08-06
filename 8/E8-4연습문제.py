def a(x):
  arr = []
  for i in x:
    if i % 2 == 0:
      arr.append(i*10)
    else:
      arr.append(i*100)
  return arr
    
data = [2,6,3,8,7]
result = a(data)
print(result)