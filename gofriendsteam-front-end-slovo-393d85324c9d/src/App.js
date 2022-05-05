import React from "react";
// import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import "./App.css";
import Routes from "./router/routesWrapper";
import { Route } from "react-router-dom";
import "antd/dist/antd.css";
import fone from './img/fone.png'

const App = () => {
  return (
      <div className="App">
        <Routes />
      </div>
  );
};

export default App;
