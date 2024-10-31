import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import DoctorPage from './components/DoctorPage';
import PatientPage from './components/PatientPage';
import AppointmentPage from './components/AppointmentPage';
import './App.css'; // Importando o CSS

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/doctors" element={<DoctorPage />} />
          <Route path="/patients" element={<PatientPage />} />
          <Route path="/appointments" element={<AppointmentPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;