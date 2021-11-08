"""
+ "방탄소년단" 곡명만 출력
+ 곡명에 "사랑"이 포함된 곡명만 출력하기
+ "좋아요" 수가 200,000 이상인 곡명만 출력하기
"""

from pprint import pprint
from typing import List  # type Hinting #파이썬의 타입힌팅기능 사용하기 위함
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 1. '방탄소년단' 곡명만 출력하기
# => '방탄소년단'의 곡명 문자열로 구성된 리스트를 만들어보세요.

# ===================================================
# sol.1
# title_list: List[str] = []

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단":
#         title: str = song_dict["title"]
#         title_list.append(title)

# print(title_list)
# ==================================================

# sol.2
# new_song_list: List[str] = []

# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist == "방탄소년단": # 필터(filter)의 조건 부합
#         new_song_list.append(song_dict)

# pprint(new_song_list)
# ==================================================


# sol.3-1 (filter함수 활용?)
def check_bts_song(song_dict):
    """
    BTS 노래라면 True를 반환합니다.
    """
    # ↑ 함수의 사용법을 작성하는 방법(밑에 if 함수에 check_bts_song 변수에 커서를 대면, 해당 내용이 뜸)
    # bts 노래라면 True를 리턴
    # 아니라면 False를 리턴
    artist: str = song_dict["artist"]
    return artist == "방탄소년단"


# new_song_list: List[str] = []

# for song_dict in song_list:
#     if check_bts_song(song_dict):
#         new_song_list.append(song_dict)

# pprint(new_song_list)
# ====================================================
# sol.3-2
new_song_list = list(filter(check_bts_song, song_list))  # 리스트화 시킨 것일뿐, 리스트는 아님
pprint(new_song_list)

# 단순히 print만 한다라고 한다면
for song_dict in filter(check_bts_song, song_list):
    print("{title} {artist} {like}".format(**song_dict))

# =====================================================

# 2. 곡명에 "사랑" 이 포함된 곡명만 출력하기
# => 곡명에 "사랑"이 포함된 곡들의 곡명 리스트를 만들어보세요.


def check_contains_love(song_dict):
    title: str = song_dict["title"]
    return "사랑" in title


for song_dict in filter(check_contains_love, song_list):
    print("{rank} {title}".format(**song_dict))


# title_list: List[str] = []
# for song_dict in song_list:
#     title: str = song_dict["title"]
#     if "사랑" in title:
#         title_list.append(title)

# print(title_list)

# # 3. '좋아요' tnrk 200,000 이상인 곡명만 출력하기
# # => ~ 곡들의 곡명 리스트를 만들어보세요.


def check_above_200000(song_dict):
    like: int = song_dict["like"]
    return like >= 200_000


for song_dict in filter(check_above_200000, song_list):
    print("{title} - {like}".format(**song_dict))

# title_list: List[str] = []

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     like: int = song_dict["like"]
#     if like >= 200_000:
#         title_list.append(title)

# print(title_list)
