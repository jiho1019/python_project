a = list(range(1,22))

for i in range(1,len(a)):
  if i%2 == 0:
    print("%d"%i, end = " ")
  else:
    continue