import React from 'react';
import { useDispatch } from 'react-redux';
import { Link, useHistory } from "react-router-dom";
import { StylesProvider } from '@material-ui/core';
import styles from './logOut.module.css'

const LogOut = props => {
    const dispatch = useDispatch();
    const history = useHistory();

    const logout = () => {
        dispatch({
            type: 'LOGOUT'
        });
        console.log('propsadasdasd', props)
        // props.history.replace('/login')
        history.push("/login");
    }
    return (
        <>
        
        <button className={styles.button} onClick={logout}>Выход</button>
        </>
    )
}

export default LogOut;