import "./Home.css";
import Header from "../../comps/Header/Header.tsx";

export default function Home() {
  return (
    <>
      <Header />
      <div className="home">
        <div className="home__item home__statistics">
          <h1>Статистика</h1>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error,
            excepturi facilis mollitia nam nemo nesciunt sint vitae. Aliquid est
            minima, quae repellat saepe vitae. Error fuga incidunt iusto quidem
            ratione!
          </p>
        </div>
        <div className="home__item home__deadlines">
          <h1>Дедлайны</h1>
        </div>
        <div className="home__item home__recent">
          <h1>Недавние</h1>
        </div>
        <div className="home__item home__to-do">
          <h1>Надо сделать</h1>
        </div>
      </div>
    </>
  );
}
