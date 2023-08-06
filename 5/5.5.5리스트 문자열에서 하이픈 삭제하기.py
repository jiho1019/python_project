a = ["010-1234-5678","010-1234-1234","010-5678-5678"]
print(a)
b = []
for i in a:
  x = i.replace("-","")
  b.append(x)
print(b)