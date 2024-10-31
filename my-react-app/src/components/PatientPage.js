import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css'; // Importando o CSS
import logo from '../logo.gif'; // Importando o GIF
import Menu from './Menu'; // Importando o Menu

function PatientPage() {
  const [patient, setPatient] = useState({
    name: '',
    age: ''
  });
  const [patients, setPatients] = useState([]);
  const [patientId, setPatientId] = useState('');

  useEffect(() => {
    fetchPatients();
  }, []);

  const fetchPatients = () => {
    axios.get('http://localhost:8000/patients/')
      .then((response) => {
        setPatients(response.data);
      })
      .catch((error) => {
        console.error('Error fetching patients:', error);
      });
  };

  const fetchPatientById = () => {
    if (!patientId) {
      fetchPatients();
      return;
    }
    axios.get(`http://localhost:8000/patients/${patientId}`)
      .then((response) => {
        setPatients([response.data]);
      })
      .catch((error) => {
        console.error('Error fetching patient by ID:', error);
      });
  };

  const handleChange = (e) => {
    setPatient({ ...patient, [e.target.name]: e.target.value });
  };

  const handleIdChange = (e) => {
    setPatientId(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/patients/', patient)
      .then((response) => {
        alert('Patient created successfully!');
        fetchPatients(); // Atualiza a lista de pacientes após adicionar um novo
      })
      .catch((error) => {
        alert('Error creating patient: ' + error.message);
      });
  };

  return (
    <div>
      <img src={logo} alt="Logo" className="logo" />
      <Menu />
      <h2>Create Patient</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={patient.name}
          onChange={handleChange}
          required
        /><br/>
        <label>Age:</label>
        <input
          type="number"
          name="age"
          value={patient.age}
          onChange={handleChange}
          required
        /><br/>
        <button type="submit">Create Patient</button>
      </form>

      <h2>Patients List</h2>
      <div>
        <label>Patient ID:</label>
        <input
          type="text"
          value={patientId}
          onChange={handleIdChange}
        />
        <button onClick={fetchPatientById}>Fetch Patient by ID</button>
        <button onClick={fetchPatients}>Refresh List</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {patients.map((pat) => (
            <tr key={pat.id}>
              <td>{pat.id}</td>
              <td>{pat.name}</td>
              <td>{pat.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default PatientPage;