import PageLotto from "./components/PageLotto";
import ProfileCard from "./components/ProfileCard";
// import userInfoList from "./data/userInfo.json";
import { useState, useEffect } from "react";
import Axios from "axios";

function App() {
  const [userInfoList, setProfileList] = useState([]);

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((reponse) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(reponse.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [selectedId, setUserId] = useState(`bts-jin`);

  return (
    <div>
      {userInfoList.map((userinfo, index) => {
        const className = `user${index % 4}`;
        if (selectedId === userinfo.unique_id) {
          return (
            <ProfileCard
              {...userinfo}
              className={className}
              // name={userinfo.name}
              // role={userinfo.role}
              // facebookUrl={userinfo.facebookUrl}
              // email={userinfo.email}
              changeProfile={setUserId}
              img={`/profile-images/member${index + 1}.jpg`}
            >
              {userInfoList.map((userinfo) => {
                return (
                  <a
                    className={selectedId === userinfo.unique_id ? "on" : ""}
                    onClick={() => setUserId(userinfo.unique_id)}
                  ></a>
                );
              })}
            </ProfileCard>
          );
        }
      })}

      <h1>번호 추출</h1>
      <PageLotto />
    </div>
  );
}

export default App;
