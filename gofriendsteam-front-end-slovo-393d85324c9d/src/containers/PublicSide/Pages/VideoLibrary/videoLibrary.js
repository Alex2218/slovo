import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { library, buyVideoFetch } from "../../../../actions/userActions";
import styles from "./library.module.css";
import { notification } from "antd";

// const host = "http://387d0007.ngrok.io";

const VideoLibrary = props => {
  const history = useHistory();
  const [myLibrary, setMyLibrary] = useState(null);
  useEffect(() => {
    library().then(myLibrary => setMyLibrary(myLibrary));
  }, []);

  console.log("myLibrary", myLibrary);

  const buyVideo = props => {
    console.log("props", props);
    const token = localStorage.getItem("token");
    console.log("token", token);
    if (token) {
      buyVideoFetch({ video_id: props })
        .then(el => {
          notification.success({ message: el.msg });
        })
        .catch(err => {
          notification.error({ message: err.msg });
          // history.push("/login");
        });
    } else {
      console.log("aasdasdas");
      history.push("/login");
    }
  };

  return (
    <div className={styles.wrapper}>
      <div className={styles.titleWrapper}>Библиотека видео</div>
      <div className={styles.libraryWrapper}>
        {myLibrary &&
          myLibrary.map(library => {
            return (
              <div key={library.id} className={styles.oneLibraryWrapper}>
                <div
                  style={{
                    width: "329px",
                    height: "183px",
                    background: `url(${library.preview})`,
                    borderRadius: "7px 7px 0px 0px",
                    backgroundSize: "cover"
                  }}
                >
                  {library.sale === true ? (
                    <div className={styles.oneLibraryWrapperSale}>Sale</div>
                  ) : (
                    ""
                  )}
                </div>
                <div className={styles.bottom}>
                  <div className={styles.topTitle}>{library.title}</div>
                  <div className={styles.priceAndBuy}>
                    <div className={styles.price}>
                      {library.sale === false ? (
                        <div className={styles.priceFull}>
                          {library.price} $
                        </div>
                      ) : (
                        <div className={styles.priceWithSale}>
                          <div className={styles.priceWithSaleOne}>
                            {library.price} $
                          </div>
                          <div className={styles.priceWithSaleTwo}>
                            {library.new_price} $
                          </div>
                        </div>
                      )}
                    </div>
                    <div
                      onClick={() => buyVideo(library.id)}
                      className={styles.buy}
                    >
                      buy
                    </div>
                  </div>

                  <div>
                    <div className={styles.container}>
                      <input
                        className={styles.input}
                        type="checkbox"
                        id={library.id}
                      />
                      <div className={styles.readMoreWrap}>
                        <div className={styles.readMoreTarget}>
                          <div
                            className={styles.moreWrap}
                            // dangerouslySetInnerHTML={{
                            //   __html: library.speaker.description
                            // }}
                          >
                            <div className={styles.moreWrapSpeaker}>
                              <img
                                className={styles.moreWrapImg}
                                src={library.speaker.photo}
                                alt="ava"
                              />
                              <div
                                style={{
                                  width: "40px",
                                  height: "40px",
                                  background: `url(${
                                    library.speaker.photo})`,
                                  borderRadius: "100%"
                                }}
                              ></div>

                              <div className={styles.name}>
                                {library.speaker.name}
                              </div>
                            </div>
                            <div
                              className={styles.moreWrapDescription}
                              dangerouslySetInnerHTML={{
                                __html: library.speaker.description
                              }}
                            >
                              {/* {library.speaker.description} */}
                            </div>
                          </div>
                        </div>
                      </div>
                      <label className={styles.label} for={library.id}></label>
                    </div>
                  </div>

                  {/* <div className={styles.showMore}>
                    <input
                      type="checkbox"
                      className={styles.readMoreState}
                      id={library.id}
                    />

                    <div className={styles.readMoreWrap}>
                      <div className={styles.readMoreTarget}>
                        <div
                          className={styles.moreWrap}
                    
                        >
                          <div className={styles.moreWrapSpeaker}>
                           

                            <div>{library.speaker.name}</div>
                          </div>
                          <div className={styles.moreWrapDescription}>
                            {library.speaker.description}
                          </div>
                        </div>
                      </div>
                    </div>

                    <label
                      for={library.id}
                      className={styles.readMoreTrigger}
                    ></label>
                  </div> */}
                </div>
              </div>
            );
          })}
      </div>
    </div>
  );
};

export default VideoLibrary;
