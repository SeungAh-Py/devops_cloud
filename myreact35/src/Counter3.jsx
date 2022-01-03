import { useReducer, useState } from "react";

//   2단계
function reducer(prevState, action) {
  const { type, amount, color } = action;

  if (type === "COUNT") {
    // 2단계 1번
    return { ...prevState, value: prevState.value + amount };
    // 2단계 2번
  } else if (type === "COLOR_CHANGE") {
    return { ...prevState, color: color };
  }
  return prevState;
}

function Counter3() {
  //   const [state, setState] = useState({ value: 0, color: "red" });
  // 2-3번
  const [state, dispatch] = useReducer(reducer, { value: 0, color: "red" });
  const { value, color } = state;

  // 2단계 1번
  const handlePlus = () => {
    //     const action = { type: "COUNT", amount: 1 };
    //     setState((prevState) => {
    //       return reducer(action, prevState);
    //     });
    //   };

    // 2-3번(+)
    dispatch({ type: "COUNT", amount: 1 });
  };

  const handleMinus = () => {
    //     const action = { type: "COUNT", amount: -1 };
    //     setState((prevState) => {
    //       return reducer(action, prevState);
    //     });
    //   };

    // 2-3번(-)
    dispatch({ type: "COUNT", amount: -1 });
  };

  // 2단계 2번
  const changeGreen = () => {
    //     const action = { type: "COLOR_CHANGE", color: "green" };
    //     setState((prevState) => {
    //       return reducer(action, prevState);
    //     });
    //   };

    // 2-3번(초록)
    dispatch({ type: "COLOR_CHANGE", color: "green" });
  };

  const changeBlue = () => {
    //     const action = { type: "COLOR_CHANGE", color: "blue" };
    //     setState((prevState) => {
    //       return reducer(action, prevState);
    //     });
    //   };

    // 2-3번(파랑)
    dispatch({ type: "COLOR_CHANGE", color: "blue" });
  };

  const changeRed = () => {
    //     const action = { type: "COLOR_CHANGE", color: "red" };
    //     setState((prevState) => {
    //       return reducer(action, prevState);
    //     });
    //   };

    // 2-3번(빨강)
    dispatch({ type: "COLOR_CHANGE", color: "red" });
  };

  // 1~5번
  // const [value, setValue] = useState(0);
  // const [color, setColor] = useState("red");

  // -----
  // 2번
  // const handlePlus = () => {setValue(value +1);}
  // const handleMinus = () => {setValue(value -1);}

  // ------
  // 3번
  // const Plus = () => {
  //     setValue((prevValue) => prevValue +1);
  // }

  // const Minus = () => {
  //     setValue((prevValue) => prevValue -1);
  // }

  // ----
  // 4번
  // const changeGreen = () => setColor("green")
  // const changeBlue = () => setColor("blue")
  // const changeRed = () => setColor("red")

  // ----
  // 5번
  // const changeGreen = () => {
  //     setColor(() => "green")
  // }
  // const changeBlue = () => {
  //     setColor(() => "blue")
  // }
  // const changeRed = () => {
  //     setColor(() => "red")
  // }

  // 6번

  // const handlePlus = () => {
  //     return setState({...setState,
  //         value: state.value + 1
  //     })
  // }

  //   const handlePlus = () => {
  //     setState((prevState) => ({ ...prevState, value: prevState.value + 1 }));
  //   };

  //   const handleMinus = () => {
  //     setState((prevState) => {
  //       return { ...prevState, value: prevState.value - 1 };
  //     });
  //   };

  //   const changeGreen = () => {
  //     setState((prevState) => {
  //       return { ...prevState, color: "green" };
  //     });
  //   };
  //   const changeBlue = () => {
  //     setState((prevState) => {
  //       return { ...prevState, color: "blue" };
  //     });
  //   };
  //   const changeRed = () => {
  //     setState((prevState) => {
  //       return { ...prevState, color: "red" };
  //     });
  //   };

  return (
    <div>
      <h2>Counter3</h2>
      <div
        style={{
          ...defaultStyle,
          backgroundColor: color,
        }}
      >
        {value}
      </div>
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
      <button onClick={changeGreen}>Green</button>
      <button onClick={changeBlue}>Blue</button>
      <button onClick={changeRed}>Red</button>
    </div>
  );
}

const defaultStyle = {
  width: "100px",
  height: "100px",
  borderRadius: "50px",
  lineHeight: "100px",
  textAlign: "center",
  display: "inline-block",
  fontSize: "3rem",
  userSelect: "none",
};

export default Counter3;
