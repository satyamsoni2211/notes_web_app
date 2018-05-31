import React, { Component } from 'react';
import './Login.css';
import axios from 'axios';
import qs from 'qs';

class Login extends Component {
    state = {
        username: '',
        password: '',
        authToken: null,
        error: false,
        errorMessage: null
    }
    componentDidUpdate(){
        if (this.state.authToken){
            console.log('Login successfuly');
           this.props.tokenHandler(this.state.authToken); 
        }
    }
    handleForm(e){
        e.preventDefault();
        console.log(this.state);
        console.log('Getting AuthToken');
        axios.post('http://127.0.0.1:8000/accounts/api-token-auth/', qs.stringify({
            'username': this.state.username,
            'password': this.state.password
        })).then((response) => {
                // console.log(response)
                console.log(response);
                window.sessionStorage.setItem('token',response.data.token);
                this.setState({ authToken: response.data.token });
                // console.log(response);

            }).catch(error => { console.log(error);
            this.setState({error: true, errorMessage: error});
         });
    }

    render(){
        return(
            <div className='Login'>
            <form>
            <br/>
            <label htmlFor="username" >Username &nbsp;</label>
            <input type="text" name='username' value={this.state.username} 
            onChange={(e)=>{this.setState({username: e.target.value})}}/>
            <br/>
            <label htmlFor="password">Password &nbsp;</label>
            <input type="password" name='password' value={this.state.password}
            onChange={(e)=>{this.setState({password: e.target.value})}} />
            <br/>
            <button className='btn btn-primary' onClick={(e) => this.handleForm(e)}>Login</button>
            {this.state.error ? <span className='help-block'>Wrong Username/Password</span> : null }
            </form>
            </div>
        );
    }
} 

export default Login;