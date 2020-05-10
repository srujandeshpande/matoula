import React,{Component} from 'react';
import './profile.css';

class Profile extends Component{
  render(){
   return(

  <div className="card">
  <img className="dp" src="https://www.w3schools.com/w3images/team2.jpg" alt="John" />
  <h1>John Doe</h1>
  <p className="title">Welcome back dave!</p>
  <p>Harvard University</p>
  
  </div>
)
}
}

export default Profile;

