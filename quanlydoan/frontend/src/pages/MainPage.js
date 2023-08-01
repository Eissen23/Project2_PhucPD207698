import React from "react";
import  PropTypes  from "prop-types";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore"
const MainPage = (props) => {
    const {type, user, ...others} = props

    

    return (
        <div>

        </div>
    )
}

MainPage.propsTypes = {
    type: PropTypes.bool.isRequired,
    user: PropTypes.object.isRequired,
};

export default MainPage;