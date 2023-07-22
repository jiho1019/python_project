a = []
while True:
  b = int(input("성적을 입력하세요.(종료시 -1 입력)"))
  if b == -1:
    break
  else:
    a.append(b)
sum = 0 
for c in a:
  sum = sum + c

avg = sum/len(a)
print("합계:%d,평균:%.2f"%(sum,avg))
