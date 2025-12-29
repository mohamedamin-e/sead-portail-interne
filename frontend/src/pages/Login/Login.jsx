import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import pour la navigation
import { APP_ROUTES } from '../../utils/constants'; // Import de tes constantes
import './Login.css';

// Importation des images
import armoiriesLogo from '../../assets/react.svg'; // Vérifie que le nom est correct
import etafatLogo from '../../assets/etafat-logo.png';

const Login = () => {
  const [email, setEmail] = useState('allali.mohamedamine@gmail.com');
  const [password, setPassword] = useState('');
  
  const navigate = useNavigate(); // Initialisation du hook de navigation

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Simulation d'une connexion réussie
    console.log("Tentative de connexion avec :", email);
    
    // On stocke un faux token pour simuler l'authentification
    localStorage.setItem('token', 'connected_user_token');
    
    // Redirection vers le dashboard après le clic
    navigate(APP_ROUTES.DASHBOARD);
  };

  return (
    <div className="login-container">
      <div className="login-overlay"></div>

      <div className="login-card">
        <div className="login-header">
          <img src={armoiriesLogo} alt="Armoiries Burundi" className="crest-logo" />
          <h1 className="login-title">Connexion</h1>
          <p className="login-subtitle">Veuillez entrer vos identifiants</p>
        </div>

        <form onSubmit={handleSubmit} className="login-form">
          <div className="input-group">
            <label>Email :</label>
            <input 
              type="email" 
              value={email} 
              onChange={(e) => setEmail(e.target.value)} 
              required
            />
          </div>

          <div className="input-group">
            <label>Mot de passe :</label>
            <input 
              type="password" 
              placeholder="**********"
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              required
            />
          </div>

          <button type="submit" className="login-button">Se connecter</button>
          
          <a href="#" className="forgot-password">Mot de passe oublié ?</a>
        </form>
      </div>

      <div className="footer-logo">
        <img src={etafatLogo} alt="Logo ETAFAT" />
        <span>ETAFAT</span>
      </div>
    </div>
  );
};

export default Login;