import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faBars, faEnvelope, faStickyNote} from "@fortawesome/free-solid-svg-icons";

import { faFacebook } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({profile_image_url, name, role, instagram_url, mbti, className, children}) {
    return (
        <div className={className}>
            <section>
                <nav className="menu">
                    <a href="#"><FontAwesomeIcon icon={faBars} /></a>
                    <a href="#"><FontAwesomeIcon icon={faStickyNote} /></a>
                </nav>

                <article className="profile">
                    <img src={profile_image_url} alt="프로필 이미지" />

                    <h1>{name}</h1>
                    <h2>{role}</h2>

                    <a href="#" className="btnView">VIEW MORE</a>
                </article>

                <ul className="contact">
                    <li><FontAwesomeIcon icon={faFacebook} /><span><a href={instagram_url}>{instagram_url}</a></span></li>
                    <li><FontAwesomeIcon icon={faEnvelope} /><span>{mbti}</span></li>
                </ul>

                {/* 멤버별 프로필 링크 */}
                <nav className="others">
                    {children}
                </nav>
            </section>
        </div>          
        
    );
}

export default ProfileCard;