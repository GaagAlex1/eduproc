import "./Input.css"

export default function Input(props){
    return(
        <div className="input-block">
            <label>{props.text}</label>
            <input placeholder={props.text} type="text" value={props.value}/>
        </div>
    )
}