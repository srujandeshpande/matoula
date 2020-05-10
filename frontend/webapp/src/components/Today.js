import React,{Component} from 'react';
import './cloth.css';
import Cloth from './Cloth.js'
class Today extends Component{
  render(){
   return(

  <div className="Today Header">
  
  <hr/>
  <h3><p>So what did you wear today</p></h3>
  <hr/>
  {//code for getting which cloth
  }
  <Cloth/>
  <p><button>Add Apparel</button></p>
</div>
  
 
)
}
}

export default Today;