# 숫자 퀴즈
# 랜덤 숫자를 맞춰보세요.

# hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.

# 유저에게 10회의 기회를 줍니다. - for/range
# 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는 지 출력
# 입력한 숫자가 랜덤수보다 작다면, "더 큰수를 입력해주세요." 라고 출력
# 입력한 숫자가 랜덤수보다 크다면, "더 작은 수를 입력해주세요." 라고 출력
# 횟수를 초과했다면, "다음 기회에 ..." 라고 출력

import random

input("랜덤 숫자를 맞춰보세요.")

random_number = random.randint(1, 100)

ok_counter = 0

for answer in range(10):
    line = int(input(">>> "))
    ok_counter += 1
    if random_number == line:
        print(f"{ok_counter}번 만에 맞췄습니다.")
        print("게임을 종료합니다.")
        break
    elif random_number < line:
        print("더 작은 수를 입력해주세요.")
    else:
        print("더 큰 수를 입력해주세요.")
else:
    print("게임을 종료합니다2")
