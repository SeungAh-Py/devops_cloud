from typing import List


import random

def check_available(received_text: str) -> bool:
    return received_text in ("로또", "로또번호 점지해줘")

def make_response(received_text: str, candidate_numbers: List[int] = None) -> str:
    if candidate_numbers is None:
        candidate_numbers = random.sample(range(1, 46), 7)
    * numbers, bonus = random.sample(range(1, 46), 7)
    predict_numbers: str = ", ".join(map(str, sorted(numbers)) # 숫자 리스트를 문자 리스트로 바꾸는 맵핑)
    message = f"로또번호는 {predict_numbers} 이며, 보너스 번호는 {bonus}이니다."
    return message

