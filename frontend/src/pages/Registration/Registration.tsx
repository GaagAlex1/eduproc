import "./Registration.css";
import { useState } from "react";
// import api from '../../api.tsx'
// import {useNavigate} from "react-router-dom";

export default function Registration() {
  const [email, setEmail] = useState('')
  const [subGroup, setSubGroup] = useState('')
  const [password, setPassword] = useState('')
    const [pageState, setPageState] = useState('student')
  // const navigate = useNavigate()

  const handleStatusChange = () => {
      if(pageState == "student"){
          setPageState("teacher")
      }
      else{
          setPageState("student")
      }
  }

  const handleLoginChange = (event) => {
    setEmail(event.target.value);
  };
  const handleSubGroupChange = (event) => {
    setSubGroup(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = () => {
    // event.preventDefault()
    // api.post('/auth/login', {email, password}, {withCredentials: true})
    //     .then(
    //         () => {
    //           return api.get('/auth/users/me', {withCredentials: true})
    //             .then((response)=>{
    //               const { id } = response.data
    //               navigate(`/login`)
    //       });
    //     })
  };

  return (
    <>
      <div className="authorization__backgroung">
        <form className="authorization__lay" onSubmit={handleSubmit}>
            <div className="state_switcher">
                {pageState === 'student' && <div className="state_switcher_button active">Студент</div>}
                {pageState ==='teacher' && <div className="state_switcher_button" onClick={handleStatusChange}>Студент</div>}

                {pageState === 'student' && <div className="state_switcher_button" onClick={handleStatusChange}>Преподаватель</div>}
                {pageState === 'teacher' && <div className="state_switcher_button active">Преподаватель</div>}
            </div>
          <h1 className="authorization__lay_text">Регистрация</h1>

          <div className="authorization__lay_inputs">
              {pageState === "student" &&
                  <div className="authorization__lay_inputs_input">
                    <label>Подгруппа</label>
                    <input
                    type="text"
                    value={subGroup}
                    placeholder="Подгруппа"
                    onChange={handleSubGroupChange}/>
            </div>}
            <div className="authorization__lay_inputs_input">
              <label>Почта</label>
              <input
                type="text"
                value={email}
                placeholder="Почта"
                onChange={handleLoginChange}
              />
            </div>
            <div className="authorization__lay_inputs_input">
              <label>Пароль</label>
              <input
                type="password"
                value={password}
                placeholder="Пароль"
                onChange={handlePasswordChange}
              />
            </div>
          </div>

          <button className="authorization__lay_button" type={'submit'}>
            Войти
          </button>
        </form>
      </div>
    </>
  );
}
