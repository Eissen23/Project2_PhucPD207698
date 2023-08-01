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
    Grid,
    Tabs,
    Tab,
} from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import AuthContext from "../context/AuthContext";
import CustomTabPanel from "../utils/BasicTabs";

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

//handle the logic for custom tabs switch
function a11yProps(index) {
    return {
        id: `simple-tab-${index}`,
        "aria-controls": `simple-tabpanel-${index}`,
    };
}

export default function ProjectManagerPage() {
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

    const [value, setValue] = useState(0);

    useEffect(() => {
        fetch("/auth/user/me", {
            method: "GET",
            headers: { Authorization: "Bearer " + authToken["access"] },
        })
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

    const handleChange = (event, newValue) => {
        setValue(newValue);
    };

    if (loading) {
        return <h1>LOADING ....</h1>;
    } else {
        return (
            <ThemeProvider theme={hust}>
                <CssBaseline />
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={2} position="fixed">
                        <AppBar align="left">
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
                                <Container align="right" sx={{ display: { xs: "none", sm: "block" }, }}>
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
                                    <Typography variant="subtitle1" align="right" >
                                        Ngày tháng năm
                                    </Typography>
                                </Container>
                            </Toolbar>
                            <Container
                                component={Paper}
                                maxWidth={false}
                                sx={{ display: {xs: "none", sm: "block" } }}
                            >
                                <Box alignContent="left" alignSelf="left">
                                    <Tabs
                                        value={value}
                                        onChange={handleChange}
                                        aria-label="basic tabs example"
                                        textColor="black"
                                    >
                                        <Tab
                                            label="Trang chủ"
                                            {...a11yProps(0)}
                                        />
                                        <Tab
                                            label="Nhóm đồ án"
                                            {...a11yProps(1)}
                                        />
                                        <Tab label="Đề tài" {...a11yProps(2)} />
                                        <Tab label="Lịch" {...a11yProps(3)} />
                                        <Tab
                                            label="Tiến độ"
                                            {...a11yProps(4)}
                                        />
                                    </Tabs>
                                </Box>
                            </Container>
                        </AppBar>
                    </Grid>

                    <Grid item xs={8} sm={2} marginTop={15}>
                        <CustomTabPanel value={value} index={0}>
                            Content của trang chủ
                        </CustomTabPanel>

                        <CustomTabPanel value={value} index={1}>
                            Thông tin nhóm dồ án
                        </CustomTabPanel>

                        <CustomTabPanel value={value} index={2}>
                            Thông tin đề tài
                        </CustomTabPanel>

                        <CustomTabPanel value={value} index={3}>
                            Lịch chi tiết
                        </CustomTabPanel>

                        <CustomTabPanel value={value} index={4}>
                            Tiến độ
                        </CustomTabPanel>
                    </Grid>

                    <Grid item xs={4} marginTop={15}>
                        {/* For calendar */}
                    </Grid>
                </Grid>
            </ThemeProvider>
        );
    }
}
