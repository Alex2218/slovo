import * as React from "react";
import { render } from "react-dom";
import styles from "./HomePageAccordion.module.css";
import girlFirstPage from "../../../../../img/girlFirstPage.png";
import think from "../../../../../img/think.png";
import speaker1 from "../../../../../img/speaker1.png";
import speaker2 from "../../../../../img/speaker2.png";
import speaker3 from "../../../../../img/speaker3.png";
import speaker4 from "../../../../../img/speaker4.png";

const HomePageAccordion = () => {
  return (
    <article className={styles.accordion}>
      <section id="acc1">
        <div className={styles.name}>
          <p className={styles.nameSpeaker}>Юлия Моисеева</p>
          <p className={styles.nameText}>спикер</p>
        </div>
        <h2>
          <a href="#acc1">Digital маркетинг</a>
        </h2>
      </section>
      <section id="acc2">
        <div className={styles.name}>
          <p className={styles.nameSpeaker}>Владимир Курченко</p>
          <p className={styles.nameText}>спикер</p>
        </div>
        <h2>
          <a href="#acc2">IT специальности</a>
        </h2>
      </section>
      <section id="acc3">
        <div className={styles.name}>
          <p className={styles.nameSpeaker}>Дмитрий Шевчук</p>
          <p className={styles.nameText}>спикер</p>
        </div>
        <h2>
          <a href="#acc3">Товарный бизнес</a>
        </h2>
      </section>
      <section id="acc4">
        <div className={styles.name}>
          <p className={styles.nameSpeaker}>Евгений Моисеев</p>
          <p className={styles.nameText}>спикер</p>
        </div>
        <h2>
          <a href="#acc4">Продажи</a>
        </h2>
      </section>
      <div className={styles.default}>
        <img className={styles.speakerThinks} src={think} />
        <img className={styles.speakerImg} src={girlFirstPage} />
      </div>
    </article>
  );
};

export default HomePageAccordion;
