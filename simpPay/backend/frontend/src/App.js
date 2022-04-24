import './App.css';
import Header from "./components/header/Header"  ;
import Login from "./components/Login/Login" ;
import Home from "./components/Home/home"

import {
  BrowserRouter ,
  Route,
Routes
} from "react-router-dom";
function App() {
  return (
    <BrowserRouter>
    <Header/>
    <Routes>
    <Route  exact path ="/" element={<Home/>}/>
    <Route  path="/login" element={<Login/>}/>
    </Routes>

    </BrowserRouter>
  );
}

export default App;
