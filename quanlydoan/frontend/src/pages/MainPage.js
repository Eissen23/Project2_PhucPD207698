import React, { useContext, useEffect, useState } from "react";
import  PropTypes  from "prop-types";
import AuthContext from "../context/AuthContext";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore"
import { Typography } from "@material-ui/core";
const MainPage = (props) => {
    const {token, user, ...others} = props

    

    let [groupdata, setGroupData] = useState([])
    let [is_fetched, setFetch] = useState(false)
    useEffect(() => {
        if (user.is_teacher)
        {
            fetch("/auth/user/manageclass", {
                method: "GET",
                headers: { Authorization: "Bearer " + token },
            }).then(async (respond) => respond.json()).then((data) => setGroupData(data))
        }else{
            fetch("/auth/user/manageclass", {
                method: "GET",
                headers: { Authorization: "Bearer " + token },
            }).then(async (respond) => respond.json()).then((data) => setGroupData(data))
        }

        if(!is_fetched)
            setFetch(true)
    }, []);    

    console.log(groupdata)

    if(is_fetched)
        return (
            
            <div>
                
            </div>
        )

    else
        return
            <div>Fetching ...</div>
}

MainPage.propsTypes = {
    token: PropTypes.string.isRequired,
    user: PropTypes.object.isRequired,
};

export default MainPage;