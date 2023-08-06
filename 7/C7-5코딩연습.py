def tri_area(a,b):
  c = a * b / 2
  return c

a = int(input("너비를 입력하세요."))
b = int(input("높이를 입력하세요."))

print("-삼각형의 너비:",a)
print("-삼각형의 높이:",b)
print("-삼각형의 면적:",tri_area(a,b))