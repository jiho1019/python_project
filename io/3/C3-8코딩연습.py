print("서비스 만족도:\n\t1:매우만족\n\t2:만족\n\t3:불만족")
a = int(input("서비스 만족도는?(1/2/3/)"))
b = int(input("음식 값은?"))

if a == 1:
  c = b*0.2
  d = "매우만족"
elif a == 2:
  c = b*0.1
  d = "만족"
else:
  c = 0
  d = "불만족"

print("서비스 만족도:%s,팁:%d원"%(d,c))
