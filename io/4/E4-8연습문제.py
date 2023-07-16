print("-"*50)
print("\tcm\tmm\tm\tinch")
print("-"*50)
i = 1
for i in range(1,51,1):
  a = i*10
  b = i*0.01
  c = i*0.39
  i = i + 1
  print("\t%.2f\t%.2f\t%.2f\t%.2f"%(i,a,b,c))
print("-"*50)
