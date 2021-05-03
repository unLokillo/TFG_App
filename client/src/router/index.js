import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LogIn from '../views/LogIn.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LogIn.vue'),
  },
  {
    path: '/forgot-password',
    name: 'forgot-password',
    component: () => import('@/views/ForgotPassword.vue'),
  },
  {
    path: '/create-user',
    name: 'Create User',
    component: () => import('@/views/CreateUser.vue'),
  },
  {
    path: '/create-neologisme',
    name: 'forgot-password',
    component: () => import('@/views/CreateNeologisme.vue'),
  },
  {
    path: '/view-neologisme',
    name: 'Ver Neologismo',
    component: () => import('@/views/ViewNeologisme.vue'),
  },
  {
    path: '/view-user/:userid',
    name: 'vUser',
    props: true,
    component: () => import('@/views/ViewUser.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
