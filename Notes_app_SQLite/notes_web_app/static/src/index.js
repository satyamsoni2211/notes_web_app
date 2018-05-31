import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './containers/App/App';
import {HashRouter} from 'react-router-dom';
// import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<HashRouter><App /></HashRouter>,  document.getElementById('root'));
// registerServiceWorker();
