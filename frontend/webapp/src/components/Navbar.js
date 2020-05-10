import React,{Component} from 'react';


class Navbar extends Component{
  render(){
   return(
    <div className="navbar navbar-inverse">
  <div className="container-fluid">
    <div className="navbar-header">
      <a className="navbar-brand" href="#">Matoula</a>
    </div>
    
    <a className="btn btn-danger navbar-btn"><p>Home</p></a>
    <a className="btn btn-danger navbar-btn"><p>Wardrobe</p></a>
  </div>
</div>)
}
}

export default Navbar;

