today = "2024년-10월-10일-월요일"

myday1 = today[6:9 + 10:13] # 어떤 결과?
# myday1 = today[6:(9 + 10):13] 로 인식한다.

myday2 = today[6:15:2]                                        # 6에서 15까지 2씩 건너뛰면서 출력해라.

myday3 = today[6:12:2]
#6부터 12까지 한글자 건너 한글자 띄엄띄엄
myday4 = today[12:6:-2] 
#위에거 반대로
myday5 = today[6:9] + today[10:13]
#두개를 각각 가져와서 합하기
print(myday3)
