def count_words(a):
  arr = a.split(" ")
  return len(arr)

string = input("문장을 입력하세요 :")
num_words = count_words(string)
print("단어의 개수 :",num_words)