import React, { Component, StrictMode, Fragment } from "react";
import { createRoot } from "react-dom/client";
import LoginPage from "./Login";
import ProjectManagerPage from "./ProjectManagerPage";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignUp from "./SignUp";
import ResetAuthenticate from "./ResetAuthenticate";
import PromptPage from "./Prompt";
import PrivateRoute from "../utils/PrivateRoute";
import AuthContext, { AuthProvider } from "../context/AuthContext";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <StrictMode>
                    <Router>
                        <Fragment>
                            <Routes>
                                {/* Take care of the urls in frontend.urls.py after making change */}
                                <Route path="/" element={<PromptPage />}></Route>

                                <Route path="" element={<AuthProvider />}>
                                    <Route exact path="/login" element={<LoginPage />}></Route>
                                    
                                    <Route path="/project_manager" element={<PrivateRoute />}>
                                        <Route path="" element={<ProjectManagerPage />} />
                                    </Route>

                                </Route>

                                <Route path="/sign_up" element={<SignUp />}></Route>
                                
                                <Route path="/reset-password" element={<ResetAuthenticate />}></Route>
                            </Routes>
                        </Fragment>
                    </Router>
                </StrictMode>
            </div>
        );
    }
}

const appDiv = document.getElementById("app");

const root = createRoot(appDiv);
root.render(<App />);
