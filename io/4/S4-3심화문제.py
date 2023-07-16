a = int(input("시작 수를 입력해주세요:"))
b = int(input("끝 수를 입력해주세요."))
flag = False # 이 수가 나누어 떨어지는 수가 있는지 판별하는 변수

for i in range(a,b+1):
    flag = False
    for j in range(2,i//2):
      if i % j == 0:
        flag = True
    if flag == False:
      print(i,end = " ")

   