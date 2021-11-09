"""
멜론 top 100 리스트에서
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 1) 리스트에 랭크된 가수는 총 몇 팀? (중복 제거한 가수명 리스트의 크기)

# 방법1
artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)
print(len(artist_list))

# 방법2
artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
print(len(artist_set))

# 방법3(List Comprehension)
artist_set = set([song_dict["artist"] for song_dict in song_list])
print(len(artist_set))

# 방법4(Set Comprehension)
artist_set = {song_dict["artist"] for song_dict in song_list}
print(len(artist_set))


# 2) 2곡 잇아 랭크된 가수는 몇 팀?


# 3) "방탄소년단"의 좋아요 총 합?
