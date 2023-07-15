'''
print()함수를 이용한 데이터 출력
-작성자:황재호
-일자:2023.7.15
'''
name = input("당신의 이름은?")
birth = int(input("당신이 태어난 해는?"))
age = 2023 - birth + 1
print("%s님의 나이는%d입니다"%(name,age))