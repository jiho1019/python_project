a = int(input("시작수는?"))
b = int(input("끝 수는?"))
c = int(input("정수를 입력하세요"))
if a < c and b > c:
  print(c,"은(는)", a,"~", b, "사이에 있다.")
else:
  print(c,"은(는)", a,"~", b, "사이에 없다.")