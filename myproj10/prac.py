import random

# 난수 리스트 생성(1~99까지의 수 하나 추출)
ranNum = random.sample(range(1, 100), 1)
print("난수 : ", ranNum)

# 난수 testNum 변수에 저장
testNum = ranNum[0]

# 기억력 테스트 게임 시작
print("당신의 기억력을 테스트합니다.")
print("준비되셨습니까?")
print("1. yes / 2. no")

inputNum = int(input())
type(inputNum)

if inputNum == 1:
    for i in range(20):
        print()
        print()
        print("난수는?")
        myNum = int(input())

        if myNum == testNum:
            print("빙고~ 훌륭합니다.")
        else:
            print("아쉽습니다.")
else:
    print("게임을 종료합니다.")
