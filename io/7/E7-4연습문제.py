def a(b):
  c = b*0.621371
  print("%d 킬로미터는 %.2f 마일이다."%(b,c))
  return c
b = int(input("킬로미터를 입력하세요"))
a(b)