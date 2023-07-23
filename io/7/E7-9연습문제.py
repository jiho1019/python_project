b = input("문자열을 입력하세요:")
def space(a):

  for x in a:
    if x == " ":
      a.replace(" ","-")
  print(a)

space(b)
