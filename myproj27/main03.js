const { melon_data: song_array } = require("./melon_data");

// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

const top10_song_list = song_array.sort(
    (a, b) => (b.like - a.like)
).slice(0, 10)


for (const song of top10_song_list) {
    console.log(`[${song.like}] ${song.title} ${song.artist}`)
};
