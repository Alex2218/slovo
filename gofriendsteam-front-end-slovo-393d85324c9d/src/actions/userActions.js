import api from "./request";
import {
  LOGIN,
  PROFILE,
  REGISTRATION,
  SOCIALLOGIN,
  RESET_PASSWORD,
  GET_FORM_QUESTIONNAIRE,
  POST_FORM_QUESTIONNAIRE,
  ALL_COURSES,
  COURSE,
  PACKAGES_INFO,
  PACKAGE_INFO,
  BUY_PACKAGE,
  FILTER,
  MY_COURSES,
  MY_LESSON,
  LIBRARY,
  BUY_VIDEO,
  MY_VIDEOS
} from "../constants/apiUrl";

export const login = user => dispatch => {
  return api("post", LOGIN, user).then(res => {
    localStorage.setItem("token", res.token);
    return res;

    // getProfile().then(res => {
    //     if(res.role === 'mentor') {
    //       window.history.pushState('', '', '/mentor')
    //     } else {
    //       window.history.pushState('', '', '/student')
    //     }
    //     dispatch({
    //       type: 'UPDATE_PROFILE',
    //       payload: res
    //     });

    //   // });
  });
};

export const socialLogin = user => dispatch => {
  return api("post", SOCIALLOGIN, user).then(res => {
    localStorage.setItem("token", res.token);
    return res;
  });
};

export const getProfile = () => {
  return api("get", PROFILE);
};

export const registration = (user, history) => dispatch => {
  const h = history;
  return api("post", REGISTRATION, user)
    .then(res => {
      h.push("/login");
    })
    .catch(e => console.log(e.response));
};

export const resetPassword = email => {
  return api("put", RESET_PASSWORD, email);
};

export const getFormQuestionnaire = () => {
  return api("get", GET_FORM_QUESTIONNAIRE);
};

export const postFormQuestionnaire = data => {
  return api("post", POST_FORM_QUESTIONNAIRE, data);
};

//courses

export const getAllCourses = () => {
  return api("get", ALL_COURSES);
};

export const getCourse = id => {
  return api("get", COURSE + id);
};

export const getAllPackages = () => {
  return api("get", PACKAGES_INFO);
};

export const getPackage = id => {
  return api("get", PACKAGE_INFO + id);
};

export const getFilter = () => {
  return api("get", FILTER);
};

//order
export const buyPackage = data => {
  return api("post", BUY_PACKAGE, data);
};

//student
export const myCourses = () => {
  return api("get", MY_COURSES);
};

export const myCourse = id => {
  return api("get", MY_COURSES + id);
};

export const myLesson = id => {
  return api("get", MY_LESSON + id);
};

//library
export const library = () => {
  return api("get", LIBRARY);
};

export const buyVideoFetch = data => {
  return api("post", BUY_VIDEO, data);
};

export const myVideosFetch = () => {
  return api("get", MY_VIDEOS);
};

export const myVideoFetch = id => {
  return api("get", LIBRARY + id);
};
