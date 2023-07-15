import React, { Component } from "react";
import {
    Typography,
    AppBar,
    CssBaseline,
    Container,
    Toolbar,
    Avatar,
    Button,
    Paper,
    List,
    Box,
} from "@material-ui/core";
import { withRouter } from "react-router";
const sections = ["Trang chủ", "Nhóm đồ án", "Dề tài", "Lịch", "Tiến độ"];

//nTODO: Turn this into a function asap

export default class ProjectManagerPage extends Component {
    constructor(props) {
        super(props);
        this.state ={ 
            fullName: null,
            email: null,
        };
    }

    render() {
        return (
            <div>
                <AppBar
                    align="left"
                    sx={{ color: "background.default" }}
                    elevation={5}
                >
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
                        <Container align="right">
                            <Avatar align="right"></Avatar>
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
                                    <Button key={item} sx={{ color: "#fff" }}>
                                        {item}
                                    </Button>
                                ))}
                            </List>
                        </Box>
                    </Container>
                </AppBar>
            </div>
        );
    }
}
