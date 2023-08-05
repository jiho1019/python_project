def a(x,y):
  start = 0
  end  = len(x)-1
  arr = x.sort()
  while start <= end:
    mid = (start + end)//2
    if y > arr[mid]:
      start = start + 1
    elif y < arr[mid]:
      end = end - 1
    else:
      return True
  return False


data = [55,3,-12,2,51,-23,17,9,13,16,30,9]
num = int(input("찾고자 하는 수를 입력하세요."))
if a(data,num):
  print("%d은(는) 리스트에 존재한다."%num)
else:
  print("%d은(는) 리스트에 존재하지 않는다."%num)