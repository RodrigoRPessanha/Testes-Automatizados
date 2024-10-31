import React from 'react';
import '../App.css'; // Importando o CSS
import logo from '../logo.gif'; // Importando o GIF
import Menu from './Menu'; // Importando o Menu

function HomePage() {
  return (
    <div className="container">
      <img src={logo} alt="Logo" className="logo" />
      <Menu />
      <div className="homepage">
        <h2>Welcome to the Medical Management System</h2>
        <p>Manage your medical practice efficiently with our comprehensive system.</p>
        <div className="cards">
          <div className="card">
            <h3>Manage Doctors</h3>
            <p>Keep track of doctor information and specialties.</p>
          </div>
          <div className="card">
            <h3>Manage Patients</h3>
            <p>Maintain detailed records of patient information.</p>
          </div>
          <div className="card">
            <h3>Manage Appointments</h3>
            <p>Schedule and manage appointments with ease.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;