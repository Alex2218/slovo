import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { myVideosFetch } from "../../../../../actions/userActions";
import styles from "./myVideos.module.css";
// const host = "http://387d0007.ngrok.io";

const MyVideos = props => {
  const [videos, setVideos] = useState(null);
  useEffect(() => {
    myVideosFetch().then(videos => setVideos(videos));
  }, []);

  console.log("videos", videos);

  return (
    <div className={styles.wrapper}>
      <div className={styles.wrapperMiddle}>
        <div className={styles.titleWrapper}>Мои видео</div>
        <div className={styles.wrapperVideos}>
          {videos &&
            videos.map(video => {
              return (
                <div key={video.id} className={styles.wrapperVideo}>
                  <div
                    style={{
                      width: "329px",
                      height: "183px",
                      background: `url(${video.preview})`,
                      borderRadius: "7px 7px 0px 0px",
                      backgroundSize: "cover"
                    }}
                  ></div>
                  <div className={styles.bottom}>
                    <div className={styles.imgWrapper}>
                      <div
                        style={{
                          width: "56px",
                          height: "56px",
                          background: `url(${video.speaker.photo})`,
                          borderRadius: "100%"
                        }}
                      ></div>
                    </div>
                    <div className={styles.bottomRight}>
                      <Link
                        to={`/private_video/${video.id}`}
                        className={styles.topTitle}
                      >
                        {video.title}
                      </Link>
                      <div className={styles.name}>{video.speaker.name}</div>
                    </div>
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
};

export default MyVideos;
