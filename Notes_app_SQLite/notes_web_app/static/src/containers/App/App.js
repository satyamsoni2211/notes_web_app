import React, { Component } from 'react';
import './App.css';
import Navbar from '../../components/Navbar/Navbar';
import Notes from '../../components/Notes/Notes';
import Login from '../../components/Login/Login';
import Aux from '../../hoc/Aux';
import {Link, Route} from 'react-router-dom';
import CreateNote from '../../components/CreateNote/CreateNote';

class App extends Component {
  state = {
    authToken: null,
    sessionSet : false
  }
  tokenHandle= Token => {
    console.log(`TOken Received ${Token}`);
    console.log(`My toekn is ${window.sessionStorage.getItem('token')}`);
    this.setState({authToken: Token});
  }
  logoutHandle = () => {
    window.sessionStorage.removeItem('token');
    this.setState({sessionSet: false});
  }
  componentDidMount() {
    if(this.state.authToken === null && window.sessionStorage.getItem('token')){
      this.setState({authToken: window.sessionStorage.getItem('token')});
    }
  }

  render() {
    return (
      <Aux>
        <Navbar logoutHandler={this.logoutHandle}/>
        { !window.sessionStorage.getItem('token') ? <Login
        tokenHandler={this.tokenHandle}/>:null}
        { this.state.sessionSet || window.sessionStorage.getItem('token')  ? 
        <Aux>
        <Route path='/' exact component={Notes}/>
        <Route path='/view_notes' exact component={Notes}/>
        <Route path='/create_notes' exact component={() => <CreateNote token={this.state.authToken} logout={this.logoutHandle}/>} />
        </Aux>: null}
      </Aux>
    );
  }
}

export default App;
