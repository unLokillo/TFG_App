import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        meta: {
          showModal: true
        },
        path: 'fav-neo/:neoId',
        component: () => import('@/views/ViewNeologisme.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: '/login',
        name: 'login',
        props: true,
        component: () => import('@/views/LogIn.vue'),
      },
      {
        meta: {
        showModal: true
        },
        path: '/create-neologisme',
        name: 'Create Neologisme',
        props: true,
        component: () => import('@/views/CreateNeologisme.vue'),
      },
    ]
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
    path: '/view-neologisme/:neoid',
    name: 'vNeo',
    meta:{
      showModal: true,
    },
    props: true,
    component: () => import('@/views/ViewNeologisme.vue'),
  },
  {
    path: '/view-user/:userid',
    name: 'vUser',
    props: true,
    component: () => import('@/views/ViewUser.vue'),
    children: [
      {
        meta: {
          showModal: true
        },
        path: '/view-all-neologismes',
        component: () => import('@/views/View_All_Neologismes.vue'),
        props: true
      }
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
