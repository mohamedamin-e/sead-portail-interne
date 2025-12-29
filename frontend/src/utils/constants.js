/**
 * ROUTES DE L'APPLICATION (FRONTEND)
 */
export const APP_ROUTES = {
  LOGIN: '/',
  DASHBOARD: '/dashboard',
  
  // Module Données
  FICHE_EXPLOITANT: '/donnees/exploitant', // Fiche 1
  FICHE_PROVINCIALE: '/donnees/provinciale', // Fiche 2
  FICHE_FONCIER: '/donnees/foncier', // Fiche 3
  FICHE_NUTRITION: '/donnees/nutrition', // Fiche 4
  FICHE_FILIERES: '/donnees/filieres', // Fiche 5
  
  // Module Qualité
  SYNC_FLUX: '/qualite/synchronisation',
  ANOMALIES: '/qualite/anomalies',
  
  // Module Analyse
  MAPS: '/analyse/cartes',
  REPORTS: '/analyse/rapports',
  
  // Module Administration
  ADMIN_USERS: '/admin/utilisateurs',
  ADMIN_ROLES: '/admin/roles-permissions',
  ADMIN_REFERENTIELS: '/admin/referentiels',
  ADMIN_INDICATEURS: '/admin/indicateurs',
  ADMIN_LOGS: '/admin/logs',
};

/**
 * ENDPOINTS DE L'API (BACKEND DJANGO)
 */
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login/',
    REFRESH: '/auth/token/refresh/',
    LOGOUT: '/auth/logout/',
  },
  DASHBOARD: {
    KPIS: '/stats/kpi-summary/',
    CHARTS: '/stats/charts/',
  },
  FICHES: {
    BASE: '/fiches/',
    VALIDATE: (id) => `/fiches/${id}/validate/`,
  },
  ADMIN: {
    USERS: '/admin/users/',
    LOGS: '/admin/audit-logs/',
  }
};