import random

for cd in 5, 4, 3, 2, 1, "hey!":
    print(cd)

spells = [
    "Riddikulus!",
    "Wingardium Leviosa!",
    "Avada Kedavra!",
    "Expecto Patronum!",
    "Nox!",
    "Lumos!",
]
print(spells[3])

quotes = {
    "Moe": "A wi1se guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk, nyuk!",
}
stooge = "Larry"
print("Moe", "says:", "바보")

numbers = 1
print(type(numbers))

# 불변객체(아래 내용) / 가변객체(list, tuple, dictionary)
x = 5
print(x)

y = 5
print(y)

x = 29
print(x)

print(y)

# 연습문제
# 2. 정수 99를 변수 prince에 할당하고 출력해보자

prince = 99
print(prince)

# 2-1. 값 5는 어떤 타입?

if type(5) == int:
    print("correct!")
else:
    print("wrong!")

# 2-2. 값 2.0은 어떤 타입

if type(2.0) == float:
    print("correct!")
else:
    print("wrong!")

# 2-3. 표현식 5 + 2.0은 어떤 타입?

if type(5 + 2.0) == float:
    print("correct!")
else:
    print("wrong!")

# 2-4. 예외 문제!

if print(type(5 + 2.0)) == print(float):
    print("correct!")
else:
    print("wrong!")

# 4-8 연습문제
# 4-1)
secret = random.randint(1, 10)
guess = random.randint(1, 10)

if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

start = "Na" * 4 + "\n"
middle = "Hey" * 3 + "\n"
end = "Goodbye."
print(start + start + middle + end)

thing = "wereduck"
place = "werepond"
print(f"The {thing:>20} is in the {place:.^20}")
