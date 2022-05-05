import React, { useEffect, useState } from "react";
import { myVideoFetch } from "../../../../../../actions/userActions";
import styles from "./myVideo.module.css";
import { Player } from "video-react";
// const host = "http://387d0007.ngrok.io";

const MyVideo = props => {
  const [myVideo, setMyVideo] = useState(null);
  useEffect(() => {
    myVideoFetch(props.match.params.id).then(myVideo => setMyVideo(myVideo));
  }, []);

  console.log("myVideo", myVideo);

  return (
    myVideo && (
      <div className={styles.wrapper}>
        <div className={styles.title}>{myVideo.title}</div>
        <div className={styles.wrapperMiddle}>
          <div className={styles.videoWrapper}>
            {/* <div className={styles.titleVideo}>
            <h2>{myVideo.title}</h2>
          </div> */}
            <Player className={styles.video}>
              <source src={myVideo.video} />
            </Player>
          </div>
          <div className={styles.bottom}>
            <div className={styles.imgWrapper}>
              <div
                style={{
                  width: "56px",
                  height: "56px",
                  background: `url(${myVideo.speaker.photo})`,
                  borderRadius: "100%"
                }}
              ></div>
            </div>
            <div className={styles.bottomRight}>
              <div className={styles.topTitle}>{myVideo.title}</div>
              <div className={styles.name}>{myVideo.speaker.name}</div>
            </div>
          </div>
        </div>
      </div>
    )
  );
};

export default MyVideo;
