import React, { useState } from "react";
import axios from "axios";

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    phone_number: "",
    password: "",
  });

  const handleInputChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post("/api/registration/", formData)
      .then((response) => {
        console.log("User registered successfully.");
      })
      .catch((error) => {
        console.log("An error occurred while registering the user:", error);
      });
  };

  return (
<header>
  <br />
  
    <form onSubmit={handleSubmit} className="formR">
      <div></div>
      <br/>
      <span class="span">S'enregistrer</span>
  <br/>


      <label>
       
        <input className="input" placeholder="      entrez votre nom ici" type="text" name="username" onChange={handleInputChange} />
      </label>
      <label>
      
        <input className="input" placeholder="      entrez votre  Email: ici" type="email" name="email" onChange={handleInputChange} />
      </label>
      <label>
       
        <input className="input" placeholder="     entrez votre numero de telephone ici" type="text" name="phone_number" onChange={handleInputChange} />
      </label>
      <label>
       
        <input className="input" placeholder="     entrez votre mot de pass ici" type="password" name="password" onChange={handleInputChange} />
      </label>
      <button type="submit">S'enregistrer</button>
    </form>
    </header>
  );
};
export default RegistrationForm;
