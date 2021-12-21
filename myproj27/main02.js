const { melon_data: song_array } = require("./melon_data");

// TODO: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

const filter_bts = song_array.filter(
    song => song.artist === "방탄소년단"
);

for (const song of filter_bts) {
    console.log(`${song.artist} ${song.title} ${song.like}`)
};