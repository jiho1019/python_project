a = 0
b = 0
n = 1
while n <= 100:
  if n % 2 == 1:
    a = a + n
    print("%6d"%a, end = " ")
    b = b + 1

    if b % 10 == 0:
      print()
  n = n + 1
