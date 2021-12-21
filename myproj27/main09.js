const { melon_data: song_array } = require("./melon_data");

// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const like_2thousands = song_array.filter(
    song => song.like >= 200000
).map(
    ({ title }) => title
);

console.log(like_2thousands);