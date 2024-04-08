import "./Task.css";
import {Link} from "react-router-dom";

export default function Task(props) {
  return (
    <Link to={`/courses/${props.taskId}`} className="task">
      {props.taskName}
        <p>{props.taskDescription}</p>
    </Link>
  );
}
