numbers = [7,9,15,18,30,-3,7,12,-16,-12]
a = 0
list = []
while a < len(numbers):
  if a%2 == 1:
    list.append(numbers[a])
  a = a + 1
print(list)
print(sum(list))