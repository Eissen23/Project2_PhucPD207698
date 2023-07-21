import React, { createContext, useState, useEffect } from "react";
import { Outlet, json, useNavigate } from "react-router-dom";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = () => {
    const navigate = useNavigate();

    let [authToken, setToken] = useState(
        localStorage.getItem("authToken")
            ? JSON.parse(localStorage.getItem("authToken"))
            : null
    );

    let loginUser = async (event) => {
        event.preventDefault();
        let respond = await fetch("/api/token/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                email: event.target.email.value,
                password: event.target.password.value,
            }),
        });
        let data = await respond.json();

        if (respond.status === 200) {
            setToken(data);
            localStorage.setItem("authToken", JSON.stringify(data));
            navigate("/project_manager");
        } else {
            alert("Something went wrong");
        }
    };


    let contextData = {
        loginUser: loginUser,
        authToken: authToken,
    };

    return (
        <AuthContext.Provider value={contextData}>
            <Outlet />
        </AuthContext.Provider>
    );
};
