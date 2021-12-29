import PageLotto from "./components/PageLotto";
import ProfileCard from "./components/ProfileCard";
import userInfoList from "./data/userInfo.json";
import { useState } from "react";

const userIdList = userInfoList.map(({ userid }) => userid);

function App() {
  const [selectedId, setUserId] = useState(userIdList[0]);

  return (
    <div>
      {userInfoList.map((userinfo, index) => {
        const className = `user${index % 4}`;
        if (selectedId === userinfo.userid) {
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
                    className={selectedId === userinfo.userid ? "on" : ""}
                    onClick={() => setUserId(userinfo.userid)}
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
