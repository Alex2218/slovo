import React, { useState, useEffect } from "react";
import { connect, useSelector, useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { Icon as MaterialIcon } from "@material-ui/core";
import styles from "./login.module.css";
import MyButton from "../../../Buttons/button";
import { login, socialLogin } from "../../../../actions/userActions";
import TextField from "@material-ui/core/TextField";
import { Formik } from "formik";
import SocialButton from "../../../Buttons/SocialButton/SocialButton";
// import Button from '@material-ui/core/Button';
import { Input } from "antd";
import googleIcon from "../../../../img/googleIcon.png";
import backgroundImg from "../../../../img/background.png";


// const FormItem = Form.Item;

const Login = ({ login, history, location }) => {
  const userRole = useSelector(state => state.user.role);
  const dispatch = useDispatch();
  // if (localStorage.getItem('token')) {
  //   if (userRole) {
  //     history.replace('/admin/main');
  //   }
  // }

  // const fromLocation =
  //   (location.state && location.state.from.pathname) || "/admin/main";

  const onSubmit = values => {
    login(values).then(res => {
      dispatch({
        type: "UPDATE_PROFILE",
        payload: res
      });
      if (res.user.done_form === false) {
        history.push("/questionnaire");
      } else if (res.role === "mentor") {
        history.push("/my_courses");
      } else {
        history.push("/my_courses");
      }
    });
  };
  const handleSocialLogin = user => {
    dispatch(socialLogin({token: user.token.accessToken})).then(res => {
      dispatch({
        type: "SOCIALLOGIN",
        payload: res
      });

      if (res.user.done_form === false) {
        history.push("/questionnaire");
      } else if (res.role === "mentor") {
        history.push("/my_courses");
      } else {
        history.push("/my_courses");
      }
      console.log("res", res);
    });

    console.log("success google login", user);
  };

  const handleSocialLoginFailure = err => {
    console.error(err);
  };

  const validate = values => {
    let errors = {};
    if (!values.email) {
      errors.email = "Заполните  поле Email";
    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
      errors.email = "Невернный формат email!";
    }
    if (!Boolean(values.password.trim())) {
      errors.password = "Введите пароль!";
    }
    return errors;
  };

  return (
    <div className={styles.formWrapper} >
      <Formik
        initialValues={{ email: "", password: "" }}
        validate={validate}
        onSubmit={onSubmit}
      >
        {({ values, errors, touched, handleChange, handleSubmit }) => (
          <form className={styles.form} onSubmit={handleSubmit}>
            <div>
              <h2 className={styles.title}>Войти в кабинет</h2>
              <div className={styles.inputs}>
                {/* <MaterialIcon style={{ margin: "30px 15px 0 0" }}>
                email
              </MaterialIcon> */}
                <TextField
                  label="E-mail"
                  name="email"
                  className={styles.textField}
                  value={values.email}
                  onChange={handleChange}
                  helperText={errors.email}
                  fullWidth
                  error={errors.email || (touched.email && errors.email)}
                  margin="normal"
                  variant="outlined"
                />
              </div>
              <div className={styles.inputs}>
                {/* <MaterialIcon style={{ margin: "30px 15px 0 0" }}>
                lock_outline
              </MaterialIcon> */}
                <TextField
                  label="Пароль"
                  name="password"
                  type="password"
                  className={styles.textField}
                  value={values.password}
                  onChange={handleChange}
                  fullWidth
                  helperText={errors.password}
                  error={
                    errors.password || (touched.password && errors.password)
                  }
                  margin="normal"
                  variant="outlined"
                />
              </div>
            </div>
            {/* <div className={styles.forgot}>
              <MyButton
                title="Забыли пароль?"
                component={prop => <Link {...prop} />}
                to="/auth/reset_password"
              ></MyButton>
            </div> */}
            <div className={styles.enterBtn}>
              <MyButton
                title="Войти"
                fullWidth
                type="submit"
                myvariant="green"
              ></MyButton>
            </div>
            <div className={styles.forgot}>
              <MyButton
                style={{
                  textTransform: "initial",
                  fontFamaly: "Proxima Nova",
                  fontStyle: "normal",
                  fontWeight: "normal",
                  fontSize: "14px",
                  lineHeight: "17px",
                  margin: "3px 0px"
                }}
                title="Забыли пароль?"
                component={prop => <Link {...prop} />}
                to="/reset_password"
              ></MyButton>
            </div>
            <div>
              <MyButton
                style={{
                  textTransform: "initial",
                  fontFamaly: "Proxima Nova",
                  fontStyle: "normal",
                  fontWeight: "normal",
                  fontSize: "14px",
                  lineHeight: "17px",
                  margin: "0px 0px 10px"
                }}
                component={prop => <Link {...prop} />}
                to="registration"
                fullWidth
                title="Регистрация"
              ></MyButton>
            </div>
            <div>
              <SocialButton
                style={{ border: "none", padding: "0px", cursor: "pointer" }}
                provider="google"
                appId="383231785741-50qq080nkmda5i4dp1gqa89cjknsrl01.apps.googleusercontent.com"
                onLoginSuccess={handleSocialLogin}
                onLoginFailure={handleSocialLoginFailure}
              >
                <img src={googleIcon}></img>
              </SocialButton>
            </div>
          </form>
        )}
      </Formik>
    </div>
  );
};

// const WrappedNormalLoginForm = Form.create()(Login);

const mapStateToProps = state => ({});

const mapDispatchToProps = dispatch => ({
  login: user => dispatch(login(user))
});

export default connect(mapStateToProps, mapDispatchToProps)(Login);
