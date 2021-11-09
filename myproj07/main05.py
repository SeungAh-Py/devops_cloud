"""
멜론 top 100 리스트에서
"""
from collections import defaultdict, Counter
from pprint import pprint
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 2) 2곡 잇아 랭크된 가수는 몇 팀?

# idea1. 가수별로 곡이 올라가 있는 곡의 수가 있으면 좋음

# 풀이1

artist_list = [song_dict["artist"] for song_dict in song_list]

# song_count_dict = {}  # key : artist, value: song count
# for artist in artist_list:
#     if artist not in song_count_dict:
#         song_count_dict[artist] = 0
#     song_count_dict += 1

# pprint(song_count_dict)

# 풀이2


# song_count_dict = defaultdict(int)
# for artist in artist_list:
#     song_count_dict += 1


# 풀이3

song_count_dict = Counter(artist_list)

# 풀이3-1 : 나름 괜찮은 코드
artist_count_above_2 = 0
for song_count in song_count_dict.values():
    if song_count >= 2:
        artist_count_above_2 += 1

pprint(artist_count_above_2)


# 풀이3-2
def check_above_1(song_count):
    return song_count > 1


print(len(list(filter(check_above_1, song_count_dict.values()))))
