import React, { useContext, useState, useEffect } from "react";
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

    let [loading, setLoad] = useState(true);

    let { authToken } = useContext(AuthContext);

    let [user, setUser] = useState({
        fullName: "",
        email: "",
        is_teacher: false,
        code: "",
        malop: "",
        sdt: "",
        domain: "",
    });

    const requestOption = {
        method: "GET",
        headers: { Authorization: "Bearer " + authToken["access"] },
    };

    // to stop fetch every rendering
    useEffect(() => {
        fetch("/auth/user/me", requestOption)
            .then(async (respond) => respond.json())
            .then((data) => {
                setUser(() => {
                    if (!data.user.is_teacher) {
                        return {
                            fullName: data.user.fullName,
                            email: data.user.email,
                            is_teacher: false,
                            code: data.detail.masv,
                            malop: data.detail.malop,
                            sdt: data.detail.sdt,
                            domain: data.detail.nganh,
                        };
                    } else {
                        return {
                            fullName: data.user.fullName,
                            email: data.user.email,
                            is_teacher: true,
                            code: data.detail.magv,
                            malop: "",
                            sdt: "",
                            domain: data.detail.vien,
                        };
                    }
                });
                setLoad(false);
            });
    }, []);

    if (loading) {
        return <h1>LOADING ....</h1>;
    } else {
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
                                <Typography variant="subtitle1">
                                    {user.fullName}
                                </Typography>
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
                        <TabContext>
                            <Box alignContent="left" alignSelf="left">
                                <List>
                                    {sections.map((item) => (
                                        <Button key={item} sx={{ color: "black" }}>
                                            {item}
                                        </Button>
                                    ))}
                                </List>
                            </Box>
                        </TabContext>
                    </Container>
                </AppBar>

                <Box sx={{ flexGrow: 1 }}>
                    <Grid container spacing={2}>
                        <Grid item xs={8}>

                        </Grid>

                        <Grid item xs={4}>
                            {/* For calendar */}
                        </Grid>
                    </Grid>
                </Box>
            </ThemeProvider>
        );
    }
}
