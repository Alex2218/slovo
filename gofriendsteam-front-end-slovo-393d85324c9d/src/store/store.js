import { createStore, applyMiddleware } from 'redux';
import reducer from './reducers/root';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';

const persistConfig = {
  key: 'root',
  storage,
};

const persistedReducer = persistReducer(persistConfig, reducer);


export default function configureStore (initState = {}) {
 
  const enhancer = 
    composeWithDevTools(applyMiddleware(thunk));


  let store = createStore(persistedReducer, enhancer);
  let persistor = persistStore(store);
  return { store, persistor }
}
