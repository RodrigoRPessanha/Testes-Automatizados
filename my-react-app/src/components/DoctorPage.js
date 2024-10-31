import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css'; // Importando o CSS
import logo from '../logo.gif'; // Importando o GIF
import Menu from './Menu'; // Importando o Menu

function DoctorPage() {
  const [doctor, setDoctor] = useState({
    name: '',
    specialty: ''
  });
  const [doctors, setDoctors] = useState([]);
  const [doctorId, setDoctorId] = useState('');

  useEffect(() => {
    fetchDoctors();
  }, []);

  const fetchDoctors = () => {
    axios.get('http://localhost:8000/doctors/')
      .then((response) => {
        setDoctors(response.data);
      })
      .catch((error) => {
        console.error('Error fetching doctors:', error);
      });
  };

  const fetchDoctorById = () => {
    if (!doctorId) {
      fetchDoctors();
      return;
    }
    axios.get(`http://localhost:8000/doctors/${doctorId}`)
      .then((response) => {
        setDoctors([response.data]);
      })
      .catch((error) => {
        console.error('Error fetching doctor by ID:', error);
      });
  };

  const handleChange = (e) => {
    setDoctor({ ...doctor, [e.target.name]: e.target.value });
  };

  const handleIdChange = (e) => {
    setDoctorId(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/doctors/', doctor, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        alert('Doctor created successfully!');
        fetchDoctors(); // Atualiza a lista de médicos após adicionar um novo
      })
      .catch((error) => {
        if (error.response) {
          const errorDetails = error.response.data.detail;
          const errorMessage = Array.isArray(errorDetails)
            ? errorDetails.map(err => err.msg).join(', ')
            : errorDetails;
          alert('Error creating doctor: ' + errorMessage);
        } else if (error.request) {
          alert('Error creating doctor: No response from server.');
        } else {
          alert('Error creating doctor: ' + error.message);
        }
      });
  };

  return (
    <div>
      <img src={logo} alt="Logo" className="logo" />
      <Menu />
      <h2>Create Doctor</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={doctor.name}
          onChange={handleChange}
          required 
        /><br/>
        <label>Specialty:</label>
        <input
          type="text"
          name="specialty"
          value={doctor.specialty}
          onChange={handleChange}
          required
        /><br/>
        <button type="submit">Submit</button>
      </form>

      <h2>Doctors List</h2>
      <div>
        <label>Doctor ID:</label>
        <input
          type="text"
          value={doctorId}
          onChange={handleIdChange}
        />
        <button onClick={fetchDoctorById}>Fetch Doctor by ID</button>
        <button onClick={fetchDoctors}>Refresh List</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Specialty</th>
          </tr>
        </thead>
        <tbody>
          {doctors.map((doc) => (
            <tr key={doc.id}>
              <td>{doc.id}</td>
              <td>{doc.name}</td>
              <td>{doc.specialty}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DoctorPage;