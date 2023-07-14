import React, { Component } from "react";
import { createRoot } from "react-dom/client";
import LoginPage from "./Login";
import ProjectManagerPage from "./ProjectManagerPage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
} from "react-router-dom";
import SignUp from "./SignUp";
import ResetAuthenticate from "./ResetAuthenticate";
import PromptPage from "./Prompt";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>

                <Router>
                    <Routes>
                        {/* Take care of the urls in frontend.urls.py after making change */}
                        <Route path="/" element={<PromptPage />}></Route>
                        <Route
                            exact
                            path="/login"
                            element={<LoginPage />}
                        ></Route>
                        <Route path="/sign_up" element={<SignUp />}></Route>
                        <Route
                            path="/project_manager"
                            element={<ProjectManagerPage />}
                        ></Route>
                        <Route
                            path="/reset-password"
                            element={<ResetAuthenticate />}
                        >
                            {" "}
                        </Route>
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
root.render(<App />);
