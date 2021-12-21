const { melon_data: song_array } = require("./melon_data");

// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const filter_bts = song_array.filter(
    song => song.artist === "방탄소년단"
);

const song_bts = filter_bts.map(
    ({ title }) => title
)

console.log(song_bts)
