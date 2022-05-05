import React, { Component } from "react";
import styles from "./FormFields.module.css";
import axios from "axios";
import FileImg from "../../../../../../../../../img/file.png";

class FormFields extends Component {
  constructor(props) {
    super(props);
    this.state = { ...props };
  }

  render() {
    return (
      <div className={`form-field ${styles.formField}`}>
        <div className={`js-field-group field-form ${styles.formField}`}>
          <textarea
            className={styles.formTextarea}
            name={`text_answer_${this.state.index}`}
          />
          <br />
          <div className={styles.formFieldInput}>
            <img className={styles.FileImg} src={FileImg} />
            <input
              className={styles.formInput}
              placeholder="Введите сообщение"
              // id="file"
              id={`file_${this.state.index}`}
              name={`file_answer_${this.state.index}`}
              type="file"
            />
            <label className={styles.formLabel} for={`file_${this.state.index}`}>
              Добавить файлы
            </label>
          </div>
        </div>
        <hr />
      </div>
    );
  }
}

export default FormFields;
