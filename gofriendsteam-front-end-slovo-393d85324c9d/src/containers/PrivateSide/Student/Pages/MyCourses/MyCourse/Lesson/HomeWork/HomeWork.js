import React, { Component } from "react";
import styles from "./homeWork.module.css";
import axios from "axios";
import FormFields from "./FormFields/FormFields";
import FileImg from "../../../../../../../../img/file.png";
import { notification } from "antd";

// const host = "http://387d0007.ngrok.io";
const token = localStorage.getItem("token");

export default class HomeWork extends Component {
  state = {
    componentField: ["input-0"]
    // package: 0, // hard code package id
    // module: 0, // hard code module id
    // lesson: 0 // hard code lesson id
  };

  // let fields = document.querySelectorAll('.js-field-group');
  //       for (let i = 0; i < fields.length; i++) {
  //           let current_field = fields[i];
  //           let text_value = current_field.querySelector(`textarea[name="text_answer_${i}"`).value;
  //           let file_value = current_field.querySelector(`input[name="file_answer_${i}"`);
  //           console.log('i ', i, file_value.files)
  //           formData.set(`text_answer_${i}`, text_value || '');
  //           formData.set(`file_answer_${i}`, file_value.files[0] || '');
        // }
  handleSubmit = event => {
    event.preventDefault();
    console.log("submit form!");
    let formData = new FormData();
    formData.set("package", this.props.match.params.id);
    formData.set("module", this.props.match.params.moduleId);
    formData.set("lesson", this.props.match.params.lessonId);
    let fields = document.querySelectorAll(".js-field-group");
    for (let i = 0; i < fields.length; i++) {
      let current_field = fields[i];
      let text_value = current_field.querySelector(
        `textarea[name="text_answer_${i}"`
      ).value;
      let file_value = current_field.querySelector(
        `input[name="file_answer_${i}"`
      );
      console.log("i", i, file_value.files);
      formData.set(`text_answer_${i}`, text_value || "");
      formData.set(`file_answer_${i}`, file_value.files[0] || "");
    }

    axios({
      method: "post",
      url: "http://387d0007.ngrok.io/api/v1/student/upload_home_task",
      headers: {
        "Content-Type":
          "multipart/form-data;boundary=----WebKitFormBoundaryyrV7KO0BoCBuDbTL",

        Authorization: `Bearer ${token}`
      },
      data: formData
    })
      .then(response => {
        if (response.status === 201) {
          notification.success({ message: "Домашнее задание отправлено!" });
        }
      })
      .catch(err => {
        notification.error({
          message: "Домашнее задание не удалось отправить!"
        });
      });
  };

  render() {
    const HomeWorkInform = this.props.myLessonn && this.props.myLessonn.task;

    console.log("HomeWorkInform", HomeWorkInform);

    return (
      <div className={styles.wrapper}>
        <div className={styles.hwInf}>
          <div className={styles.hwTitle}>Домашнее задание</div>
          <div
            className={styles.description}
            dangerouslySetInnerHTML={{
              __html: HomeWorkInform && HomeWorkInform.text
            }}
          ></div>
          <div className={styles.files}>
            <p className={styles.filesTitle}>Материалы</p>
            {HomeWorkInform &&
              HomeWorkInform.files.map(file => {
                return (
                  <div key={file.id} className={styles.file}>
                    <img className={styles.FileImg} src={FileImg} />
                    <a href={file.file} download>
                      {file.file
                        .slice(file.file.lastIndexOf("/") + 1)
                        .slice(0, 10) + "..."}
                    </a>
                  </div>
                );
              })}
          </div>
        </div>
        <div className={styles.form}>
          <div className={styles.sendHW}>Сдать домашнее задание</div>
          <button
            className={styles.addForm}
            onClick={e => {
              var block = `input-${this.state.componentField.length}`;
              this.setState(prevState => ({
                componentField: prevState.componentField.concat([block])
              }));
            }}
          >
            {" "}
            <p>Добавить ответ</p>
          </button>
          <form
            className={styles.formWrapper}
            enctype="multipart/form-data"
            action=""
            onSubmit={this.handleSubmit}
          >
            {this.state.componentField.map((elem, index) => {
              return (
                <div className={styles.formWrapperText}>
                  <FormFields index={index} key={elem} />
                  <div
                    onClick={event => {
                      let fields = this.state.componentField;
                      let index = this.state.componentField.indexOf(elem);
                      fields.splice(index, 1);
                      this.setState({
                        componentField: fields
                      });
                    }}
                    className={styles.deleteButton}
                  >
                    <p>Удалить ответ</p>
                  </div>
                </div>
              );
            })}
            <button className={styles.submitButton}>
              <p>Отправить!</p>
            </button>
          </form>
        </div>
      </div>
    );
  }
}

// export default HomeWork;
