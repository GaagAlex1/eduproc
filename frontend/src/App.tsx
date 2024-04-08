import Home from "./pages/Home/Home.tsx";
import Courses from "./pages/Courses/Courses.tsx";
import Profile from "./pages/Profile/Profile.tsx";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CoursePage from "./pages/CoursePage/CoursePage.tsx";
import Welcome from "./pages/Welcome/Welcome.tsx";
import Authorization from "./pages/Authorization/Authorization.tsx";
import Registration from "./pages/Registration/Registration.tsx";

export default function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Welcome />} />
          <Route path="/login" element={<Authorization />} />
          <Route path="/registration" element={<Registration />} />
          <Route path="/:userId/home" element={<Home />} />
          <Route path="/:userId/courses" element={<Courses />} />
          <Route path="/:userId/profile" element={<Profile />} />
          <Route path="/:userId/courses/:courseId" element={<CoursePage />} />
          {/*<Route path="*" element={<ErrorPage/>} />*/}
          {/*<Route path="courses/:courseId/:taskId" element={<TaskPage />} />*/}
        </Routes>
      </Router>
    </>
  );
}
