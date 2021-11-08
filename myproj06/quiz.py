from typing import List
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 각 곡의 좋아요 수와 곡명의 글자수의 곱을 출력해보세요.

# 1) for/if로 구현
artist_length = []
for song_dict in song_list:
    if len(song_dict["artist"]) >= 3:
        title: str = song_dict["title"]
        like: int = song_dict["like"]
        artist_length.append([title, len(title), like])

for title, length, like in artist_length:
    print(f"{title} - {len(title)} * {like} = ", int(length) * like)

# ============ 1) 교수님 풀이 ========================

new_song_list: List[dict] = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if len(artist) >= 3:
        value:int = song_dict["like"] * len(song_dict["title"])
        #new_song_list.append(dict(song_dict, value=value))
        #위의 코드가 아래코드와 비슷하게 동작하는 코드(32~38라인)
        new_song_list.append({
            "title": song_dict["title"],
            "artist": song_dict["artist"],
            "like": song_dict["like"],
            "album": song_dict["album"],
            "rank": song_dict["rank"],
            "value": value,
        })

for value in new_song_list:
    print("{title} / {value}".format(**song_dict))

# 2) filter/map 위주로 구현

def artist_length_3():
    