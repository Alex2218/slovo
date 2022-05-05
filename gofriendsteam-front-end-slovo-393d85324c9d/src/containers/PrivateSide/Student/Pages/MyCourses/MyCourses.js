import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { myCourses } from "../../../../../actions/userActions";
// import styles from "./courses.module.css";
import styles from "./myCourses.module.css";

const MyCourses = props => {
  const [myCoursess, setMyCourses] = useState(null);

  useEffect(() => {
    myCourses().then(myCoursess => setMyCourses(myCoursess));
  }, []);

  console.log("myCoursess", myCoursess);

  return (
    <div className={styles.wrapper}>
      <div className={styles.titleAll}>
        <h2>Мои курсы</h2>
      </div>
      <div className={styles.coursesWrapper}>
          {myCoursess &&
            myCoursess.map(course => {
              return (
                <div key={course.id} className={styles.coursesType}>
                  {/* <div className={styles.coursesTypesTitle}>Дизайн</div> */}
                  <Link to={`/my_course/${course.id}`} className={styles.course}>
                    <div className={styles.wrapper}>
                      <div
                        style={{
                          width: "326px",
                          height: "179px",
                          // margin: "auto",
                          borderRadius: "7px",
                          background: `url(${course.course.small_image})`
                        }}
                      ></div>
                      <div className={styles.bottom}>
                        <div className={styles.title}>
                          <p>{course.course.title}</p>
                        </div>
                        {/* <div className={styles.bottomText}>
                          <div className={styles.duration}>
                            <p>От {course.from_min_price} грн</p>
                          </div>
                          <div className={styles.from_min_price}>
                            <p>{course.duration}</p>
                          </div>
                        </div> */}
                      </div>
                    </div>
                  </Link>
                </div>
              );
            })}
        </div>
      {/* <div className={styles.coursesWrapper}>
        {myCoursess &&
          myCoursess.map(myCourse => {
            return (
                <div key={myCourse.id} className={styles.courseWrapper}>
                  <div className={styles.title}><p>{myCourse.course.title}</p></div>
                  <Link
                    to={`/my_course/${myCourse.id}`}
                    className={styles.button}
                  >
                    <p>Перейти к курсу</p>
                  </Link>
                </div>
            );
          })}
      </div> */}
    </div>
  );
};

export default MyCourses;
