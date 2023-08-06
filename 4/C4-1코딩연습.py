a = 0 
for i in range(200,801):
  if i%5 != 0:
    print("%d"%i,end=" ")
    a = a + 1

    if a % 10 == 0:
      print()