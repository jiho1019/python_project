import random

x = ["가위","바위","보"]

def choice(a,x):
  computerchoice = x[a]
  return computerchoice

again = "yes"
print("="*50)
print("가위바위보 게임")
print("="*50)
while True:
  if again == "yes":
    me = input("가위 바위 보 중에 고르세요.")
    computer = choice(random.randint(0,2),x)
    print("나:",me)
    print("상대:",computer)
    if me == "가위" and computer == "바위" or me == "바위" and computer == "보" or me == "보" and computer == "가위":
      print("상대의 승리입니다!")
    elif me == "가위" and computer == "보" or me == "바위" and computer == "가위" or me == "보" and computer == "바위":
      print("나의 승리입니다!")
    else:
      print("무승부 입니다!")
    print("-"*50)
    again = input("계속 하시겠습니까?(예:yes/아니오:no)")
  else:
    break
print("게임이 종료되었습니다.")



