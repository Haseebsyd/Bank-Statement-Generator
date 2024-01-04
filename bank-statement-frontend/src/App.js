import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedin } from '@fortawesome/free-brands-svg-icons';
import { faGlobe } from '@fortawesome/free-solid-svg-icons';
import './App.css';
import bgPic from './assets/bg_pic.jpg';

function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    startDate: '',
    endDate: '',
    selectedUser: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;

    const regex = /^[A-Za-z]*$/;
    if ((name === 'firstName' || name === 'lastName') && !regex.test(value)) {
      alert('Only characters A-Z allowed');
      return;
    }
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  
    // Construct the POST request body with the form data
    const postData = {
      startDate: formData.startDate,
      endDate: formData.endDate,
      selectedUserEmail: formData.selectedUser,
      firstName: formData.firstName,
      lastName: formData.lastName,
      email: formData.email,
    };
    
    const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
    // Make the POST request to the backend
    fetch(`${backendUrl}/generate-statement`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(postData),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log(data);
      alert(data.message);
  
      // Clear firstName, lastName, and email fields after successful submission
      setFormData(prevFormData => ({
        ...prevFormData,
        firstName: '',
        lastName: '',
        email: '',
      }));
    })
    .catch(error => {
      console.error('There was an error with the request', error);
      alert('Error: ' + error.message);
    });
  };
  

  return (
    <div className="App" style={{ 
      backgroundImage: `url(${bgPic})`, 
      backgroundSize: 'cover', 
      backgroundPosition: 'center center', 
      backgroundRepeat: 'no-repeat', 
      backgroundAttachment: 'fixed' 
    }}>
      <div className="title">
        <h1 className="text-primary">Bank Statement Generator</h1>
      </div>
      <div className="card-container">
        <div className="card">
          <form onSubmit={handleSubmit} className="form-layout">
            <h2>Personal Information</h2>
            <div className="input-row name-row">
            <input 
                type="text" 
                name="firstName" 
                placeholder="First Name" 
                value={formData.firstName} 
                onChange={handleChange} 
                pattern="[A-Za-z]+" 
                title="Only characters A-Z allowed"
                required 
              />
              <input 
                type="text" 
                name="lastName" 
                placeholder="Last Name" 
                value={formData.lastName} 
                onChange={handleChange} 
                pattern="[A-Za-z]+" 
                title="Only characters A-Z allowed"
                required 
              />
            </div>
            <div className="input-row">
              <input 
                type="email" 
                name="email" 
                placeholder="Email" 
                value={formData.email} 
                onChange={handleChange} 
                required />
            </div>
            <hr className='separator-line'/>
            <h2>Enquiry Information</h2>
            <div className="input-row email-row">
              <select 
                name="selectedUser" 
                value={formData.selectedUser} 
                onChange={handleChange} 
                required
                >
                  <option value="">Email For Enquiry</option>
                  <option value="user1@gmail.com">user1@gmail.com</option>
                  <option value="user3@hotmail.com">user3@hotmail.com</option>
                  <option value="user2@yahoo.com">user2@yahoo.com</option>
              </select>
            </div>
            <div className="input-row date-row">
              <div className="date-input">
                <label htmlFor="startDate">Start Date</label>
                <input 
                  type="date" 
                  id="startDate" 
                  name="startDate" 
                  value={formData.startDate} 
                  onChange={handleChange} 
                  required max="9999-12-31"
                />
              </div>
              <div className="date-input">
                <label htmlFor="endDate">End Date</label>
                <input 
                  type="date" 
                  id="endDate" 
                  name="endDate" 
                  value={formData.endDate} 
                  onChange={handleChange} 
                  required max="9999-12-31"
                />
              </div>
            </div>
            <div className="button-container">
              <button type="submit">Generate Statement</button>
            </div>
            <div className="social-links">
              <a href="https://haseebsyd.github.io" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faGlobe} />
              </a>
              <a href="https://github.com/Haseebsyd" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faGithub} />
              </a>
              <a href="https://linkedin.com/in/haseeb--syed" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faLinkedin} />
              </a>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
