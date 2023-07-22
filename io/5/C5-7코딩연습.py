a = [100,20,30,40,50,20,10,30,40,20,50,60]

soo = 0
woo = 0
mi = 0
yang = 0
ga = 0

i = 0
while i < len(a):
  if a[i] >= 90 and a[i] <= 100:
    soo = soo + 1
  if a[i] >= 80 and a[i] <= 89:
    woo = woo + 1
  if a[i] >= 70 and a[i] <= 79:
    mi = mi + 1
  if a[i] >= 60 and a[i] <= 69:
    yang = yang + 1
  if a[i] >= 0 and a[i] <= 59:
    ga = ga + 1

  i = i + 1

print("수 : %d명"%soo)
print("우 : %d명"%woo)
print("미 : %d명"%mi)
print("양 : %d명"%yang)
print("가 : %d명"%ga)


