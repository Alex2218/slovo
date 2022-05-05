import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";
// import { myCourse } from "../../../../../../actions/userActions";
import styles from "./Videos.module.css";
import { myLesson } from "../../../../../../../../actions/userActions";
import "video-react/dist/video-react.css";
import { Player } from "video-react";
import FileImg from "../../../../../../../../img/file.png";

const Videos = props => {
  console.log("myLessonnVVV", props);
  const VideosInform = props.myLessonn;
  // const host = "http://387d0007.ngrok.io";
  console.log("VideosInform", VideosInform);

  return (
    <div className={styles.wrapper}>
      {VideosInform && (
        <div className={styles.videosWrapper}>
          <div
            className={styles.description}
            dangerouslySetInnerHTML={{
              __html: VideosInform.description
            }}
          ></div>
          <div className={styles.videos}>
            {VideosInform &&
              VideosInform.videos.map(video => {
                return (
                  <div key={video.id} className={styles.videoWrapper}>
                    <div className={styles.titleVideo}>
                      <h2>{video.title}</h2>
                    </div>
                    <Player className={styles.video}>
                      <source src={video.video_1080} />
                    </Player>
                  </div>
                );
              })}
          </div>
          <div className={styles.files}>
            <p className={styles.filesTitle}>Материалы</p>
            {VideosInform &&
              VideosInform.files.map(file => {
                return (
                  <div key={file.id} className={styles.file}>
                    <img className={styles.FileImg} src={FileImg} />
                    <a href={file.file} download>
                    {file.file.slice(file.file.lastIndexOf('/') + 1).slice(0, 10) + '...'}
                    </a>
                  </div>
                );
              })}
          </div>
        </div>
      )}
    </div>
  );
};

export default Videos;
