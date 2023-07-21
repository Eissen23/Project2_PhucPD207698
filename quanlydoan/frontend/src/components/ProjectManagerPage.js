import React, { Component, useContext } from "react";
import {
    Avatar,
    AppBar,
    List,
    Toolbar,
    CssBaseline,
    Box,
    Typography,
    Paper,
    Container,
    Button,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import AuthContext from "../context/AuthContext";
const sections = ["Trang chủ", "Nhóm đồ án", "Dề tài", "Lịch", "Tiến độ"];

export default function ProjectManagerPage() {
    
    const hust = createTheme({
        palette: {
            primary: {
                main: "#aa1d2b",
            },
            common: {
                black: "#0000",
            },
        },
    });

    let user = {
        fullName: null,
        email: null,
        code: null,
        malop: null,
        sdt: null, 
        domain: null,
        is_teacher: false,
    }
    
    let { authToken } = useContext(AuthContext);    
    
    const requestOption = {
        method: 'GET',
        headers: {'Authorization' : 'Bearer ' + authToken["access"]},
    };

    fetch('/auth/user/me', requestOption).then((respond) =>
        respond.json()
    ).then((data) => {
        user.fullName =  data.user.fullName;
        user.email = data.user.email;
        is_teacher = data.user.is_teacher;
        
        if(!is_teacher){
            code = data.detail.masv;
            malop = data.detail.malop;
            sdt = data.detail.sdt;
            domain = data.detail.nganh;
        }else{
             code = data.detail.magv;
             domain = data.detail.vien;
        }
    });

    return (
        <ThemeProvider theme={hust}>
            <AppBar align="left" elevation={5}>
                <CssBaseline />
                <Toolbar>
                    <img
                        width="55pt"
                        height="82pt"
                        src={
                            "https://storage.googleapis.com/hust-files/5807675312963584/images/hust-logo-official_.3m.jpeg"
                        }
                        alt="hust_logo"
                    />
                    <Container align="left">
                        <Typography variant="h5">
                            Hệ thống quản lý bộ môn đồ án
                        </Typography>
                        <Typography variant="subtitle1">
                            ĐẠI HỌC BÁCH KHOA HÀ NỘI
                        </Typography>
                    </Container>
                    <Container
                        align="right"
                        sx={{ display: { xs: "none", sm: "block" } }}
                    >
                        <Box
                            alignContent="right"
                            display="flex"
                            flexDirection="row"
                            alignItems="center  "
                            justifyContent="flex-end"
                            sx={{
                                columnGap: 3,
                            }}
                        >
                            <Typography></Typography>
                            <Avatar align="right"></Avatar>
                        </Box>
                        <Typography variant="subtitle1" align="right">
                            Ngày tháng năm
                        </Typography>
                    </Container>
                </Toolbar>
                <Container
                    component={Paper}
                    maxWidth={false}
                    sx={{ display: { xs: "none", sm: "block" } }}
                >
                    <Box alignContent="left" alignSelf="left">
                        <List>
                            {sections.map((item) => (
                                <Button key={item} sx={{ color: "black" }}>
                                    {item}
                                </Button>
                            ))}
                        </List>
                    </Box>
                </Container>
            </AppBar>

            {/* Set up tabular and calendar just like the practice*/}
        </ThemeProvider>
    );
}
