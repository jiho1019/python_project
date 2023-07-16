a = input("영문소문자 또는 대문자를 입력하세요:")
b = a.upper()
if b == "A" or b == "E" or b == "I" or b == "O"  or  b == "U":
  print("%s -> 모음"%a)
else:
  print("%s -> 자음"%a)