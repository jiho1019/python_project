a = int(input("단위를 입력해주세요(1:섭씨,2:화씨):"))
b = int(input("온도를 입력해주세요."))
if a == 2:
  b = (b-32)*8/9

if b <= 0:
  c = "고체"
elif b < 100:
  c = "액체"
else:
  c = "기체"

print("물의 섭씨 온도 : %.1f도,상태 : %f"%(b,c))