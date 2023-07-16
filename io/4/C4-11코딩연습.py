a = input("문장을 입력해 주세요.")

i = len(a)

while i >= 0:
  if a[i] == " ":
    print("-",end = " ")
  else:
    print("%s"%a[i],end = " ")

