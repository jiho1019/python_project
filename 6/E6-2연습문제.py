year_sale = {"2016":237,"2017":98,"2018":158,"2019":233,"2020":120}
b = 0
for i in year_sale:
  if i == "2018" or i == "2019":
    print("%s년 자동차 판매량:%d대"%(i,year_sale[i]))
    b = b + year_sale[i]
print("2년간 자동차 판매량:%d대"%b)