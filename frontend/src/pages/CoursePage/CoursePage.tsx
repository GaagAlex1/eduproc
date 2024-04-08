import "./CoursePage.css";
import {useParams} from "react-router-dom";
import Header from "../../comps/Header/Header.tsx";

export default function CoursePage() {
  const { courseId } = useParams();
  return (
      <>
          <Header/>
          <div className="course-page">
              <h1 className="course-page__head">{courseId}</h1>
              <ul className="course-page__task-list">
                  {/*{tasks.map(task => (<Task {...task}/>))}*/}

              </ul>
          </div>
      </>

  );
}
