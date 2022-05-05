import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Reset.module.css';
import { Formik } from 'formik';
import { resetPassword } from '../../../../actions/userActions';
import MyButton from '../../../Buttons/button';
import TextField from '@material-ui/core/TextField';
import { Icon as MaterialIcon } from '@material-ui/core';
import backgroundImg from "../../../../img/background.png";

const ResetPassword = props => {
  const validate = values => {
    let errors = {};
    if (!values.email) {
      errors.email = 'Заполните  поле Email';
    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
      errors.email = 'Невернный формат email!';
    }

    return errors;
  };
  const onSubmit = values => {
    resetPassword(values).then(() => {
      props.history.push('/');
    });
  };
  return (
    <div className={styles.formWrapper} styles={{ background:`url(${backgroundImg})` }}>

    <Formik
      initialValues={{
        email: ''
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
            <h2 className={styles.title}>Восстановление Пароля</h2>

            <div className={styles.inputs}>
              <TextField
                label="Ваш E-mail"
                name="email"
                fullWidth
                value={values.email}
                onChange={handleChange}
                helperText={errors.email}
                error={errors.email}
                margin="normal"
                variant="outlined"
              />
            </div>
          </div>
          <div className={styles.inputs}>
            <MyButton
              title="Отправить"
              fullWidth
              type="submit"
              myvariant="green"
            ></MyButton>
          </div>

          <div className={styles.inputs}>
            <MyButton
              fullWidth
              title="Попробовать войти"
              component={val => <Link {...val} />}
              to="/login"
              style={{
                textTransform: "initial",
                fontFamaly: "Proxima Nova",
                fontStyle: "normal",
                fontWeight: "normal",
                fontSize: "14px",
                lineHeight: "17px",
                margin: "0px 0px 10px"
              }}
            ></MyButton>
          </div>
        </form>
      )}
    </Formik>
    </div>
  );
};

export default ResetPassword;
