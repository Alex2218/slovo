import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./publicSide.module.css";
import Header from '../Header/header'


const PublicSide = ({ children }) => {
  return (
  <>
  <Header/>
  </>
  );
}

export default PublicSide;
