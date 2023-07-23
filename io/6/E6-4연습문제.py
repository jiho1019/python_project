year_sale = {"2016":237,"2017":98,"2018":158,"2019":233,"2020":120}
b = 2016
c = year_sale["2016"]
for i in year_sale:
  if year_sale[i] > year_sale["2016"]: 
    b = i
    c = year_sale[i]
print("판매량이 가장 많은 해:%d년"%b)
print("판매량:%d대"%(c))