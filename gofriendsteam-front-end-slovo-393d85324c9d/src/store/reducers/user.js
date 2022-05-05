export default (state = {
    role: ''
    // role: 'mentor'
}, action) => {
    console.log(action);
    switch (action.type) {
        case 'UPDATE_PROFILE':
            return {...action.payload.user};
        case 'LOGOUT':
            localStorage.removeItem('token');
            return {};
        case 'SOCIALLOGIN':
        return {...action.payload.user};
            default: 
            return state;
            
    }
};
