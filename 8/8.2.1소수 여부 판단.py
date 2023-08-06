def a(x):
  b = True
  if x > 1:
    for i in range(2,x):
      if x % i == 0:
        b = False
  return b
number = int(input("소수를 입력하세요."))
if a(number):
  print("소수이다!")
else:
  print("소수가 아니다!")