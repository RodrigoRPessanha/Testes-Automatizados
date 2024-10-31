import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css'; // Importando o CSS

function Menu() {
  return (
    <nav className="menu">
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/doctors">Manage Doctors</Link></li>
        <li><Link to="/patients">Manage Patients</Link></li>
        <li><Link to="/appointments">Manage Appointments</Link></li>
      </ul>
    </nav>
  );
}

export default Menu;