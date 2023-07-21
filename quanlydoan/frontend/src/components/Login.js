import React, { Component, useContext } from "react";
import { useNavigate } from "react-router-dom";
import {
    Button,
    CssBaseline,
    TextField,
    FormControlLabel,
    Checkbox,
    Link,
    Paper,
    Box,
    Grid,
    Typography,
} from "@mui/material";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AuthContext from "../context/AuthContext";
//Todo: Fix backgroud and re theme the Present page
const defaultTheme = createTheme();

export default function LoginPage(){
        

    //for navigation and api calling
    const navigate = useNavigate();

    //original submit 
    // const handleSubmit = (event) => {
    //     event.preventDefault();
    //     const data = new FormData(event.currentTarget);
        
    //     const requestOption = {
    //         method: 'POST',
    //         headers:{'Content-Type': 'application/json'},
    //         body:JSON.stringify({
    //             email: data.get('email'),
    //             password:data.get('password'),
    //         }),
    //     };

    //     fetch('/api/token/', requestOption).then((respond) =>
    //         respond.json()
    //     ).then((data) => navigate("/project_manager/" + data['access'].toString()));
    //   };

      // new summit
      let { loginUser } = useContext(AuthContext);

        return (
            <ThemeProvider theme={defaultTheme}>
                <Grid container component="main" sx={{ height: "100vh" }}>
                    <CssBaseline />
                    <Grid item xs={false} sm={4} md={7} sx={
                            {
                                backgroundSize: 'cover',
                                backgroundPosition: 'center',
                            }
                    }>
                      <img src="../../static/images/bk_login.png"/>
                    </Grid>
                    <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
                        <Box
                            sx={{
                                my: 8,
                                mx: 4,
                                display: "flex",
                                flexDirection: "column",
                                alignItems: "center",
                            }}>
                            <Typography component="h1" variant="h5">
                                Đăng nhập
                            </Typography>
                            <Box component="form" noValidate onSubmit={loginUser} sx={{ mt: 1 }}>
                                <TextField margin="normal" required fullWidth id="email" label="Email" name="email" autoComplete="email" autoFocus/>
                                <TextField margin="normal" required fullWidth name="password" label="Mật khẩu" type="password" id="password" autoComplete="current-password"/>
                                <FormControlLabel
                                    control={
                                        <Checkbox value="remember" color="primary"/>
                                    }
                                    label="Lưu mật khẩu"
                                />
                                <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
                                    Đăng nhập
                                </Button>
                                <Grid container>
                                    <Grid item xs>
                                        <Link href="/reset-password" variant="body2">
                                            Quên mật khẩu?
                                        </Link>
                                    </Grid>
                                    <Grid item>
                                        <Link href="/sign_up" variant="body2">
                                            {"Không có tài khoản? Đăng ký"}
                                        </Link>
                                    </Grid>
                                </Grid>
                            </Box>
                        </Box>
                    </Grid>
                </Grid>
            </ThemeProvider >
        );
}
