"""
랜덤 숫자
hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다. 유저에게 10회의 기회를 줍니다.
 + 그 숫자를 정확히 맞췄다면, 몇번 만에 맞췄는지 출력
 +
"""

from random import randint

number = randint(1, 100)

for retry in range(1, 11):
    line = input(f"[{retry}] Try guess number : ")
    answer = int(line.strip() or 0)

    if answer == number:
        print(f"{retry}회 시도에 성공.")
        break
    elif answer < number:
        print("더 큰 수를 입력해주세요.")
    else:
        print("더 작은 수를 입력해주세요.")
else:
    print("다음 기회에 ...")
