# 문자열을 인수로 받아 단어수를 반환하는 함수
def get_word_count(s):
    return len(s.split())


print(get_word_count("우리는 파이썬을 즐겨요"))


# 문자열을 인자로 받아, 공백을 제외한 글자수를 반환하는 함수
# "우리는 파이썬을 즐겨요"를 인자로 받아, 10을 반환


def get_ch_count_except_space(s):
    count = 0
    for ch in s:
        if ch != " ":
            count += 1

    return count


print(get_ch_count_except_space("우리는 파이썬을 즐겨요"))


#


def get_rounded_number(number):
    return (number // 1000) * 1000


print(get_rounded_number(1234567))
