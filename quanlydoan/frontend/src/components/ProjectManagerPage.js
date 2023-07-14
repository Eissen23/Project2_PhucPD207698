import React, { Component } from "react";
import {
    Typography,
    AppBar,
    Card,
    CssBaseline,
    Container,
    Grid,
    Toolbar,
    CardContent,
    Avatar,
    Button,
    Paper,
    List,   
    Box,
    Breadcrumbs,
} from "@material-ui/core";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { light } from "@material-ui/core/styles/createPalette";

const sections = [
    "Trang chủ" ,
    "Nhóm đồ án" ,
    "Dề tài" ,
    "Lịch" ,
    "Tiến độ" ,
];

export default class ProjectManagerPage extends Component {
    constructor(props) {
        super(props);
        
    }
    render() {
        const theme = createTheme();
        return (
            <div>
                <ThemeProvider theme={theme}>
                    <CssBaseline />
                    <AppBar align='left' >
                        <Toolbar sx={{bgColor: "error.main"}} >
                            <img
                                width="55pt"
                                height="82pt"
                                src={
                                    "https://storage.googleapis.com/hust-files/5807675312963584/images/hust-logo-official_.3m.jpeg"
                                }
                                alt="hust_logo"
                            />
                            <Container align="left" >
                                <Typography variant="h5">
                                    Hệ thống quản lý bộ môn đồ án
                                </Typography>
                                <Typography variant="subtitle1">
                                    ĐẠI HỌC BÁCH KHOA HÀ NỘI
                                </Typography>
                            </Container>
                            <Container align="right">
                                <Avatar align="right"></Avatar>
                                <Typography variant="subtitle1" align="right">
                                    Ngày tháng năm
                                </Typography>
                            </Container>
                        </Toolbar>
                        <Container component={Paper} maxWidth={false} sx={{ display: { xs: 'none', sm: 'block' }}}>
                            <Box alignContent='left' alignSelf='left'  >
                                <List >
                                    {sections.map((item)=>(
                                        <Button key={item} sx={{ color: '#fff' }}>
                                        {item}
                                      </Button>
                                    ))}
                                </List>
                            </Box>
                        </Container>
                    </AppBar>
                </ThemeProvider>
            </div>
        );
    }
}
