import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css'; // Importando o CSS
import logo from '../logo.gif'; // Importando o GIF
import Menu from './Menu'; // Importando o Menu

function AppointmentPage() {
  const [appointment, setAppointment] = useState({
    date: '',
    patientId: '',
    doctorId: ''
  });
  const [appointments, setAppointments] = useState([]);
  const [appointmentId, setAppointmentId] = useState('');

  useEffect(() => {
    fetchAppointments();
  }, []);

  const fetchAppointments = () => {
    axios.get('http://localhost:8000/appointments/')
      .then((response) => {
        setAppointments(response.data);
      })
      .catch((error) => {
        console.error('Error fetching appointments:', error);
      });
  };

  const fetchAppointmentById = () => {
    if (!appointmentId) {
      fetchAppointments();
      return;
    }
    axios.get(`http://localhost:8000/appointments/${appointmentId}`)
      .then((response) => {
        setAppointments([response.data]);
      })
      .catch((error) => {
        console.error('Error fetching appointment by ID:', error);
      });
  };

  const handleChange = (e) => {
    setAppointment({ ...appointment, [e.target.name]: e.target.value });
  };

  const handleIdChange = (e) => {
    setAppointmentId(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Submitting appointment:', appointment); // Log para depuração
    axios.post('http://localhost:8000/appointments/', {
      doctor_id: appointment.doctorId,
      patient_id: appointment.patientId,
      date: appointment.date
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        alert('Appointment created successfully!');
        fetchAppointments(); // Atualiza a lista de consultas após adicionar uma nova
      })
      .catch((error) => {
        if (error.response) {
          const errorDetails = error.response.data.detail;
          const errorMessage = Array.isArray(errorDetails)
            ? errorDetails.map(err => err.msg).join(', ')
            : errorDetails;
          alert('Error creating appointment: ' + errorMessage);
        } else if (error.request) {
          alert('Error creating appointment: No response from server.');
        } else {
          alert('Error creating appointment: ' + error.message);
        }
      });
  };

  return (
    <div>
      <img src={logo} alt="Logo" className="logo" />
      <Menu />
      <h2>Create Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label>Date:</label>
        <input
          type="datetime-local"
          name="date"
          value={appointment.date}
          onChange={handleChange}
          required
        /><br/>
        <label>Patient ID:</label>
        <input
          type="text"
          name="patientId"
          value={appointment.patientId}
          onChange={handleChange}
          required
        /><br/>
        <label>Doctor ID:</label>
        <input
          type="text"
          name="doctorId"
          value={appointment.doctorId}
          onChange={handleChange}
          required
        /><br/>
        <button type="submit">Create Appointment</button>
      </form>

      <h2>Appointments List</h2>
      <div>
        <label>Appointment ID:</label>
        <input
          type="text"
          value={appointmentId}
          onChange={handleIdChange}
        />
        <button onClick={fetchAppointmentById}>Fetch Appointment by ID</button>
        <button onClick={fetchAppointments}>Refresh List</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Patient ID</th>
            <th>Doctor ID</th>
          </tr>
        </thead>
        <tbody>
          {appointments.map((app) => (
            <tr key={app.id}>
              <td>{app.id}</td>
              <td>{app.date}</td>
              <td>{app.patient_id}</td>
              <td>{app.doctor_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AppointmentPage;