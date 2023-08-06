a = ["s_hool","compu_er","deco_ation","windo_","hi_tory"]
b = ["c","t","r","w","s"]
for i in range(0,len(a),1):
  c = input("%s:밑 줄에 들어갈 알파벳은?"%a[i])

  if c == b[i]:
    print("정답")

  else:
    print("오답")