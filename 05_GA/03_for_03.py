import time

people = {
    "이름" : "정유감",
    "나이" : 17,
    "직업" : "미필_여고생",
    "특기" : ["십자수", "뜨개질", "요리"],
    "취미" : "씹덕질",
    "money" : 10000,
    "소지품" : ["k2", "군번줄"],
    "전역까지" : {"남은 일" : 10}
    }

for people["전역까지"]["남은 일"] in range(people["전역까지"]["남은 일"], 0, -1) :
    print(f'{people["이름"]}이 눈을 감고 한숨을 쉽니다. 전역까지 {people["전역까지"]["남은 일"]}일 남았네. 또르르... 잠이 듭니다.')
    time.sleep(0.5)

# people["전역까지"]["남은 일"] -= 1 
# for문 안에서 나올때 1일이었음.
# 종료값이 포함되지 않는다는 말!☆☆☆

time.sleep(1)
print(f'{people["이름"]}은 전역까지 {people["전역까지"]["남은 일"]}일 남았다.')
time.sleep(1)
print(f'병장 {people["이름"]} 전역을 명 받았습니다!')