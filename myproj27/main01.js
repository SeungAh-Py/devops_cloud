
const { melon_data: song_array, melon_data } = require("./melon_data");

console.log(song_array);

// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

melon_data.sort(
    (a, b) => (a.like - b.like)
);

for (const song of melon_data) {
    console.log(`[${song.like}] ${song.title}`)
};
