today = "2024년-10월-10일-월요일"

myday1 = today[6:9 + 10:13] # 어떤 결과?

myday2 = today[6:15:2]                                        # 6에서 15까지 2씩 건너뛰면서 출력해라.

myday3 = today[6:12:-1]

myday4 = today[12:6:-1] 

myday5 = today[6:9] + today[10:13]

print(myday3)
