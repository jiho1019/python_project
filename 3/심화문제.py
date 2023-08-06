a  = input("등급을 입력해주세요(A+,A,B+,B...F)")
if a == "A+":
  b = 4.5
elif a == "A":
  b = 4
elif a == "B+":
  b = 3.5
elif a == "B":
  b = 3
elif a == "C+":
  b = 2.5
elif a == "C":
  b = 2
elif a == "D+":
  b = 1.5
elif a == "D":
  b = 1
else:
  b = 0
print("등급:",a,"평점:",b)