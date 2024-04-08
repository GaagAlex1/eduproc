import "./Course.css";
import {Link} from "react-router-dom";

export default function Course(props) {
  return (
    <Link to={`/courses/${props.id}`} className="course">
      {props.name}
      {/*<img src={props.name} alt="" />*/}
    </Link>
  );
}
