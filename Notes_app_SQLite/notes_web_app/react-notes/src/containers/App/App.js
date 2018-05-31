import React, { Component } from 'react';
import './App.css';
import Navbar from '../../components/Navbar/Navbar';
import Notes from '../../components/Notes/Notes';
import Login from '../../components/Login/Login';
import Aux from '../../hoc/Aux';

class App extends Component {
  state = {
    authToken: null
  }
  tokenHandle= Token => {
    console.log(`TOken Received ${Token}`);
    this.setState({authToken: Token});
  }
  logoutHandle = () => {
    this.setState({authToken: null});
  }

  render() {
    return (
      <Aux>
        <Navbar logoutHandler={this.logoutHandle}
        token={this.state.authToken}/>
        {!this.state.authToken? <Login
        tokenHandler={this.tokenHandle}/>:null}
        { this.state.authToken ? <Notes />: null}
      </Aux>
    );
  }
}

export default App;
