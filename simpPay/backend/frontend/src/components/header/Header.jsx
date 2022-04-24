import "./header.css" ;  
import {Link} from "react-router-dom" ; 
export default function Header () {
    return(
       <div className="top">
       <div className="topLeft">
          <div className="Icon">SimpPay</div>
       </div>
       <div className="topCenter">
        <ul className=""></ul>
       </div>
       <div className="topRight">
           <ul className="topList">
      <li className="topListItem" style={{"color":"black"}}><Link className="link" to="/login">LOGIN / SIGNUP</Link></li>
           </ul>
       </div>
       </div>

    )
}
