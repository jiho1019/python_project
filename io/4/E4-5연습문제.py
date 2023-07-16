a = 0
for i in range(0,101,4):
  if i % 4 == 0:
    a = a + i
    print("%d --> %d"%(i,a))