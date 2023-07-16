a = int(input("첫번째 시간의 시를 입력하세요"))
b = int(input("첫번째 시간의 분를 입력하세요"))
c = int(input("두번째 시간의 시를 입력하세요"))
d = int(input("두번째 시간의 분를 입력하세요"))
e = a*60
f = c*60
if e + b < f + d:
  print("-빠른시간 :", a,":",b)
  print("-늦은시간 :", c,":",d)
else:
  print("-빠른시간 :", c,":",d)
  print("-늦은시간 :", a,":",b)