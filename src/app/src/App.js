import './App.css';
import axiosInstance from '../AuthComp/AxiosInstance'
import view_task from './view_task';
import post_task from './post_task';
import React, { useState , useEffect} from 'react';
const App = () => {
 
  return (
    <div className="App">
      <view_task/>
      <post_task/>
    </div>
  );
}

export default App;
