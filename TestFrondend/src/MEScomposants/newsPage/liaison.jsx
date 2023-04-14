import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Accueil from '../index.jsx';
import Shop from '../restaurant/shop.jsx';
import Chariot from '../CHARIOT/chariot.jsx';
import Contact from '../CONTACT/Contact.jsx';
import  Login from '../connexion/login.jsx';
import PasswordResetForm from '../connexion/reset.jsx'
import RegistrationForm from '../connexion/registerCLIENT.jsx'




const Liaison = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/"element={<Accueil />} />
      <Route path="/restaurant/shop" element={<Shop />} />
      <Route path="/CHARIOT/chariot" element={<Chariot />} />
      <Route path="/CONTACT/Contact" element={<Contact />} />
      <Route path="/connexion/login" element={<Login/>} />
      <Route path="/connexion/reset" element={<PasswordResetForm/>} />
      <Route path="/connexion/register" element={<RegistrationForm/>} />



    </Routes>
  </BrowserRouter>
);

export default Liaison;


