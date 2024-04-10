import "./Welcome.css";
import { Link } from "react-router-dom";

export default function Welcome(){
  return (
    <div className="welcome__background">
      <div className="welcome__lay">
        <h1>EDUPROC</h1>
        <h2>Добро пожаловать</h2>
        <div className="welcome__links">
          <Link to="/login" className="welcome__links_link">
            Войти
          </Link>
          <Link to="/registration" className="welcome__links_link">
            Создать аккаунт
          </Link>
        </div>
      </div>
    </div>
  );
};