a = int(input("키는?"))
b = int(input("몸무게는?"))
c = (a - 100)*0.9
print("="*50)
print("키:",a)
print("몸무게:",b)
if c < b:
  print("건강을 위해 다이어트가 필요합니다.")
else:
  print("표준 또는 마른 체형입니다.")