import React, { Component } from 'react';
import { Link } from 'react-router-dom';


const Profile = ({ children }) => {
  console.log('asd');
  return (
    <div>
      Profile
      {/* <Link
        style={{ position: 'absolute', top: 20, left: 20, fontSize: 40 }}
        to="/"
      >
        HOME
        </Link>
      <div className="size-container content">
        {children}
      </div> */}
    </div>
  );
}

export default Profile;
