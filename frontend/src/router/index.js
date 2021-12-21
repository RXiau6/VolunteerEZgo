import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { 
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  { 
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    
    path: '/Login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    
    path: '/event',
    name: 'event',
    component: () => import('../views/event.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/register.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
