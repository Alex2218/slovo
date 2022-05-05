const SERVERS = {
  PRODUCT: {
    XHR: "https://api.slovo.expert/api/v1/"
  },
  DEV: {
    XHR:
      // 'http://192.168.88.239:8001/api/v1/'
      "http://778fb501.ngrok.io/api/v1/"
  }
};

export const BASE_URL = /\bdev\b|\blocalhost\b/.test(document.location.hostname)
  ? // ? SERVERS.DEV.XHR /* <=== set here server what needs for developing -  */
    SERVERS.DEV.XHR /* <=== set here server what needs for developing -  */
  : SERVERS.PRODUCT.XHR;


//USER
export const LOGIN = "user/login/";

export const PROFILE = "user/profile/";
export const REGISTRATION = "user/register/";
export const SOCIALLOGIN = "user/social-login/";
export const RESET_PASSWORD = "user/password_reset/";
export const GET_FORM_QUESTIONNAIRE = "user/get_form/";
export const POST_FORM_QUESTIONNAIRE = "user/get_form/";

//course
export const ALL_COURSES = "course/all_courses/";
export const COURSE = "course/all_courses/";
export const PACKAGES_INFO = "course/package_info/";
export const PACKAGE_INFO = "course/package_info/";
export const FILTER = "course/params/";

//order
export const BUY_PACKAGE = "orders/create/";

//student

export const MY_COURSES = "student/my_courses/";
export const MY_LESSON = "student/get_video/";

//library


export const LIBRARY = "library/videos/";
export const BUY_VIDEO = "library/videos/create_order/";
export const MY_VIDEOS = "library/videos/my_videos/";