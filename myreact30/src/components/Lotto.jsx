import { useState } from "react";
import Ball from "./Ball";

function LottoNumber() {
    const [NumberList, setNumberList] = useState([]);
    const randomInt = () => {
        let ranNumList = [];

        for (let i = 0; i < 7; i++) {
            let num = Math.floor(Math.random() * 44) + 1;
            
            for (const j in ranNumList) {
                if (num == ranNumList[j]) {
                    num = Math.floor(Math.random() * 44) + 1;
                }
            }
        ranNumList.push(num);
    }
    ranNumList.sort(function (a, b) {
        return a - b;
    });
    return ranNumList;
};

const handleClick = () => {
    setNumberList(randomInt)
};

return (
    <>
        <button onClick={handleClick}>
            번호 점지
        </button>
        <ul>
            <li style={{listStyle:'none'}}>
            {NumberList.map((number) => (
                <Ball number = {number} />
            ))}
            </li>
        </ul>
    </>
);

};

export default LottoNumber;
