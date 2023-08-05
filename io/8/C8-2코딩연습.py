def square_sum(n):
  sm = 0
  for i in range(1, n+1):
    if i % 2 != 0:
      sm = sm + (i*i*i)
      print("%d*%d*%d"%(i,i,i))

      if i == n or i == (n-1):
        print("= ",end = "")
      else:
        print("+ ",end = "")
  print(sm)

N = int(input("N의 값을 구하시오."))
print(square_sum(N))