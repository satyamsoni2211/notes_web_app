import { Navbar, Nav, NavItem } from 'react-bootstrap';
import React from 'react';
// import Logo from '../../Assets/Logo/note.png';
import Aux from '../../hoc/Aux';

const style = {
    backgroundColor: 'inherit',
    borderBottom: 'none',
    marginBottom: '0'
};
const navbar = (props) => (
    <Aux>
        <Navbar style={style}>
            <Navbar.Header>
                <Navbar.Brand>
                    {/* <a href="#home">React-Bootstrap</a> */}
                    <img src='../../Assets/Logo/note.png' alt='Brand'/>
                </Navbar.Brand>
            </Navbar.Header>
            { props.token ? <Nav pullRight>
                <NavItem eventKey={1} >
                   <i className="glyphicon glyphicon-user" onClick={props.logoutHandler}></i>
            </NavItem>
            </Nav> : null }
        </Navbar>
       { props.token ? <Nav bsStyle="tabs" >
            <NavItem eventKey="1" href="#">
                View Notes
        </NavItem>
        <NavItem eventKey="2">
                Create Note
        </NavItem>
            <NavItem eventKey="3">
                Share Notes
        </NavItem>
            <NavItem eventKey="4">
                Share By Me Notes
         </NavItem>
         </Nav>: null}
    </Aux>
);
export default navbar;