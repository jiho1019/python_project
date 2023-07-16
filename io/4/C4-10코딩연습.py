print("-"*30)
print("\t달러\t원화\t유로")
print("-"*30)
a = 10
while a <= 100:
  b = a*1080
  c = a*0.81

  print("%7d %8.0f %7.1f"%(a,b,c))

  a = a + 10

print("-"*30)