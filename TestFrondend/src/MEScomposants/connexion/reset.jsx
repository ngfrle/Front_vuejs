import React, { useState } from "react";
import axios from "axios";

const PasswordResetForm = () => {
    const [email, setEmail] = useState("");
  
    const handleInputChange = (event) => {
      setEmail(event.target.value);
    };
  
    const handleSubmit = (event) => {
      event.preventDefault();
      axios.post("/api/password-reset/", { email: email })
        .then((response) => {
          console.log("Password reset email sent.");
        })
        .catch((error) => {
          console.log("An error occurred while sending password reset email:", error);
        });
    };
  
    return (
        <header>
            <br />
            <br />
        <form onSubmit={handleSubmit} className="formr">
        <div></div>
        <br/>
      <span class="span">Reinitialiser votre mot de pass</span>
  <br/>
            <label>
            <input className="input" placeholder="entrez votre email" type="email" name="email" onChange={handleInputChange} />
            </label>
            <button type="submit">Reinitialiser</button>
        </form>
      </header>
    );
  };
export default PasswordResetForm ;