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
        <Grid container component="main" sx={{  direction:"row"    }}>
            <CssBaseline />
            <Grid
                item
                xs={12}
                sm={8}
                md={5}
                elevation={6}
                sx={{display: "flex", flexDirection: "row"}}
            >
                <Box 
                sx={{
                    p: 2,
                    display: "flex",
                    flexDirection: "row",
                    alignItems: "center",
                    justifyContent: 'space-between',
                }}>
                    <Typography component="h4" variant="h5">
                        Đã có tài khoản?
                    </Typography>
                    <Button   variant="contained" sx={{ mt: 3, mb: 2 }} href="/login">
                        Đăng nhập
                    </Button>
                </Box>

                <Box sx={{
                    p: 2,
                    display: "flex",
                    flexDirection: "row",
                    alignItems: "center",
                    justifyContent: 'space-between',
                }}>
                    <Typography component="h4" variant="h5">
                        Chưa có tài khoản?
                    </Typography>
                    <Button   variant="contained" sx={{ mt: 3, mb: 2 }} href="/sign_up">
                        Đăng ký
                    </Button>
                </Box>
            </Grid>
        </Grid>
        );
    }
}
