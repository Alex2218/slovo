// import React, { Component, Fragment } from "react";
// import { Tooltip, Menu, Icon, Dropdown } from "antd";
// import { useSelector } from "react-redux";

// const { SubMenu } = Menu;

// const mentorMenu = [
//   {
//     title: "Мои курсы",

//     href: "main",
//     developing: true
//   },
//   {
//     title: "Каталог курсов",

//     href: "products",
//     developing: true
//   },
//   {
//     title: "Мои интересы",

//     href: "contractor_orders",
//     developing: true
//   },
//   {
//     title: "Библиотека видео",

//     href: "finance",
//     developing: true
//   }
// ];

// const studentMenu = [
//   {
//     title: "Мои курсы",

//     href: "main",
//     developing: true
//   },
//   {
//     title: "Каталог курсов",

//     href: "products",
//     developing: true
//   },
//   {
//     title: "Мои интересы",

//     href: "contractor_orders",
//     developing: true
//   },
//   {
//     title: "Библиотека видео",

//     href: "finance",
//     developing: true
//   }
// ];

// const NavBar = () => {

//     const userRole = useSelector(state => state.user.role);
//     console.log("userRole", userRole);

//     // const navigation =
//     // //   this.props.user.role === "mentor" ? mentorMenu : studentMenu;
//     // console.log("this.props.user.role", this.props.user.role);

//     return (
//       <div></div>
//       // <Menu
//       //   mode="inline"

//       //   theme="dark"
//       //   inlineCollapsed={asideMenu}
//       //   style={{ width: 165 }}
//       // >
//       //   <UserTopPanel goto={this.goto} user={user} asideMenu={asideMenu} />

//       //   {navigation.map((item, index) => {
//       //     if (item.children) {
//       //       return (
//       //         <SubMenu
//       //           key={index}
//       //           title={
//       //             <Fragment>
//       //               <Icon
//       //                 component={() => (
//       //                   <Fragment>
//       //                     <img
//       //                       src={item.icon}
//       //                       alt=""
//       //                       className="default-icon"
//       //                     />
//       //                     <img
//       //                       src={item.activeIcon}
//       //                       alt=""
//       //                       className="active-icon"
//       //                     />
//       //                   </Fragment>
//       //                 )}
//       //               />

//       //               <span
//       //                 style={{ color: '#fff', fontSize: '11px' }}

//       //               >
//       //                 {item.title}
//       //               </span>
//       //             </Fragment>
//       //           }
//       //         >
//       //           {item.children.map((subItem, index) =>
//       //             subItem.title !== 'Категории' ? (
//       //               <Menu.Item key={subItem.title}>
//       //                 <Link
//       //                   to={subItem.href}
//       //                   style={{ padding: '0 30px 0 30px', fontSize: '11px' }}
//       //                 >
//       //                   {subItem.title}
//       //                 </Link>
//       //               </Menu.Item>
//       //             ) : (
//       //                 <CategoryList
//       //                   key={index}
//       //                   title={subItem.title}
//       //                   style={{ color: '#fff', fontSize: '11px' }}
//       //                   categories={categories}
//       //                   onSelectCategory={this.handleChangeCategory}
//       //                 />
//       //               )
//       //           )}
//       //         </SubMenu>
//       //       );
//       //     } else if (item.developing) {
//       //       return (
//       //         <Menu.Item key={index} onClick={() => this.goto(item.href)}>
//       //           <Icon
//       //             component={() => (
//       //               <Fragment>
//       //                 <img src={item.icon} alt="" className="default-icon" />
//       //                 <img
//       //                   src={item.activeIcon}
//       //                   alt=""
//       //                   className="active-icon"
//       //                 />
//       //               </Fragment>
//       //             )}
//       //           />
//       //           <span
//       //             style={{ color: '#fff', fontSize: '11px' }}
//       //           >
//       //             {item.title}
//       //           </span>
//       //         </Menu.Item>
//       //       );
//       //     }
//       //   })}
//       // </Menu>
//     );
//   }

// export default NavBar;

import React, { Component } from "react";
import { Link, NavLink } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "antd/dist/antd.css";
// import HomePage from "../PublicSide/Pages/HomePage/homePage";
// import Courses from "../PublicSide/Pages/Courses/courses";
// import VideoLibrary from "../PublicSide/Pages/VideoLibrary/videoLibrary";
import styles from "./navbar.module.css";
import ava from "../../../../img/ava.jpeg";

const NavBar = () => {
  const userRole = useSelector(state => state.user.role);
  // const dispatch = useDispatch();
  // const logout = () => {
  //     dispatch({
  //         type: 'LOGOUT'
  //     });
  //     props.history.replace('/login')
  // }

  console.log("userRole", userRole);

  return userRole === "student" ? (
    <div className={styles.navbar}>
      <div className={styles.ava}>
        {/* <div
          style={{
            backgroundImage: `url(${ava})`,
            borderRadius: '100%', 
            backgroundPosition: '50% 50%',
            width: "153px",
            height: "153px",
            backgroundSize: "cover"
          }}
        ></div> */}
      </div>
      <div className={styles.menuWrapper}>
        {/* <div className={styles.name}>Максим</div> */}
        <div className={styles.menu}>
          <div className={styles.menuItem}>
            <NavLink to="/my_courses" activeClassName={styles.active}>
              Мои курсы
            </NavLink>
          </div>
          <div className={styles.menuItem}>
            <NavLink to="/private_courses" activeClassName={styles.active}>
              Каталог курсов
            </NavLink>
          </div>
          {/* <div className={styles.menuItem}>
            <NavLink to="/" activeClassName={styles.active}>
              Мои интересы
            </NavLink>
          </div> */}
          {/* <div className={styles.menuItem}>
            <NavLink to="/private_video" activeClassName={styles.active}>
              Мои видео
            </NavLink>
          </div> */}
        </div>
      </div>
    </div>
  ) : (
    <div>
      {/* <div className={styles.ava}></div> */}
      <div className={styles.menuWrapper}>
        {/* <div className={styles.name}>Максим</div> */}
        <div className={styles.menu}>
          <div className={styles.menuItem}>
            <NavLink to="/my_courses" activeClassName={styles.active}>
              Мои курсы
            </NavLink>
          </div>
          <div className={styles.menuItem}>
            <NavLink to="/private_courses" activeClassName={styles.active}>
              Каталог курсов
            </NavLink>
          </div>
          {/* <div className={styles.menuItem}>
            <NavLink to="/" activeClassName={styles.link}>
              Мои интересы
            </NavLink>
          </div> */}
          {/* <div className={styles.menuItem}>
            <NavLink to="/private_video" activeClassName={styles.active}>
              Мои видео
            </NavLink>
          </div> */}
        </div>
      </div>
    </div>
  );
};

export default NavBar;
