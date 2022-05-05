import React, { useState, useEffect } from "react";
import {
  getFormQuestionnaire,
  postFormQuestionnaire
} from "../../../../../actions/userActions";
import styles from "./questionnaire.module.css";
import { Link, useHistory } from "react-router-dom";

const Questionnaire = props => {
  const history = useHistory();
  const [listQuestions, setItems] = useState([]);
  const [answers, setAnswers] = useState([]);
  const fetchGetListQuestions = () => {
    getFormQuestionnaire().then(res => {
      setItems(res);
    });
  };

  useEffect(() => {
    fetchGetListQuestions();
  }, []);

  const handleChangeCheckbox = ({ target }, questionId) => {
    const value = target.value;
    const isChecked = target.checked;
    const isInState = answers.find(el => el.question_id === questionId);
    console.log('isInState', isInState, questionId, answers, value)
    if (isInState) {
      if (isChecked) {
        console.log('isInState1', isInState)
        const newAnswers = [...isInState.answer_id, value];
        isInState.answer_id = newAnswers;
      } else {
        const newAnswers =
          isInState.answer_id && isInState.answer_id.filter(el => el !== value);
        isInState.answer_id = newAnswers;
        console.log('newAnswers', newAnswers)

      }
      const arr = answers.map(el =>
        el.id === questionId ? { ...isInState } : el
      );
      setAnswers(arr);
    } else {
      setAnswers([...answers, { question_id: questionId, answer_id: [value] }]);
    }
  };

  const sendAnswers = () => {
    postFormQuestionnaire({ questions: answers }).then(res => {
      console.log("res", res);
      history.push("/my_courses");
    });
  };
  console.log(answers);
  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <div className={styles.title}>Анкета</div>
        {listQuestions.map(item => (
          <div key={item.id} className={styles.wrapperOne}>
            <h2 className={styles.question}>{item.question}</h2>
            <div className={styles.answers}>
              {item.answers &&
                item.answers.map(i => (
                  <div key={i.id} className={styles.answer}>
                    <div className={styles.answerL}>{i.answer}</div>
                    <input
                      type="checkbox"
                      id={i.id}
                      value={i.id}
                      onChange={e => handleChangeCheckbox(e, item.id)}
                    />{" "}
                    <label className={styles.answerLB} for={i.id}></label>
                  </div>
                ))}
            </div>
          </div>
        ))}
        <div className={styles.buttonsWrapper}>
        <button
          type="submit"
          onClick={sendAnswers}
          className={styles.submitDiv}
        >
          <p className={styles.submit}>Отправить</p>
        </button>
        <Link to={`/my_courses`} className={styles.buttonLink}>
          <p>Пропустить</p>
        </Link>
        </div>
      </div>
    </div>
  );
};
export default Questionnaire;
