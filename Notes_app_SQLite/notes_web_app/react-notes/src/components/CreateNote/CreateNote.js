import React , {Component} from 'react';

class CreateNote extends Component {
    render(){
        return (
            <div>
            <form>
            <label htmlFor="title">Enter Title</label>
            <input type="text" name='title' />
            <label htmlFor="text">Enter text</label>
            <input type="text" name='text'/>
            <button className='btn btn-primary'>Create</button>
            </form>
            </div>
        ); 
    }
}

export default CreateNote;