// 파이썬의 zip을 ES6로 구현
// https://stackoverflow.com/a/10284006
const zip = (...rows) =>
  [...rows[0]].map((_, column_index) => rows.map((row) => row[column_index]));

const get_random_lotto_numbers = () =>
  [...Array(45).keys()]
    .map((index) => index + 1)
    .sort(() => Math.random() - Math.random())
    .slice(0, 7)
    .sort((number1, number2) => number1 - number2);

const shuffle_array = (array) =>
  array.sort(() => Math.random() - Math.random());

export { zip, get_random_lotto_numbers, shuffle_array };
