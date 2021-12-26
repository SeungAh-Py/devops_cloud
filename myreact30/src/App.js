import PageAbout from "pages/PageAbout";
import PageCounter from "pages/PageCounter";
import PageLotto from "pages/PageLotto";
import PagePlayList from "pages/PagePlayList";
import TopNav from "components/TopNav";
import { useState } from "react";

function App() {
  const [pageName, setPageName] = useState("about");

  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };

  return (
    <div>
      <h1>김승아의 리액트</h1>
      <TopNav changePageName={setPageName} />
      {pageName === "about" && <PageAbout />}
      {pageName === "counter" && <PageCounter />}
      {pageName === "lotto" && <PageLotto />}
      {pageName === "playlist" && <PagePlayList />}
    </div>
  );
}


export default App;