import { useState } from "react";

function makeLottoNumbers() {
    const ranNumList = [];

    for (let i = 0; i<7; i++) {
        let num = Math.floor(Math.random() * 44) + 1;

        for (let j in ranNumList) {
            if (num == ranNumList[j]) {
                num = Math.floor(Math.random() * 44) + 1;
            }
        }

        ranNumList.push(num);
    }
    ranNumList.sort(function(a,b) {
        return a - b;
    })
    return ranNumList
};


function PageLotto () {
    const [numberList, setNumberList] = useState([11, 12, 13, 14, 15, 16, 17]);

    const clickListener = () => {
        setNumberList(makeLottoNumbers());
    };

    return (
        <>
            <h2>Lotto</h2>  
            <button onClick={clickListener}>
                예지
            </button>
            <div>
                {numberList.map(
                    (number) => <span style={{
                        display: 'inline-block', 
                        fontSize: '2rem', 
                        margin: '10px',
                        }}>{number}</span>)}
            </div>            
        </>
    )
};



export default PageLotto;