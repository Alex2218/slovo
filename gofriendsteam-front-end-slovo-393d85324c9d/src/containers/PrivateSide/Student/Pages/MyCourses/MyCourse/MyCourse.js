import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import ProgressBar from "react-bootstrap/ProgressBar";
import { myCourse } from "../../../../../../actions/userActions";
import styles from "./myCourse.module.css";
// import { Progress } from 'semantic-ui-react'
import Accordion from "../../../components/Accordion/Accordion";
import badStatus from "../../../../../../img/badStatus.png";
import waitStatus from "../../../../../../img/waitStatus.png";
import goodStatus from "../../../../../../img/goodStatus.png";

const MyCourse = props => {
  const [myCours, setMyCourse] = useState(null);

  useEffect(() => {
    myCourse(props.match.params.id).then(myCours => setMyCourse(myCours));
  }, []);

  console.log("myCourse", myCours);

  let num = myCours && (myCours.waiting_task / myCours.total_count) * 100;

  console.log("num", num);
  return (
    <div className={styles.courseWrapper}>
      <div className={styles.title}>
        <h1>{myCours && myCours.course.title}</h1>
      </div>
      {myCours && (
        <div className={styles.progressBarWrapper}>
          <div className={styles.progressBar}>
            <div
              style={{
                width: `${myCours.progress_done}%`,
                height: "78px",
                background: "#FFEE55",
                borderRadius: "7px 0px 0px 7px",
                display: "flex",
                alignItems: "center",
                padding: "0px 0px"
              }}
            >
              <div className={styles.progressBarTitle}>
                <p>Прогресс прохождения курса</p>
              </div>
            </div>

            <div className={styles.progressBarPercentAny}>
              <p>{myCours.progress_done}%</p>
            </div>
          </div>
          <div className={styles.progressBar}>
            <div
              style={{
                width: `${myCours.activity_progress}%`,
                height: "78px",
                background: "#FFEE55",
                borderRadius: "7px 0px 0px 7px",
                display: "flex",
                alignItems: "center",
                padding: "0px 0px"
              }}
            >
              <div className={styles.progressBarTitle}>
                <p>Общая успеваемость по курсу:</p>
              </div>
            </div>

            <div className={styles.progressBarPercentAny}>
              <p>{myCours.activity_progress}%</p>
            </div>
          </div>
          <div className={styles.progressBar}>
            <div
              style={{
                width: `${num}%`,
                height: "78px",
                background: "#FFEE55",
                borderRadius: "7px 0px 0px 7px",
                display: "flex",
                alignItems: "center",
                padding: "0px 0px"
              }}
            >
              <div className={styles.progressBarTitle}>
                <p>Пройдено уроков:</p>
              </div>
            </div>

            <div className={styles.progressBarPercent}>
              <p className={styles.progressBarPercentItemBig}>
                {myCours.waiting_task}
              </p>
              <p className={styles.progressBarPercentItem}>
                из {myCours.total_count}
              </p>
            </div>
          </div>
        </div>
      )}
      <div className={styles.topText}>
        <div className={styles.topTextItem}>Программа курса</div>
        <div className={styles.topTextItem}>Пройдено уроков</div>
      </div>
      <div className={styles.accordion}>
        {/* <Accordion> */}
        {myCours &&
          myCours.modules.map(moduleItem => {
            return (
              <div key={moduleItem.id} className={styles.moduleItem}>
                <Accordion>
                  <div className={styles.moduleTitleAndNumber}>
                    <div className={styles.moduleTitle}>
                      {moduleItem.module.title}
                    </div>
                    <div className={styles.moduleNumber}>
                      {/* {moduleItem.module.title} */}
                    </div>
                  </div>
                  <div>
                    {moduleItem.lessons && moduleItem.lessons.map(lesson => {
                      return (
                        <Link
                          to={`/lesson/${props.match.params.id}/${moduleItem.module.id}/${lesson.id}`}
                          className={styles.lessonItem}
                          key={lesson.id}
                        >
                          <div className={styles.lessonTitle}>
                            {lesson.title}
                          </div>
                          <div className={styles.lessonStatus}>
                            {lesson.status_task === "not_done" ? (
                              <img className={styles.status} src={badStatus} />
                            ) : lesson.status_task === "wait" ? (
                              <img className={styles.status} src={waitStatus} />
                            ) : (
                              <img className={styles.status} src={goodStatus} />
                            )}
                            {/* {lesson.status_task} */}
                          </div>
                        </Link>
                      );
                    })}
                  </div>
                </Accordion>
              </div>
            );
          })}
      </div>
      {/* <div className={styles.bottomWrapper}>
        <Link to={`/`} className={styles.button}>
          <p>Пройти финальный тест</p>
        </Link>
        <div className={styles.redStar}>
          <p>*Если прогресс прохождения курса больше 70%</p>
        </div>
      </div> */}
    </div>
  );
};

export default MyCourse;
