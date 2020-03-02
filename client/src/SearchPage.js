import React from 'react'
import 'bootstrap/dist/js/bootstrap.bundle'
//import { Router, Switch, Route, Link } from 'react-router-dom'
import NavBar from './NavBar'
import DynamicCards from './DynamicCards'
import Login from './Login'
import axios from 'axios'

class App extends React.Component {
	constructor(props){
		super(props);
		this.state = { 
			showLogin: false 
			
		}
	};
	
		 
	
	 getLoginWindowStatus = (loginWindowStatus) => {
        this.setState({showLogin : !loginWindowStatus});
    };
	
	render(){
		
	return (
		<React.Fragment>
			<div>
			<NavBar 
				getWindowStatus = {this.getLoginWindowStatus}
			/>
			<Login />
			<DynamicCards />
			</div>
		</React.Fragment>
	  )
	}
	
};

export default App;