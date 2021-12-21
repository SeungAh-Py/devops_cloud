const { melon_data: song_array } = require("./melon_data");

// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

const like_2thousands = song_array.filter(
    song => song.like >= 200000
);

const asc_like = like_2thousands.sort(
    (a, b) => (b.like - a.like)
)

for (const song of asc_like) {
    console.log(`[${song.like}] ${song.title} ${song.artist}`)
}