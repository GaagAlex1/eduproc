import "./Profile.css";
import Input from "../../comps/Input/Input.tsx";
import Header from "../../comps/Header/Header.tsx";

export default function Profile() {
  return (
    <>
      <Header />
      <div className="profile">
        <img src="" alt="profIcon" />
        <div className="profile__info">
          <Input text="Фамилия" />
          <Input text="Имя" />
          <Input text="Отчество" />
        </div>
        <div className="course-info">
          <label>Информация о курсах</label>
          <ul>
            <li>Какой-то курс</li>
          </ul>
        </div>
      </div>
    </>
  );
}
