const { melon_data: song_array } = require("./melon_data");

// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

const filter_bts = song_array.filter(
    song => song.artist === "방탄소년단"
).reduce(
    (prev_val, cur_val) => (prev_val + cur_val.like), 0
);

console.log(filter_bts);