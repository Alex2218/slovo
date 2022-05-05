// import React, { Component } from "react";
// import { notification } from "antd";

// import { getAllCourses } from "../../../../actions/userActions";
// import MyButton from "../../../Buttons/button";

// class Courses extends Component {
//   // state = {
//   //   id: 0,
//   //   title: '',
//   //   description: '',
//   //   speaker: {
//   //     id: 0,
//   //     name: '',
//   //     description: '',
//   //     photo: [],
//   //     is_lead: true,
//   //   },
//   //   proffesion: '',
//   //   packages: [],
//   //   duration: '',
//   //   from_min_price: 0,
//   // };

//   state = {
//     articles: []
//   };

//   componentDidMount() {
//     getAllCourses().then(
//       response =>
//         console.log("response", response) &&
//         this.setState({
//           articles: response.data.map(
//             item =>
//               console.log("articles", item) && {
//                 item
//               }
//           )
//         })
//       // this.setState({ articles: response.data.hits })
//     );
//   }

//   // fetchCourses = async () => {
//   //   try {
//   //     // const { results } = await getAllCourses();
//   //     // const course = results.map(item => ({
//   //     //   item,
//   //     // }))

//   //     await getAllCourses() // Получаем массив параметров с селективным заполнением для категории товара
//   //       .then(data => {
//   //         this.setState({
//   //           courses: data
//   //         });
//   //       });
//   //     console.log('course', courses)
//   //     // this.setState({ courses: [...results] });
//   //   } catch (e) {
//   //     notification.error({
//   //       title: 'Ошибка сервера!'
//   //     });
//   //   }
//   // };

//   // componentDidMount() {
//   //   this.fetchCourses();
//   // }

//   render() {
//     const { articles } = this.state;
//     return <div></div>;
//   }
// }

// export default Courses;

import React, { Component, Fragment, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Filter from "../../Components/Filter/filters";

import { getAllCourses } from "../../../../actions/userActions";
import styles from "./courses.module.css";
// const host = "http://387d0007.ngrok.io";

const Courses = props => {
  const [courses, setCourses] = useState(null);
  // const [selectedFilters, setSelectedFilters] = useState(null);
  // const [selectedCourses, setselectedCourses] = useState(null);

  // const onChange = (event, key) => {
  //   console.log("event", event.target.value, key);
  //   setSelectedFilters({ ...selectedFilters, [key]: event.target.value });
  // };

  useEffect(() => {
    getAllCourses().then(courses => setCourses(courses));
  }, []);

  const onSubmit = values => {
    console.log("values", values);
    // fetchFilters(values).then(values => setCourses(values));
  };
  // useEffect(() => {
  //   setselectedCourses(courses);
  // }, [courses]);

  // useEffect(() => {
  //   const filterItems =
  //     courses &&
  //     courses.filter(item => {
  //       if (item.tags.find(element => element.id == selectedFilters.tags)) {
  //         return true;
  //       }
  //     });
  //   setselectedCourses(filterItems);
  // }, [selectedFilters]);

  // console.log("selectedFilters", selectedFilters);
  console.log("courses", courses);

  return (
    <Fragment>
      <div className={styles.coursesWrapper}>
        {/* <Filter submit={onSubmit} /> */}

        <div className={styles.coursesAll}>
          {courses &&
            courses.map(course => {
              return (
                <div key={course.id} className={styles.coursesType}>
                  {/* <div className={styles.coursesTypesTitle}>Дизайн</div> */}
                  <Link to={`/courses/${course.id}`} className={styles.course}>
                    <div className={styles.wrapper}>
                      <div
                        style={{
                          width: "326px",
                          height: "179px",
                          margin: "auto",
                          borderRadius: "7px",
                          background: `url(${course.small_image})`
                        }}
                      ></div>
                      <div className={styles.bottom}>
                        <div className={styles.title}>
                          <p>{course.title}</p>
                        </div>
                        <div className={styles.bottomText}>
                          <div className={styles.duration}>
                            <p>От {course.from_min_price} грн</p>
                          </div>
                          <div className={styles.from_min_price}>
                            <p>{course.duration}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </Link>
                </div>
              );
            })}
        </div>
      </div>
    </Fragment>
  );
};

export default Courses;
