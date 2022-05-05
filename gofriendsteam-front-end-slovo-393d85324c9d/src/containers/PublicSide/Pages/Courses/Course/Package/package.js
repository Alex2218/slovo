import React, { Component, Fragment, useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";

import { getPackage, buyPackage } from "../../../../../../actions/userActions";
import styles from "./package.module.css";
import { notification, Modal } from "antd";
// const host = "http://387d0007.ngrok.io";
// const token = localStorage.getItem('token');

const Package = props => {
  const history = useHistory();
  const [packagee, setPackage] = useState(null);
  useEffect(() => {
    getPackage(props.match.params.id).then(packagee => setPackage(packagee));
  }, []);

  console.log("packagee", packagee);

  //   const [modal, setModal] = useState(false);

  const buyPack = props => {
    const token = localStorage.getItem("token");

    // console.log("token", token);
    if (token) {
      buyPackage({ package_id: packagee.id })
        .then(el => {
          notification.success({ message: el.msg });
        })
        .catch(err => {
          history.push("/login");
        });
    } else {
      // setModal(true)
      history.push("/login");
    }
  };

  const numLesson =
    packagee &&
    packagee.modules.map(mod => {
      return mod.lessons.length;
    });





  if (packagee) {
    let sum = 0;

    for (let num of numLesson) {
      sum = sum + num;
    }
    console.log("sum", sum);

    
    // function arraySum(array) {
    //   var sum = 0;
    //   for (var i = 0; i < array.length; i++) {
    //     sum += array[i];
    //   }
    //   console.log(sum);
    //   return sum;
    // }
    // console.log("arraySum", arraySum(numLesson));
    // const sumLesson = arraySum(numLesson)
    // console.log("sumLesson", sumLesson);
    // return sumLesson
  }
  // console.log("sum", sum);

  return (
    packagee && (
      <div className={styles.courseWrapper}>
        <div
          className={styles.courseTopCenter}
          style={{ background: `url(${packagee.course.full_image})`, filter: 'invert(0%)', zIndex: '0', backgroundRepeat: 'no-repeat', backgroundSize: 'cover' }}
        >
          <div className={styles.courseTop}>
            <Link to={`/courses`} className={styles.return}>
              <p>&#8592; Вернуться к курсам</p>
            </Link>
            <div className={styles.title}>
              <h1>{packagee.title}</h1>
            </div>
            <div className={styles.description}>
              <p
                dangerouslySetInnerHTML={{
                  __html: packagee.description
                }}
              >
                {/* {item.description} */}
              </p>
            </div>
            <div className={styles.from}>
              <p>{packagee.price} грн</p>
            </div>
            <button onClick={buyPack} className={styles.buyPack}>
            Записаться на курс
            </button>
            <div>
              <div className={styles.numModules}>Кол-во модулей: {packagee.modules.length}</div>
              {/* <div>{numLesson} уроков</div> */}
              <div></div>
              <div></div>
            </div>
          </div>
        </div>
        <div className={styles.coursePackages}>
          <div className={styles.coursePackagesTitle}>
            <h1>Программа пакета курса</h1>
          </div>
          <div className={styles.packagesWrapper}>
            {packagee.modules.map(modul => {
              return (
                <div key={modul.id} className={styles.module}>
                  <div className={styles.moduleLeft}>
                    <h2>{modul.title}</h2>
                  </div>
                  <div className={styles.moduleRight}>
                    <div className={styles.moduleRightTop}>
                      <p>{modul.title}</p>
                    </div>
                    <div className={styles.moduleRightBottom}>
                      {modul.lessons.map(lesson => {
                        return (
                          <div key={lesson.id}>
                            <div className={styles.moduleRightBottomOne}>
                              <p>- {lesson.title}</p>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                </div>
              );
            })}
            <button onClick={buyPack} className={styles.buyPackBlue}>
              Купить
            </button>
          </div>
        </div>
        {/* <Modal
          title="Basic Modal"
          visible={modal}
        //   onOk={this.handleOk}
        //   onCancel={this.handleCancel}
        >
          <p>Some contents...</p>
          <p>Some contents...</p>
          <p>Some contents...</p>
        </Modal> */}
      </div>
    )
  );
};

export default Package;
