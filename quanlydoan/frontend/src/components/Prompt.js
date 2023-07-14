import React, { Component } from "react";
import {
    Box,
    Button,
    CssBaseline,
    Paper,
    Grid,
    Typography,
} from "@material-ui/core";
import { createTheme, ThemeProvider } from "@mui/material/styles";

export default class PromptPage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return(
        <Grid container spacing={2} component="main" justifyContent="flex-end"  sx={{  direction:"row",  }}>
            <CssBaseline />
            <Grid
                item
                elevation={6}
                p={2}
                sx={{display: "flex", flexDirection: "row"}}
            >
                <Box 
                sx={{
                    p: 2,
                    display: "flex",
                    justifyContent: 'space-evenly',
                    flexDirection: "row",
                    alignItems: 'flex-end',
                }}>
                    <Button   variant="contained" sx={{p:2}} href="/login">
                        Đăng nhập
                    </Button>
                    <Button   variant="contained" sx={{p:2}} href="/sign_up">
                        Đăng ký
                    </Button>
                </Box>
                
            </Grid>
        </Grid>
        );
    }
}
