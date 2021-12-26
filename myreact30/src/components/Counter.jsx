import { useState } from 'react';

function Counter({ initial, color }) {
        // 속성값을 초기값으로 참하여 상탯값 value를 생성
    const [value, setValue] = useState(initial);

    const handleClick = () => {
        setValue(value + 1); // 완벽한 코드는 x
    };
    
    const handleContextMenu = (e) => {
        // context menu의 기본 동작을 막음.
        e.preventDefault();
        setValue(value - 1);
    }

    return (
    <div 
    style= {{
        ...style, backgroundColor: color
    }} 
    onClick={handleClick}
    onContextMenu={handleContextMenu}
    >
        {value}
    </div>
    )
}

// 컴포넌트의 고정된 스타일을 지정할 떄 , 사용
const style = {
    width: "100px",
    height: "100px",
    borderRadius: "50px",
    lineHeight: "100px",
    textAlign: "center",
    color: "white",
    display: "inline-block",
    fontSize: "3rem",
    margin: "1rem",
    userSelect: "none",
  };

export default Counter;