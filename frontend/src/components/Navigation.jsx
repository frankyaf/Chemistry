import { Link } from "react-router-dom";

export function Navigation(){
  return (
    <div>
        <nav>
            <ul>
                <li><Link to="/Card">Card</Link></li>
                <li><Link to="/Game">Game</Link></li>
            </ul>
        </nav>
    </div>
  )
}