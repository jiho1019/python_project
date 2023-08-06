a = list(range(0,20))
b = 0

while b < len(a):
  b = b + 1
  if (b) % 3 == 0:
    print("%d"%b, end = " ")
  else:
    continue

