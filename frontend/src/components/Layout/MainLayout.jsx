import React from 'react';
import { Outlet, NavLink } from 'react-router-dom';
import { APP_ROUTES } from '../../utils/constants';
import './MainLayout.css';
import armoiries from '../../assets/react.svg';
import etafat from '../../assets/etafat-logo.png';

const MainLayout = () => {
  return (
    <div className="admin-container">
      {/* SIDEBAR FIXE A GAUCHE */}
      <aside className="sidebar">
        <div className="sidebar-top">
          <img src={armoiries} alt="Crest" className="sidebar-logo" />
          <h2 className="sidebar-title">Portail interne SEAD</h2>
        </div>

        <nav className="sidebar-nav">
          <NavLink to={APP_ROUTES.DASHBOARD} className={({isActive}) => isActive ? "nav-item active" : "nav-item"}>
             Suivi et évaluation
          </NavLink>
          <NavLink to={APP_ROUTES.FICHE_EXPLOITANT} className="nav-item">
             Contrôle de données
          </NavLink>
          <NavLink to={APP_ROUTES.MAPS} className="nav-item">
             Génération automatique des cartes
          </NavLink>
          <NavLink to={APP_ROUTES.ADMIN_USERS} className="nav-item">
             Gestion des utilisateurs
          </NavLink>
        </nav>

        <div className="sidebar-footer">
          <img src={etafat} alt="ETAFAT" className="footer-logo-img" />
          <span className="footer-text">ETAFAT</span>
        </div>
      </aside>

      {/* ZONE DE CONTENU A DROITE */}
      <main className="main-content">
        <header className="content-header">
           <div className="welcome-card">
              <h3>Bonjour , utilisateur x</h3>
           </div>
        </header>
        <section className="page-container">
          <Outlet /> {/* Les pages comme Dashboard s'afficheront ici */}
        </section>
      </main>
    </div>
  );
};

export default MainLayout;