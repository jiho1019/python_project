def words(a,b):
  global c
  c = 0
  for i in a:
    if i == b:
      c = c + 1

a = input("영어 문장을 입력하세요")
b = input("알파벳 하나를 입력하세요.")
words(a,b)
print("%s에 포함된%s의 개수는 %d개이다."%(a,b,c))
