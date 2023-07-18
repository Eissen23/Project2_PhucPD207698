import React, { Component } from "react";
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
import { useParams } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
const sections = ["Trang chủ", "Nhóm đồ án", "Dề tài", "Lịch", "Tiến độ"];

export default function ProjectManagerPage() {
    const { id } = useParams();
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
                            <Typography>{id}</Typography>
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
        </ThemeProvider>
    );
}
