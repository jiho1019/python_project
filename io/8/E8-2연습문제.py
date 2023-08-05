def a(x):
  sum = 0
  for i in range(1,1001,1):
    if i % x == 0:
      sum = sum + i
  return sum

num = int(input("N값을 입력하세요."))
result = a(num)
print(result)
print("1에서 1000까지 수중 %d의 배수 합계:%d"%(num,result))