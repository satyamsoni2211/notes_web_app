import React, { Component } from 'react';
import axios from 'axios';
import qs from 'qs';
import Note from '../Note/Note';

class Notes extends Component {
    state = {
        notes: [],
        authToken: null
    }
    componentDidUpdate() {

        console.log(`logging get request using authtoken ${this.state.authToken}`);

        if (this.state.authToken && this.state.notes.length <= 0) {
                axios({ method: 'get', 
                url: 'http://127.0.0.1:8000/api/list/', 
                headers: { Authorization:`Token ${this.state.authToken}`}
            })
                .then(response => {
                    console.log(response.data);
                    this.setState({notes: [...response.data]});
                }).catch(e => {
                    console.log(e);
                });
        }
    }
    componentDidMount() {
            axios.post('http://127.0.0.1:8000/accounts/api-token-auth/', qs.stringify({
            'username': 'satyamsoni2211',
            'password': 'satyam123'
        }))
            .then((response) => {
                // console.log(response)
                this.setState({ authToken: response.data.token });

            }).catch(error => { console.log(error) });
    }

    render() {
        let notes = <div> No content found </div>;
        if(this.state.notes.length > 1){
            notes = this.state.notes.map((n, index)=> <Note
            id={n.id}
            title={n.title}
            created={n.created}
            text={n.text}
            key={index}
            token = {this.state.authToken}
            />);
        }
        return notes;
    }
};

export default Notes;