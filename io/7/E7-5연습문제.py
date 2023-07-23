def a(c,d):
  global b
  if b == 1:
    e = c + d
  if b == 2:
    e = c - d
  if b == 3:
    e = c * d
  if b == 4:
    e = c / d
  print(e)
  return e

print("-선택옵션\n1.더하기\n2.빼기\n3.곱하기\n4.나누기")
b = int(input("원하는 옵션을 선택하세요.(1/2/3/4)"))
c = int(input("첫 번째 숫자를 입력하세요."))
d = int(input("두 번쨰 숫자를 입력하세요."))
a(c,d)