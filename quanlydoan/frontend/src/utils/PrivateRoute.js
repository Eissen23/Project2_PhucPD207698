import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import AuthContext from '../context/AuthContext';


const PrivateRoute = () => {
    let {authToken} =   useContext(AuthContext) // determine if authorized, from context or however you're doing it

    // If authorized, return an outlet that will render child elements
    // If not, return element that will navigate to login page
    return authToken ? <Outlet /> : <Navigate to="/login" />;
}
export default PrivateRoute;