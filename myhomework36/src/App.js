import { useState } from "react";
// import Counter from "./Counter";
// import Counter2 from "./Conter2";
import Counter3 from "./Counter3";
import SevenNumbers1 from "./SevenNumbers1";
import SevenNumbers2 from "./SevenNumbers2";

function App() {
  // return <Counter3 />;
  return (
    <div>
      <SevenNumbers1 title="useState 버전" />
      <hr />
      <SevenNumbers2 title="useReducer 버전" />
    </div>
  );
}

export default App;
