print("-"*40)
print("\tcm\tmm\tm\tinch")
print("-"*40)
for i in range(1,101,1):
  a = i*10
  b = i*0.01
  c = i*0.3937
  print("\t",i,"\t",a,"\t%.2f\t%.1f"%(b,c))
