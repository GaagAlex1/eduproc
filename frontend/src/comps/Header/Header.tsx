import "./Header.css";
import messageIcon from "./message.png";
import notificationIcon from "./notification.png";
import profileIcon from "./profile.png";
import Messenger from "../Messenger/Messenger.tsx";
import { useState } from "react";
import Notifications from "../Notifications/Notifications.tsx";
import logo from "./Logo.png";
import { Link, useParams } from "react-router-dom";

export default function Header() {
  const { userId } = useParams();
  const [showNotifications, setShowNotifications] = useState(false);
  const [showMessenger, setShowMessenger] = useState(false);

  return (
    <header>
      <div className="header__item header__logo">
        <img src={logo} alt="" />
        <label>EDUPROC</label>
      </div>
      <nav className="header__item header__nav">
        <Link to={`/${userId}/home`}>Главная</Link>
        <Link to={`/${userId}/courses`}>Курсы</Link>
        <Link to={`/${userId}/profile`}>Профиль</Link>
      </nav>
      <div className="header__item header__profile">
        <img
          src={notificationIcon}
          alt="Notification"
          onClick={() => setShowNotifications(!showNotifications)}
        />
        <img
          src={messageIcon}
          alt="Message"
          onClick={() => setShowMessenger(!showMessenger)}
        />
        <img src={profileIcon} alt="Profile" />
      </div>
      {showMessenger && <Messenger />}
      {showNotifications && <Notifications />}
    </header>
  );
}
