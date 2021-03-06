const { melon_data: song_array } = require("./melon_data");

// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const song_word_count = song_array.map(
    song => ({ title: song.title, length: song.title.split(' ').length })
)

for (const song of song_word_count) {
    console.log(`${song.title} ${song.length}`)
};