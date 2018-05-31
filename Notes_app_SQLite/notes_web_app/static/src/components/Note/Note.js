import React, { Component } from 'react';
import './Note.css';
import axios from 'axios';

class Note extends Component {
    state = {
        text: this.props.text
    }
    updateNote(id) {
        console.log(`Updating Note with text ${this.state.text}`);
        axios({
            method: 'post',
            url: `http://127.0.0.1:8000/api/Notes/${id}/`,
            headers: { Authorization: `JWT ${this.props.token}` },
            data: {
                'text': this.state.text,
            }
        })
            .then((response) => {
                // console.log(response)
                console.log(response);

            }).catch(error => { console.log(error) });
    }
    render() {
        return (
            <div className="note-wrap note-white col-md-3">
                <h2>{this.props.title}</h2>
                <hr />
                <textarea name="text" cols="15" rows="5"
                    value={this.state.text}
                    onChange={(e) => { this.setState({ text: e.target.value }); }}>
                </textarea>
                <h5 className="help-block" id='usertag'>Created at: {this.props.created}</h5>
                <i className="fas fa-edit" onClick={() => { this.updateNote(this.props.id) }}></i>
            </div>);
    }
}

export default Note;