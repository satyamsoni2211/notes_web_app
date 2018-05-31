import React , {Component} from 'react';
import './CreateNote.css';
import axios from 'axios';

class CreateNote extends Component {
    state = {
        title : null,
        text: null
    }
    createNote = (e) => {
        e.preventDefault();
        console.log(this.props);
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/create/',
        data: {
            title : this.state.title,
            text: this.state.text
        },
        headers: {
            Authorization: `JWT ${this.props.token}`
        }
        }).then(r => {
            this.props.history.push('/view_notes');
        })
        .catch(err => {
            console.log(err.response);
            console.log(this.props);
            if (err.response.data.detail == 'Signature has expired.'){
                this.props.logout();
            }
        });
    }
    render(){
        return (
            <div>
            <form className='box'>
            <label>Title: </label><input type="text" name='title' placeholder='Type your title here '
            onChange= {e => this.setState({title: e.target.value})}/>
            <hr/>
            <textarea name="text" id="" cols="30" rows="10" placeholder='Type your Note here'
            onChange= {e => this.setState({text: e.target.value})}></textarea>
            <br/>
            <button className='btn btn-primary' onClick={(e)=> this.createNote(e)}>Create</button>
            </form>
            </div>
        ); 
    }
}

export default CreateNote;