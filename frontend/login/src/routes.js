import Login from './components/Login.vue';
import Header from './components/Header.vue';
import Home from './components/Home.vue';

export const routes = [
    {
      path: '/login',
      component: Login
    },
    {
      path: '/',
      components: {
        default: Home,
        nav: Header
      }
    },
    {
        path: '*',
        redirect: '/',
      }
  ];