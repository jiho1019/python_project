def get_item(userid):
  game_items = {"kim":"kar98k","lee":"svt40","choi":"m1garund","hwang":"ramington870"}
  for i in game_items:
    if userid == i:
      item = game_items[i]
  return item

user1 = "kim"
user2 ="hwang"

print("%s의 게임 아이템:%s"%(user1,get_item(user1)))
print("%s의 게임 아이템:%s"%(user2,get_item(user2)))