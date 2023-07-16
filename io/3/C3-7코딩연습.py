a = int(input("구매 금액은?"))
if a >= 10000 and a <= 50000:
  b = 5
  c = a*b/100
  d = a - c 
elif a > 50000 and a < 300000:
  b = 7.5
  c = a*b/100
  d = a - c 
elif a >= 300000:
  b = 10
  c = a*b/100
  d = a - c 
else:
  c = 0
  b = 0
  d = a
print("구매금액:",a )
print("할인률:",b)
print("할인금액:",c)
print("지불금액:",d)


  