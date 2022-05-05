import React, { Suspense, lazy } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import { publicRoutes } from "./routesMap";
import { PrivateRoutes } from "../utils/privateRoutes";
import { useSelector } from "react-redux";
import { BrowserRouter as Router } from "react-router-dom";
import { mentorRoutes, studentRoutes } from "../router/routesMap";
import Header from "../containers/Header/header";
import Loader from "../containers/Loader/loader";

const PublicSide = lazy(() => import("../containers/PublicSide/publicSide"));

const Routes = () => {
  const userRole = useSelector(state => state.user.role);

  return (
    <Suspense fallback={<Loader />}>
      <Router>
        {/* <Loader /> */}
        <Header />
        {/* <PublicSide> */}
        <Switch>
          {publicRoutes.map(route => (
            <Route {...route} />
          ))}
          {/* {!localStorage.getItem('token') ? publicRoutes.map(route => (
            <Route {...route} />
          )): <Redirect to="/student" />}  */}

          <PrivateRoutes />

          <Redirect to="/" />
        </Switch>
        {/* </PublicSide> */}
      </Router>
    </Suspense>
  );
};

export default Routes;
