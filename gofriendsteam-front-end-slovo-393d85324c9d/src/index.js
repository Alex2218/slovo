import React from 'react';
import { render } from 'react-dom';
import './index.css';
import App from './App';

import { Provider } from 'react-redux';
import configureStore from './store/store';
import { PersistGate } from 'redux-persist/integration/react';
import '../src/fonts/ProximaNova/fonts/fonts.css'
// import '../src/fonts/ProximaNova/fonts/fonts.min.css'

render(
  <Provider store={configureStore().store}>
    <PersistGate loading={null} persistor={configureStore().persistor}>
        <App />
        </PersistGate>
  </Provider>,
  document.getElementById('root')
);
