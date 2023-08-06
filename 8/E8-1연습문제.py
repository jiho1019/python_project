def a(x):
  y = 0
  if x % 2 == 0:
    y = "짝수"
  else:
    y = "홀수"
  return y

num = int(input("숫자를 선택하세요."))
result = a(num)
print("%d는 %s이다"%(num,result))
