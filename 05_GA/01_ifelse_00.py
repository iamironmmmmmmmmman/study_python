myHand = "가위"
herHand = "바위"

if myHand == herHand:
    print("비겼다")
elif myHand == "가위" and herHand == "보": # else if
    print("이겼다")
elif myHand == "바위" and herHand == "가위":
    print("이겼다")
elif myHand == "보" and herHand == "바위":
    print("이겼다")
else:
    print("졌다!!!") # "가위" "바위"


