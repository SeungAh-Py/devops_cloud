const { melon_data: song_array } = require("./melon_data");

// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const rank_two_over = song_array.reduce(
    (acc_val, cur_val) => {
        acc_val[cur_val] = (acc_val[cur_val] || 0) + 1;
    },
    {});

for (const result of rank_two_over) {
    console.log(result);
}


