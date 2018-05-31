import { Navbar, Nav, NavItem } from 'react-bootstrap';
import React from 'react';
import Logo from '../../Assets/Logo/note.png';
import Aux from '../../hoc/Aux';
import { Link } from 'react-router-dom';
import './Navbar.css';

const style = {
    backgroundColor: 'inherit',
    borderBottom: 'none',
    marginBottom: '0'
};
const navbar = (props) => (
    <Aux>          
             <ul>
                <li><img src={Logo} alt='Brand' /></li>
                {window.sessionStorage.getItem('token') ?
                <Aux>
                <li><Link to='/view_notes'>View Notes</Link></li>
                <li><Link to='/create_notes'>Create Note </Link></li>
                <li>Shared with me </li>
                <li>Shared by me </li> 
                <li><i className="glyphicon glyphicon-user" onClick={props.logoutHandler}></i></li>
                </Aux>
                : null }
            </ul>
    </Aux>
        );
        // <Navbar style={style}>
        //     <Navbar.Header>
        //         <Navbar.Brand>
        //             <img src={Logo} alt='Brand' />
        //         </Navbar.Brand>
        //     </Navbar.Header>
        //     {window.sessionStorage.getItem('token') ? <Nav pullRight>
        //         <NavItem eventKey={1} >
        //             <i className="glyphicon glyphicon-user" onClick={props.logoutHandler}></i>
        //         </NavItem>
        //     </Nav> : null}
        //     </Navbar>  
            //     </Navbar>
    //    { window.sessionStorage.getItem('token') ? <Nav bsStyle="tabs" >
    //         <NavItem eventKey="1" >
    //         <Link to='/'>View Notes</Link>
    //     </NavItem>
    //     <NavItem eventKey="2" >
    //             <Link to='/create_notes'>Create Note </Link>
    //     </NavItem>
    //         <NavItem eventKey="3">
    //             Share Notes
    //     </NavItem>
    //         <NavItem eventKey="4">
    //             Share By Me Notes
    //      </NavItem>
    //      </Nav>: null}
export default navbar;