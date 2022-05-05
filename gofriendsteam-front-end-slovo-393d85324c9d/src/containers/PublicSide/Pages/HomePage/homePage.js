import React, { Component } from "react";
import HomePageAccordion from "./HomePageAccordion/HomePageAccordion";
import styles from "./HomePage.module.css";
import done from "../../../../img/done.png";
import comp from "../../../../img/comp.png";
import Slovo from "../../../../img/Slovo.png";

const HomePage = ({ children }) => {
  return (
    <div className={styles.wrapper}>
      <div className={styles.block1}>
        <div className={styles.block1Left}>
          <div className={styles.topText}>
            <img className={styles.comp} src={comp} />
            <div className={styles.text1}>Онлайн курсы</div>
          </div>
          <div className={styles.title}>
            <div className={styles.titleText}>Образовательная платформа</div>
            <img className={styles.Slovo} src={Slovo} />
          </div>
          <div className={styles.description}>Освой маркетинг, SMM-менеджмент и получи высокооплачиваюмую работу</div>
          <div className={styles.dones}>
            <div className={styles.done}>
              <img className={styles.doneImg} src={done} />
              <div className={styles.doneText}>Научимся делать маркетинговый план</div>
            </div>
            <div className={styles.done}>
              <img className={styles.doneImg} src={done} />
              <div className={styles.doneText}>Сформируем привлекательное портфолио</div>
            </div>
            <div className={styles.done}>
              <img className={styles.doneImg} src={done} />
              <div className={styles.doneText}>Найдем первых реальных клиентов</div>
            </div>
          </div>
          <button className={styles.buttonn}><p>Оставить заявку</p></button>
        </div>
        <HomePageAccordion />
      </div>
    </div>
  );
};

export default HomePage;
