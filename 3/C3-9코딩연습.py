a = int(input("첫번째 정수는?"))
b = int(input("두번째 정수는?"))
c = int(input("세번째 정수는?"))
if a > b and a > c:
  d = a
elif b > a and b > c:
  d = b
else:
  d = c

print("%d,%d,%d 중에서 가장 큰수는 %d 입니다."%(a,b,c,d))    