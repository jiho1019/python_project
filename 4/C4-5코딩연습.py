a = input("숫자를 입력하세요.")
c = 0
for b in a:
  if int(b) % 2 == 1:
    c = c + 1
print("홀수의 개수:%d개"%c)
    