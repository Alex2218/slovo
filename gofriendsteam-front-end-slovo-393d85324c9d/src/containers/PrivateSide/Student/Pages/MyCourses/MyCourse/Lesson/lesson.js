import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";
// import { myCourse } from "../../../../../../actions/userActions";
import styles from "./lesson.module.css";
import { myLesson } from "../../../../../../../actions/userActions";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import { TabPanel, a11yProps } from "../../../../components/Tabs/tabs";
import Videos from "./Videos/Videos";
import HomeWork from "./HomeWork/HomeWork";
import HWicon from "../../../../../../../img/HWicon.png";
import VideoIcon from "../../../../../../../img/VideoIcon.png";

const Lesson = props => {
  const [myLessonn, setMyLesson] = useState(null);
  useEffect(() => {
    const query = `package_id-${props.match.params.id}/module_id-${props.match.params.moduleId}/lesson_id-${props.match.params.lessonId} `;
    myLesson(query).then(myLessonn => setMyLesson(myLessonn));
  }, []);

  console.log("myLesson", myLessonn);

  const [value, setValue] = React.useState(0);
  const handleChangeT = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>{myLessonn && myLessonn.title}</div>

      <Tabs
        centered
        value={value}
        onChange={handleChangeT}
        // indicatorColor="primary"
        // textColor="primary"
      >
        <Tab
          label="ВИДЕО"
          icon={<img className={styles.HWicon} src={HWicon} />}
          {...a11yProps(0)}
        />
        <Tab
          label="ДЗ"
          icon={<img className={styles.VideoIcon} src={VideoIcon} />}
          {...a11yProps(1)}
        />
      </Tabs>
      <TabPanel value={value} index={0}>
        <Videos myLessonn={myLessonn} />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <HomeWork match={props.match} myLessonn={myLessonn} />
      </TabPanel>
    </div>
  );
};

export default Lesson;
