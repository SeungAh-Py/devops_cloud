const { melon_data: song_array } = require("./melon_data");

// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const love_embed_title = song_array.filter(
    song => song.title
        .includes("사랑")
    // 결괏값 확인
    // console.log(love_embed_title)
).map(
    ({ title }) => title
);

console.log(love_embed_title);

