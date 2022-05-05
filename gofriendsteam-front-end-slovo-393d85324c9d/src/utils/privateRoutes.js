import React, { Fragment } from "react";
import { useSelector } from "react-redux";
import { Switch, Route, Redirect } from "react-router-dom";
import { mentorRoutes, studentRoutes } from "../router/routesMap";
import NavBar from "../containers/PrivateSide/Components/Navbar/NavBar";
import styles from './privateRoutes.module.css'

export const PrivateRoutes = ({ children }) => {
  const userRole = useSelector(state => state.user.role);
  console.log(userRole);

  if(!localStorage.getItem('token')) { 
    return <Redirect to="/login" />
  }
  if (userRole === "mentor") {
    return (
      <Switch>
        {mentorRoutes.map(route => (
          <Route {...route} />
        ))}

        <Redirect to="/" />
      </Switch>
    );
  } else {
    return (
      <div className={styles.wrapper}>
        <NavBar />
        <div className={styles.wrapperWithoutNav}>
        <Switch>
          {studentRoutes.map(route => (
            <Route {...route} />
          ))}

          {/* <Redirect to="/" /> */}
        </Switch>
        </div>
      </div>
    );
  }
};
