import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faBars, faEnvelope, faStickyNote} from "@fortawesome/free-solid-svg-icons";

import { faFacebook } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({img, name, role, facebookUrl, email, changeProfile, className, children}) {
    return (
        <div className={className}>
            <section>
                <nav className="menu">
                    <a href="#"><FontAwesomeIcon icon={faBars} /></a>
                    <a href="#"><FontAwesomeIcon icon={faStickyNote} /></a>
                </nav>

                <article className="profile">
                    <img src={img} alt="프로필 이미지" />

                    <h1>{name}</h1>
                    <h2>{role}</h2>

                    <a href="#" className="btnView">VIEW MORE</a>
                </article>

                <ul className="contact">
                    <li><FontAwesomeIcon icon={faFacebook} /><span><a href={facebookUrl}>{facebookUrl}</a></span></li>
                    <li><FontAwesomeIcon icon={faEnvelope} /><span>{email}</span></li>
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