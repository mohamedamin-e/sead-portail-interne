import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';

// Import de tes composants
import Login from './pages/Login/Login';
import MainLayout from './components/Layout/MainLayout';
import Dashboard from './pages/Dashboard/Dashboard';

function App() {
  // Vérification si l'utilisateur est connecté (présence du token)
  const isAuthenticated = localStorage.getItem('token') !== null;

  return (
    <Router>
      <Routes>
        {/* 1. ROUTE LOGIN : Elle est en dehors du MainLayout pour ne pas avoir la barre verte */}
        <Route path="/login" element={<Login />} />

        {/* 2. ROUTES PROTEGEES : Elles utilisent le MainLayout (Sidebar verte) */}
        <Route path="/" element={<MainLayout />}>
          
          {/* Redirection automatique à la racine '/' */}
          <Route index element={
            isAuthenticated ? <Navigate to="/dashboard" replace /> : <Navigate to="/login" replace />
          } />

          {/* Page Dashboard */}
          <Route path="dashboard" element={<Dashboard />} />
          
          {/* Pages temporaires pour les autres menus */}
          <Route path="donnees/exploitant" element={<div style={{padding: '20px'}}><h1>Fiche Exploitant</h1></div>} />
          <Route path="analyse/cartes" element={<div style={{padding: '20px'}}><h1>Génération des cartes</h1></div>} />
          <Route path="admin/utilisateurs" element={<div style={{padding: '20px'}}><h1>Gestion Utilisateurs</h1></div>} />
        </Route>

        {/* 3. CAS D'ERREUR : Si l'URL n'existe pas */}
        <Route path="*" element={<div style={{padding: '50px'}}><h1>404 - Page non trouvée</h1></div>} />
      </Routes>
    </Router>
  );
}

export default App;