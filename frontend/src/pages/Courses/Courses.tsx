import "./Courses.css";
import api from "../../api.tsx";
import Header from "../../comps/Header/Header.tsx";
import {useEffect, useState} from "react";
import Course from "../../comps/Course/Course.tsx";

export default function Courses() {
    const [courses, setCourses] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = () => {
            api.get('course/courses', {withCredentials: true})
                .then(response => {
                    setCourses(response.data)
                    setError(null)
                })
                .catch(reason => {
                    if (reason.response.status === 401) {
                        api.post('auth/refresh', {}, {withCredentials: true})
                            .then(() => {
                                return api.get('course/courses', {withCredentials: true})
                            })
                            .then(response => {
                                setCourses(response.data)
                                setError(null)
                            })
                    }
                })
        }

        fetchData()
    }, [])

  return (
      <>
        <Header/>
        <div className="courses">
          {(courses.map((course) => {
              return Course(course)
          }))}
        </div>
      </>

  );
}
