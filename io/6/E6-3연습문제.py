year_sale = {"2016":237,"2017":98,"2018":158,"2019":233,"2020":120}
b = 0
for i in year_sale:
  b = b + year_sale[i]

c = b/len(year_sale)

print("5년간 총 판매량:%d"%b)
print("5년간 평균 판매량:%d"%c)