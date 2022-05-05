import React from "react";
import { FadeLoader } from "react-spinners";
import styles from "./loader.module.css";

const Loader = () => {
  return (
    <div className={styles.wrapLoader}>
      <FadeLoader
        size={350}
        color={"#123abc"}
        loading={true}
      />
    </div>
  );
};

export default Loader;