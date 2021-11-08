import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# print(song_list)

"""
방탄소년단의 곡명만 출력해보세요.
hint : for 루프 내에서 if 조건문을 통해, "가수" 필드 체크
"""

for song_dict in song_list:
    song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])

"""
곡명에 "가을"이 들어가는 곡명만 출력
"""

for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])

"""
좋아요 수가 200_000이 넘는 곡수?
"""

song_count = 0

for song_dict in song_list:
    if song_dict["like"] > 200_000:
        song_count += 1
print(f"좋아요가 200,000이 넘는 곡은 {song_count}곡입니다.")


"""
가수 별 곡수를 출력?
"""
artist_dict = {}

for song_dict in song_list:
    artist: str = song_dict["artist"]
    
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1

print(artist_dict)