def a(x,y):
  for i in x:
    if i == y:
      return True
  return False

data = [55,3,-12,2,51,-23,17,9,13,16,30,9]
num = int(input("찾고자 하는 수를 입력하세요."))
if a(data,num):
  print("%d은(는) 리스트에 존재한다."%num)
else:
  print("%d은(는) 리스트에 존재하지 않는다."%num)