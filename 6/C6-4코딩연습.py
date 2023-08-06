word = {"꽃":"flower","나비":"butterfly","학교":"school","자동차":"car","비행기":"airplane"}

print("<영어 단어 맞추기 퀴즈>")

for i in word:
  input_word = input("'%s'에 해당하는 영어 단어를 입력하세요:"%i)

  if input_word == word[i]:
    print("정답입니다")
  else:
    print("틀렸습니다")
