import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

// TODO remove, this demo shouldn't need to reset the theme.

export default function SignUp() {
    // for check logic
    const [isTeacher, setIsTeacher] = React.useState(false);

    const handleChange = (event) => {
        setIsTeacher(event.target.checked);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);

        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                fullName: data.get("fullName"),
                email: data.get("email"),
                password: data.get("password"),
                re_password: data.get("re_password"),
                is_teacher: isTeacher,
                code: data.get("code"),
                malop: data.get("malop"),
                sdt: data.get("phone"),
                domain: data.get("domain"),
            }),
        };

        fetch("/auth/user/signup", requestOption).then((respond) => respond.json()).then((data) => data.success ? alert(data.success) : alert(data.error));
    };

    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <Box
                sx={{
                    marginTop: 8,
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}></Avatar>
                <Typography component="h1" variant="h5">
                    Đăng ký tài khoản
                </Typography>
                <Box
                    component="form"
                    noValidate
                    onSubmit={handleSubmit}
                    sx={{ mt: 3 }}
                >
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <TextField
                                autoComplete="given-name"
                                name="fullName"
                                required
                                fullWidth
                                id="fullName"
                                label="Họ và tên"
                                autoFocus
                            />
                        </Grid>

                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                id="email"
                                label="Email"
                                name="email"
                                autoComplete="email"
                            />
                        </Grid>

                        <Grid item xs={12} sm={6}>
                            <TextField
                                name="code"
                                required
                                fullWidth
                                id="code"
                                label="MSSV/Mã GV"
                                autoFocus
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                required
                                fullWidth
                                id="malop"
                                label="Mã Lớp (sinh viên)"
                                name="malop"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="domain"
                                label="Ngành/Khoa"
                                id="domain"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="phone"
                                label="Số điện thoại (sinh viên)"
                                id="phone"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="password"
                                label="Mật khẩu"
                                type="password"
                                id="password"
                                autoComplete="new-password"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="re_password"
                                label="Nhập lại mật khẩu"
                                type="password"
                                id="re_password"
                                autoComplete="new-password"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <FormControlLabel
                                control={
                                    <Checkbox
                                        value="isTeacher"
                                        color="primary"
                                        onChange={handleChange}
                                    />
                                }
                                label="Đây là tài khoản cho giảng viên"
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        color="secondary"
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign Up
                    </Button>
                    <Grid container justifyContent="flex-end">
                        <Grid item>
                            <Link href="/login" variant="body2">
                                Đã có tài khoản? Đăng nhập ngay
                            </Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Container>
    );
}
