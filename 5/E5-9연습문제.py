numbers = [7,9,15,18,30,-3,7,12,-16,-12]
a = 0
b = []
while a < len(numbers):
  if numbers[a]%2 == 0:
    b.append(numbers[a])
  a = a + 1
print(b)
print(sum(b))
