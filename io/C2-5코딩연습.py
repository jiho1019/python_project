price = int(input("책의 값은?"))
discount = int(input("할인률은?"))
delivery = int(input("배송비는?"))
pay = price -(price*(discount/100))+ delivery
print("책 값:%d"%price)
print("할인률:%d"%discount)
print("배송료:%d"%delivery)
print("결제금액%d"%pay)