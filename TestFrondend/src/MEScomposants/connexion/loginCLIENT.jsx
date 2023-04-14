import React, { useState } from "react";
import axios from "axios";
import { Link } from 'react-router-dom';


const LoginForm = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
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
    axios.post("/api/login/", formData, { withCredentials: true })
      .then((response) => {
        console.log("User authenticated successfully.");
      })
      .catch((error) => {
        console.log("An error occurred while authenticating the user:", error);
      });
  };

  return (
    <form onSubmit={handleSubmit} className="form1">
      <div>
        </div><br/>
      <span class="span">Se connecter</span>
  <br/>
      <label>
      
        <input className="input" placeholder="      entrez votre nom d'utilisateur " type="text" name="username" onChange={handleInputChange} />
      </label>
      <label>
        
        <input className="input" placeholder="      entrez votre Email ici" type="email" name="email" onChange={handleInputChange} />
      </label>
      <label>
       
        <input className="input" placeholder="      entrez votre mot de pass ici" type="password" name="password" onChange={handleInputChange} />
      </label>
      <button type="submit">Se connecter</button>
      <br/>
      <li> 
        <Link to="/connexion/register" className="link">S'enregistrer</Link></li>	
        <li> <Link to="/connexion/reset" className="link">reinitialisez votre mot de pass</Link></li>	



    </form>
  );
};
export default LoginForm;