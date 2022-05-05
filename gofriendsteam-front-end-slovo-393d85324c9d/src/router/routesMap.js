// import React, { lazy } from "react";
// import HomePage from "../containers/PublicSide/Pages/HomePage/homePage";
// import Login from "../containers/PublicSide/Pages/Login/login";
// import Registration from "../containers/PublicSide/Pages/Registration/Registration";
// import mentorPage from "../containers/PrivateSide/Mentor/Pages/mentorPage";
// import studentPage from "../containers/PrivateSide/Student/Pages/studentPage";
// import Questionnaire from "../containers/PrivateSide/Student/Pages/questionnaire/questionnaire";
// import Profile from "../containers/PrivateSide/Student/Pages/Profile";
// import ResetPassword from "../containers/PublicSide/Pages/ResetPassword/ResetPassword";
// import Courses from "../containers/PublicSide/Pages/Courses/courses";
// import Course from "../containers/PublicSide/Pages/Courses/Course/course";
// import Package from "../containers/PublicSide/Pages/Courses/Course/Package/package";
// import VideoLibrary from "../containers/PublicSide/Pages/VideoLibrary/videoLibrary";
// import MyCourses from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourses";
// import MyCourse from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourse/MyCourse";
// import Lesson from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourse/Lesson/lesson";
// import MyVideos from "../containers/PrivateSide/Student/Pages/MyVideos/myVideos";
// import MyVideo from "../containers/PrivateSide/Student/Pages/MyVideos/MyVideo/myVideo";
import React, { lazy } from "react";
import HomePage from "../containers/PublicSide/Pages/HomePage/homePage";
import Login from "../containers/PublicSide/Pages/Login/login";
import Registration from "../containers/PublicSide/Pages/Registration/Registration";
import mentorPage from "../containers/PrivateSide/Mentor/Pages/mentorPage";
import studentPage from "../containers/PrivateSide/Student/Pages/studentPage";
import Questionnaire from "../containers/PrivateSide/Student/Pages/questionnaire/questionnaire";
import Profile from "../containers/PrivateSide/Student/Pages/Profile";
import ResetPassword from "../containers/PublicSide/Pages/ResetPassword/ResetPassword";
import Courses from "../containers/PublicSide/Pages/Courses/courses";
import Course from "../containers/PublicSide/Pages/Courses/Course/course";
import Package from "../containers/PublicSide/Pages/Courses/Course/Package/package";
import VideoLibrary from "../containers/PublicSide/Pages/VideoLibrary/videoLibrary";
import MyCourses from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourses";
import MyCourse from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourse/MyCourse";
import Lesson from "../containers/PrivateSide/Student/Pages/MyCourses/MyCourse/Lesson/lesson";
import MyVideos from "../containers/PrivateSide/Student/Pages/MyVideos/myVideos";
import MyVideo from "../containers/PrivateSide/Student/Pages/MyVideos/MyVideo/myVideo";


// export const publicRoutes = [
//   {
//     path: "/home",
//     component: lazy(() => HomePage),
//     exact: true
//   },
//   {
//     path: "/courses",
//     component: lazy(() => Courses),
//     exact: true
//   },
//   {
//     path: "/courses/:id",
//     component: lazy(() => Course),
//     exact: true
//   },
//   {
//     path: "/package/:id",
//     component: lazy(() => Package),
//     exact: true
//   },
//   {
//     path: "/video",
//     component: lazy(() => VideoLibrary),
//     exact: true
//   },
//   {
//     path: "/login",
//     component: lazy(() => Login),
//     exact: false
//   },
//   {
//     path: "/registration",
//     component: lazy(() => Registration),
//     exact: true
//   },
//   {
//     path: "/reset_password",
//     component: lazy(() => ResetPassword),
//     exact: true
//   }
// ];

// export const mentorRoutes = [
//   {
//     path: "/mentor",
//     component: lazy(() => mentorPage),
//     exact: true
//   }
// ];

// export const studentRoutes = [
//   {
//     path: "/student",
//     component: lazy(() => studentPage),
//     exact: true
//   },
//   {
//     path: "/profile",
//     component: lazy(() => Profile),
//     exact: true
//   },
//   {
//     path: "/questionnaire",
//     component: lazy(() => Questionnaire),
//     exact: true
//   },
//   {
//     path: "/private_courses",
//     component: lazy(() => Courses),
//     exact: true
//   },
//   {
//     path: "/my_courses",
//     component: lazy(() => MyCourses),
//     exact: true
//   },
//   {
//     path: "/my_video",
//     component: lazy(() => VideoLibrary),
//     exact: true
//   },
//   {
//     path: "/my_course/:id",
//     component: lazy(() => MyCourse),
//     exact: true
//   },
//   {
//     path: "/lesson/:id/:moduleId/:lessonId",
//     component: lazy(() => Lesson),
//     exact: true
//   },
//   {
//     path: "/private_video",
//     component: lazy(() => MyVideos),
//     exact: true
//   },
//   {
//     path: "/private_video/:id",
//     component: lazy(() => MyVideo),
//     exact: true
//   }
// ];



export const publicRoutes = [
  {
    path: "/home",
    component: HomePage,
    exact: true
  },
  {
    path: "/courses",
    component: Courses,
    exact: true
  },
  {
    path: "/courses/:id",
    component: Course,
    exact: true
  },
  {
    path: "/package/:id",
    component: Package,
    exact: true
  },
  {
    path: "/video",
    component: VideoLibrary,
    exact: true
  },
  {
    path: "/login",
    component: Login,
    exact: false
  },
  {
    path: "/registration",
    component: Registration,
    exact: true
  },
  {
    path: "/reset_password",
    component: ResetPassword,
    exact: true
  }
];

export const mentorRoutes = [
  {
    path: "/mentor",
    component: mentorPage,
    exact: true
  }
];

export const studentRoutes = [
  {
    path: "/student",
    component: studentPage,
    exact: true
  },
  {
    path: "/profile",
    component: Profile,
    exact: true
  },
  {
    path: "/questionnaire",
    component: Questionnaire,
    exact: true
  },
  {
    path: "/private_courses",
    component: Courses,
    exact: true
  },
  {
    path: "/my_courses",
    component: MyCourses,
    exact: true
  },
  {
    path: "/my_video",
    component: VideoLibrary,
    exact: true
  },
  {
    path: "/my_course/:id",
    component: MyCourse,
    exact: true
  },
  {
    path: "/lesson/:id/:moduleId/:lessonId",
    component: Lesson,
    exact: true
  },
  {
    path: "/private_video",
    component: MyVideos,
    exact: true
  },
  {
    path: "/private_video/:id",
    component: MyVideo,
    exact: true
  }
];
