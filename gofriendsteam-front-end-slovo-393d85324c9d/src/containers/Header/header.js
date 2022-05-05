import React, { Component } from "react";
import { Link, NavLink } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "antd/dist/antd.css";
import HomePage from "../PublicSide/Pages/HomePage/homePage";
import Courses from "../PublicSide/Pages/Courses/courses";
import VideoLibrary from "../PublicSide/Pages/VideoLibrary/videoLibrary";
import LogOut from "../Buttons/LogOut/logOut";
import styles from "./header.module.css";
import logo from "../../img/logo.png";

const Header = () => {
  const userRole = useSelector(state => state.user.role);
  // const dispatch = useDispatch();
  // const logout = () => {
  //     dispatch({
  //         type: 'LOGOUT'
  //     });
  //     props.history.replace('/login')
  // }
  return userRole ? (
    <header className={styles.headerWrapper}>
      <nav className={styles.headerNav}>
        <div>
          <img className={styles.logo} src={logo} />
        </div>
        <div className={styles.linksWrapper}>
          {/* <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/home">
              О Slovo
            </NavLink>
          </div> */}
          <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/private_courses">
              Курсы
            </NavLink>
          </div>
          {/* <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/my_video">
              Библиотека видео
            </NavLink>
          </div> */}
        </div>
        {/* <div>
          <NavLink to="/login">
            Вход
          </NavLink>
        </div> */}
        <LogOut />
        {/* <button onClick={logout}>Log out</button> */}
      </nav>
    </header>
  ) : (
    <header className={styles.headerWrapper}>
      <nav className={styles.headerNav}>
        <div>
          <img className={styles.logo} src={logo} />
        </div>
        <div className={styles.linksWrapper}>
          {/* <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/home">
              О Slovo
            </NavLink>
          </div> */}
          <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/courses">
              Курсы
            </NavLink>
          </div>
          {/* <div className={styles.linkItem}>
            <NavLink activeClassName={styles.active} to="/video">
              Библиотека видео
            </NavLink>
          </div> */}
        </div>
        <div className={styles.linkItem}>
          <NavLink activeClassName={styles.active} to="/login">
            Вход
          </NavLink>
        </div>
      </nav>
    </header>
  );
};

export default Header;
