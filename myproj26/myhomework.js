const { question } = require("readline-sync");

const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];


// TODO: 현재 timestamp
let start = Date.now();

// TODO: shuffle
function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}
shuffle(animal_names);


// answer_counter
let answerCounter = 0

for (let i = 0; i < 5; i++) {
    let shuffleAnimals = animal_names[i];
    console.log("typing start");
    const input = question(`${shuffleAnimals} : `);

    if (shuffleAnimals === input) {
        answerCounter++;
        console.log("Correct.");
    }
    else {
        console.log("Wrong Typing.");
    }
}

// TODO: 마침 timestamp
let end = Date.now();
let finishTime = (end - start) / 1000;
console.log(`${answerCounter}번 성공하셨습니다. ${finishTime} 초가 걸렸습니다.`)



// TODO: input 받기
//   readline-sync 라이브러리를 설치
//   소스코드가 있는 폴더까지 이동해서 !!!
//   npm install readline-sync



// string
// const number = question("Enter a number : ");
// console.log(number);


// TODO: slicing







