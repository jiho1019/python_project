print("-"*50)
print("킬로그램\t파운드\t온스")
print("-"*50)
for i in range(100,201):
  a = i*2.204623
  b = i*35.273962
  print("%d\t\t%.1f\t%.1f"%(i,a,b),end = " ")
  print()