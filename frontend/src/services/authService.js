import api from './api';
import { API_ENDPOINTS } from '../utils/constants';

export const loginUser = async (credentials) => {
    // EN PRODUCTION :
    // return await api.post(API_ENDPOINTS.LOGIN, credentials);

    // EN ATTENDANT LE BACKEND (Simulation) :
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (credentials.email === "admin@sead.bi" && credentials.password === "admin") {
                resolve({ data: { token: 'fake-jwt-token', user: { name: 'Admin SEAD' } } });
            } else {
                reject({ response: { data: { message: 'Identifiants invalides' } } });
            }
        }, 1000);
    });
};