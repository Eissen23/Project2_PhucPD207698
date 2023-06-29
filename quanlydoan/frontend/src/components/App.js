import React, {Component} from "react";
import {createRoot} from "react-dom/client"
import LoginPage from "./HomePage";
import ProjectManagerPage from "./ProjectManagerPage";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom"
import SignUp from "./SignUp";

export default class App extends Component{
    
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div>
                <Router>
                <Routes>
                    <Route exact path="/sign_in" element= {<LoginPage/>}></Route>
                    <Route path="/sign_up" element= {<SignUp/>}></Route>
                    <Route path="/project_manager" element= {<ProjectManagerPage />} ></Route>
                    
                </Routes>
            </Router>
            </div>
        );
    }
}


const appDiv = document.getElementById("app");
// take the component render it inside index.html
// render(<App />, appDiv); #alternative
const root = createRoot(appDiv);
root.render(<App/>);