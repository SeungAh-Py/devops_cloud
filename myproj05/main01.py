import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        # print(song_dict["artist"], song_dict["title"], song_dict["like"])

        # 방법1
        line = "{}, {}, {}".format(
            song_dict["artist"], song_dict["title"], song_dict["like"]
        )
        # 방법2
        line = "{가수명}, {곡명}, {좋아요수}".format(
            가수명=song_dict["artist"], 곡명=song_dict["title"], 좋아요수=song_dict["like"]
        )
        # 방법3
        line = "{artist}, {title}, {like}".format(
            artist=song_dict["artist"], title=song_dict["title"], like=song_dict["like"]
        )
        # 방법4 (unpack arguments - **순수하게 사전에 있는 것에 대해서만 풀어주는(unpack) 명령어, 가장 많이 쓰임)
        line = "{artist}, {title}, {like}".format(**song_dict)
        print(line)
