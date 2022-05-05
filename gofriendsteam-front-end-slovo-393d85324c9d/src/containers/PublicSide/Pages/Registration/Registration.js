import React from 'react';
import { Link } from 'react-router-dom';

import MyButton from '../../../Buttons/button';
import styles from './Registration.module.css';
import { Icon as MaterialIcon } from '@material-ui/core';
import ConfirmRegistration from './ConfirmRegistration';
import TextField from '@material-ui/core/TextField';
import { Formik } from 'formik';
import googleIcon from "../../../../img/googleIcon.png";
import SocialButton from "../../../Buttons/SocialButton/SocialButton";

import { useDispatch } from 'react-redux';
import {registration, socialLogin} from '../../../../actions/userActions';
import backgroundImg from "../../../../img/background.png";

// const rolesMap = ['MENTOR', 'STUDENT'];

const Registration = ({ history, ...props }) => {
  const dispatch = useDispatch();
  const validate = values => {

    let errors = {};
    if (!values.email) {
      errors.email = 'Заполните  поле Email';
    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
      errors.email = 'Невернный формат email!';
    }
    if (!Boolean(values.password.trim())) {
      errors.password = 'Введите пароль!';
    }
    if (!Boolean(values.confirm_password.trim())) {
      errors.confirm_password = 'Введите пароль!';
    }
    if (values.confirm_password !== values.password) {
      errors.password = 'пароли не совпадают';
      errors.confirm_password = 'пароли не совпадают';
    }
    if (!/^\+38[0-9]{10}$/i.test(values.phone)) {
      errors.phone = 'Невернный телефон!';
    }
    return errors;
  };
  const [value, setValue] = React.useState(0);
  const [confirmState, setOpenConfirm] = React.useState(false);

  const handleCloseConfirm = () => {
    props.history.push('/auth/login');
    setOpenConfirm(false);
  };
  // const handleChangeT = (event, newValue) => {
  //   setValue(newValue);
  // };
  const goto =  () => {
    props.history.push('/login')
  }
  const onSubmit = values => {
    const iseMentor = /role=mentor/g.test(props.location.search);
    console.log(iseMentor, props.location);
    const obj = {
      ...values,
      role: iseMentor ? 'mentor' :'student'
    };
    dispatch(registration(obj, props.history))
    // registration(obj).then(res => {
    //   setOpenConfirm(true);
    // });
  };

  const handleSocialLogin = user => {
    dispatch(socialLogin(user._profile)).then(res => {
      dispatch({
        type: "SOCIALLOGIN",
        payload: res
      });

      if (res.success === true) {
        history.push("/questionnaire");
      } else if (res.role === "mentor") {
        history.push("/mentor");
      } else {
        history.push("/student");
      }
      console.log("res", res);
    });

    console.log("success google login", user);
  };

  const handleSocialLoginFailure = err => {
    console.error(err);
  };
 
  return (
    <div className={styles.formWrapper} styles={{ background:`url(${backgroundImg})` }}>

    <Formik
      initialValues={{
        email: '',
        password: '',
        confirm_password: '',
        surname: '',
        name:'',
        phone: ''
      }}
      validate={validate}
      onSubmit={onSubmit}
    >
      {({
        values,
        errors,
        handleChange,
        handleSubmit
      }) => (
        <form className={styles.form} onSubmit={handleSubmit}>

          <div>
            <h2 className={styles.title}>Регистрация</h2>
            <div className={styles.inputs}>
              <TextField
                label="Имя"
                name="name"
                fullWidth
                value={values.name}
                onChange={handleChange}
                helperText={errors.name}
                error={errors.name}
                variant="outlined"
              />
            </div>
            <div className={styles.inputs}>
              <TextField
                label="Фамилия"
                name="surname"
                fullWidth
                value={values.surname}
                onChange={handleChange}
                helperText={errors.surname}
                error={errors.surname}
                variant="outlined"
              />
            </div>
            <div className={styles.inputs}>
              <TextField
                label="Ваш телефон"
                name="phone"
                fullWidth
                value={values.phone}
                onChange={handleChange}
                helperText={errors.phone}
                error={errors.phone}
                variant="outlined"
              />
            </div>
            <div className={styles.inputs}>
              <TextField
                // autoComplete={false}
                label="Ваш E-mail"
                name="email"
                fullWidth
                value={values.email}
                onChange={handleChange}
                helperText={errors.email}
                error={errors.email}
                variant="outlined"
              />
            </div>
            <div className={styles.inputs}>
              <TextField
                name="password"
                fullWidth
                type="password"
                value={values.password}
                onChange={handleChange}
                label="Пароль"
                helperText={errors.password}
                error={errors.password}
                variant="outlined"
              />
            </div>
            <div className={styles.inputs}>
              <TextField
                label="Повторите пароль"
                name="confirm_password"
                type="password"
                fullWidth
                value={values.confirm_password}
                onChange={handleChange}
                helperText={errors.confirm_password}
                error={errors.confirm_password}
                variant="outlined"
              />
            </div>
            
          </div>
          {/* <MyButton
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
              ></MyButton> */}
          <div className={styles.inputs}>
           
            <MyButton
              title="Зарегистрироваться"
              fullWidth
              
              type="submit"
              myvariant="green"
            ></MyButton>
          </div>
          <div className={styles.inputs}>
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
              title="У меня уже есть аккаунт"
              component={val => <Link {...val} />}
              to="/login"
              fullWidth
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
          <ConfirmRegistration
            open={confirmState}
            handleClose={handleCloseConfirm}
          />
        </form>
      )}
    </Formik>
    </div>

  );
};

// const WrappedNormalRegistrationForm = Form.create()(Registration);

export default Registration;



