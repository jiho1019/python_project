def a(n,x):
  start = 0
  end = len(n)-1

  while start <= end:
    mid = (start + end)//2
    if x == n[mid]:
      return True
    elif x > n[mid]:
      end = mid -1
    else:
      start = mid + 1

  return False

data = [55,3,-12,2,51,-23,17,9,13,16,30,9]
data2 = [data.sort()]
num = int(input("찾고자 하는 수를 입력하세요."))
if a(data2,num):
  print(data2)
  print("%d은(는) 리스트에 존재한다."%num)
else:
  print(data2)
  print("%d은(는) 리스트에 존재하지 않는다."%num)