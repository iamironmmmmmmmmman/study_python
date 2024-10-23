import time

people = {
    "이름" : "정유감",
    "나이" : 17,
    "직업" : "여고생",
    "특기" : ["십자수", "뜨개질", "요리"],
    "취미" : "씹덕질",
    "money" : 1300,
    "소지품" : []
    }

if people["money"] >= 4000: # 떡볶이는 4000원임
    print("떡볶이를 먹는다")
    people["money"] -= 4000
    people["소지품"].append("떡볶이")
elif people["money"] >= 2000 : # 피카츄 돈가스 2000원이라 치고
    print("삐카츄 동까스 먹지 뭐")
    people["money"] -= 2000
    people["소지품"].append("피돈")
elif people["money"] >= 1000 : 
    print("배고픈데 물이라도 마셔야겠다")
    people["money"] -= 900
    people["소지품"].append("생수")
else:
    print("굶어야지 뭐")

time.sleep(2)

print(people)

