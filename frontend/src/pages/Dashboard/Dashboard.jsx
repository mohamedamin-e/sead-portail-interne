import React from 'react';
import './Dashboard.css';

const Dashboard = () => {
  return (
    <div className="dashboard-grid">
      {/* 1. BARRE DE FILTRES */}
      <div className="card filter-bar">
        <div className="filter-group">
          <label>Variable</label>
          <select><option>Orge</option></select>
        </div>
        <div className="filter-group">
          <label>Périodicité</label>
          <select><option>Mensuelle</option></select>
        </div>
        <div className="filter-group">
          <label>Année X</label>
          <select><option>2021</option></select>
        </div>
        <div className="filter-group">
          <label>Année Y</label>
          <select><option>2022</option></select>
        </div>
        <div className="filter-group">
          <label>Région</label>
          <select><option>Casablanca-Settat</option></select>
        </div>
      </div>

      {/* 2. GRAPHIQUE ET VARIANCES */}
      <div className="row">
        <div className="card chart-large">
          <h4>Évolution des prix (Comparaison X vs Y)</h4>
          <div className="placeholder-box">Graphique ici</div>
        </div>
        <div className="card variance-small">
          <h4>Variances</h4>
          <p>Mensuelle : <strong>+4.2%</strong></p>
          <p>Trimestrielle : <strong>+8.1%</strong></p>
          <p>Annuelle : <strong>+12.6%</strong></p>
        </div>
      </div>

      {/* 3. CARTE */}
      <div className="card full-width">
        <h4>Répartition par région</h4>
        <div className="placeholder-box map">Carte du Maroc ici</div>
      </div>

      {/* 4. KPI CARDS */}
      <div className="kpi-row">
        <div className="card kpi"><span>Prix moyen 2024</span><strong>3.25 DH/kg</strong><small className="up">+5.3%</small></div>
        <div className="card kpi"><span>Prix moyen 2023</span><strong>2.98 DH/kg</strong><small className="down">-1.2%</small></div>
        <div className="card kpi"><span>Variation Max</span><strong>+18%</strong><small>Région Fès</small></div>
        <div className="card kpi"><span>Variation Min</span><strong>-6%</strong><small>Région Sud</small></div>
      </div>

      {/* 5. TABLEAU */}
      <div className="card full-width">
        <h4>Comparaison des prix par région</h4>
        <table className="data-table">
          <thead>
            <tr><th>Région</th><th>Prix Année X</th><th>Prix Année Y</th><th>Variation</th></tr>
          </thead>
          <tbody>
            <tr><td>Casablanca-Settat</td><td>3.40 DH</td><td>3.15 DH</td><td>+8%</td></tr>
            <tr><td>Fès Meknès</td><td>3.60 DH</td><td>3.00 DH</td><td>+20%</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;