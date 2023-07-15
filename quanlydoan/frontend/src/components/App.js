import React, { Component, StrictMode } from "react";
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
import { createTheme, ThemeProvider, StyledEngineProvider  } from '@mui/material/styles';
import { red } from '@mui/material/colors';

export default class App extends Component {
    constructor(props) {
        super(props);
        const hust = createTheme({
            palette: {
                primary: {
                    main: red[500],
                },
                secondary: {
                    main: "#d9d9d9",
                },
                background: {
                    default: "#aa1d2b",
                },
            },
        });
        this.appTheme = hust;
    }


    render() {
        

        return (
            <div>
                <StrictMode>
                <ThemeProvider theme={this.appTheme}>
                    <StyledEngineProvider injectFirst>
                        
                            <Router>
                                <Routes>
                                    {/* Take care of the urls in frontend.urls.py after making change */}
                                    <Route
                                        path="/"
                                        element={<PromptPage />}
                                    ></Route>
                                    <Route
                                        exact
                                        path="/login"
                                        element={<LoginPage />}
                                    ></Route>
                                    <Route
                                        path="/sign_up"
                                        element={<SignUp />}
                                    ></Route>
                                    <Route
                                        path="/project_manager/:id"
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
                    </StyledEngineProvider>
                </ThemeProvider>
                </StrictMode>
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
// take the component render it inside index.html
// render(<App />, appDiv); #alternative
const root = createRoot(appDiv);
root.render(<App />);
