import "./Authorization.css";
import { useState } from "react";
import api from '../../api.tsx'
import {useNavigate} from "react-router-dom";

export default function Authorization() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleLoginChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault()
    api.post('/auth/login', {email, password}, {withCredentials: true})
        .then(
            () => {
              return api.get('/auth/users/me', {withCredentials: true})
                .then((response)=>{
                  const { id } = response.data
                  navigate(`/${id}/home`)
          });
        })
  };

  return (
    <>
      <div className="authorization__backgroung">
        <form className="authorization__lay" onSubmit={handleSubmit}>
          <h1 className="authorization__lay_text">Авторизация</h1>
          <div className="authorization__lay_inputs">
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
