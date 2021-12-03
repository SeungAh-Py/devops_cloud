"""
Quiz : 멜론 top 100 리스트에서 ...
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# "좋아요" 수가 가장 많은 곡은? 가장 작은 곡은?


def pick_like_for_song(song_dict):
    return song_dict["like"]


# song_list가 빈 리스트일 경우 대처#1
song_dict = max(song_list, key=pick_like_for_song, defalut=None)
if song_dict == None:
    print("노래목록이 비었습니다.")
else:
    print(song_dict)

# song_list가 빈 리스트일 경우 대처#2
try:
    song_dict = max(song_list, key=pick_like_for_song)
except ValueError:
    print("노래목록이 비었습니다.")
else:
    print(song_dict)

# song_list가 빈 리스트일 경우 대처#3
if song_list:
    song_dict = max(song_list, key=pick_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다.")


# "곡명" 단어수가 가장 많은 곡은? 가장 작은 곡은?


def pick_title_maxium_words(song_dict):
    return song_dict["title"]


song_dict = max(song_list, key=pick_title_maxium_words)
print(song_dict)


# "곡명" 글자수가 가장 많은 곡은? 가장 작은 곡은?
