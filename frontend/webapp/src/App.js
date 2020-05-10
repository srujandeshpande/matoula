import React from 'react';
import logo from './logo.svg';
import Navbar from './components/Navbar.js'
import Profile from './components/Profile.js'
import Today from './components/Today.js'
import './App.css';

function App() {
  return (
    <div>
    <Navbar />
    <div className="App">
        
        <div className = "card_ui">

          <Profile/>
          <Today />
        </div>
    </div>
    </div>
  );
}

export default App;
