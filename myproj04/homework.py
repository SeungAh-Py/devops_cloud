import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list

count = 0

for song in song_list:
    if "방탄소년단" in song["artist"]:
        count += 1
print(count)
