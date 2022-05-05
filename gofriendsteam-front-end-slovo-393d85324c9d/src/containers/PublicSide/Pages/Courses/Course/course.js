import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import girl from "../../../../../img/girl.png";
import { getCourse } from "../../../../../actions/userActions";
import styles from "./course.module.css";
// const host = "http://387d0007.ngrok.io";

const Course = props => {
  const [course, setCourse] = useState(null);
  useEffect(() => {
    getCourse(props.match.params.id).then(course => setCourse(course));
  }, []);

  console.log("course", course);

  return (
    course && (
      <div className={styles.courseWrapper}>
        {/* <div className={styles.courseTopCenter}>
          <div className={styles.courseTop}>
            <Link to={`/courses`} className={styles.return}>
              <p>&#8592; Вернуться к курсам</p>
            </Link>
            <div className={styles.title}>
              <h1>{course.title}</h1>
            </div>
            <div className={styles.description}>
              <p
                dangerouslySetInnerHTML={{
                  __html: course.description
                }}
              ></p>
            </div>
            <div className={styles.from}>
              <p>От {course.from_min_price}грн</p>
            </div>
          </div>
          <div className={styles.courseTopRight}>
            <img src={girl} className={styles.courseTopRightImg} />
          </div>
        </div> */}
        <div className={styles.courseTopCenter} style={{ background: `url(${course.full_image})`, filter: 'invert(0%)', zIndex: '0', backgroundRepeat: 'no-repeat', backgroundSize: 'cover' }}>
          <div className={styles.courseTop}>
            <Link to={`/courses`} className={styles.return}>
              <p>&#8592; Вернуться к курсам</p>
            </Link>
            <div className={styles.title}>
              <h1>{course.title}</h1>
            </div>
            <div className={styles.description}>
              <p
                dangerouslySetInnerHTML={{
                  __html: course.description
                }}
              ></p>
            </div>
            <div className={styles.from}>
              <p>От {course.from_min_price}грн</p>
            </div>
          </div>
          {/* <div className={styles.courseTopRight}>
            <img src={girl} className={styles.courseTopRightImg} />
          </div> */}
        </div>
        <div className={styles.coursePackages}>
          <div className={styles.coursePackagesTitle}>
            <h2>Пакети</h2>
          </div>
          <div className={styles.packagesWrapper}>
            {course &&
              course.packages.map(item => {
                return (
                  <div key={item.id} className={styles.coursePackage}>
                    <div className={styles.courseTitle}>
                      <p>{item.title}</p>
                    </div>
                    <div>
                      <div className={styles.courseDescription}>
                        <p
                          dangerouslySetInnerHTML={{
                            __html: item.description
                          }}
                        >
                          {/* {item.description} */}
                        </p>
                      </div>
                    </div>
                    <div className={styles.coursePrice}>
                      <p>Цена пакета {item.price}</p>
                    </div>
                    <Link to={`/package/${item.id}`} className={styles.button}>
                      <p>Подробнее</p>
                    </Link>
                  </div>
                );
              })}
          </div>
        </div>
      </div>
    )
  );
};

export default Course;
