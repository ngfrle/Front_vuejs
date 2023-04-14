import React from 'react';
import ReactDOM from 'react-dom';
// import ContactForm from '/ContactForm';

// ReactDOM.render(<ContactForm />, document.getElementById('root'));

import { useState } from 'react';

const BodyContact = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [subject, setSubject] = useState('');
  const [description, setDescription] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitted(true);
  }

  return (
    <div>
      <h1>Quel probleme rencontrez vous?</h1><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
      {isSubmitted ?
        <p>Thank you for contacting us!</p>
        :
        
        <form onSubmit={handleSubmit} className='form'>
          <div>
            <label htmlFor="name">Name: </label>
            <input className='input' type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} required />
          </div>
          <div>
            <label htmlFor="email">Email: </label>
            <input className='input' type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div>
            <label htmlFor="phone">Phone Number: </label>
            <input className='input' type="tel" id="phone" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} required />
          </div>
          <div>
            <label htmlFor="subject">Subject: </label>
            <input className='input' type="text" id="subject" value={subject} onChange={(e) => setSubject(e.target.value)} required />
          </div>
          <div>
            <label htmlFor="description">Description: </label>
            <textarea className="text"id="description" rows="5" value={description} onChange={(e) => setDescription(e.target.value)} required></textarea>
          </div>
          <button type="submit"className='btn btn-warning'>Submit</button>
        </form>
      }
    </div>
  );
}

export default BodyContact;