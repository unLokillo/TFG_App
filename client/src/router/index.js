import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import View_Proposals_User from '../components/User_View/View_Proposals_User.vue'
import View_Neologisme from '../views/ViewNeologisme.vue'
import badges_menu from '../components/User_View/badges_menu.vue'
Vue.use(VueRouter)

var route = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        meta: {
          showModal: true
        },
        path: 'badges_menu',
        name: 'badges',
        component: badges_menu,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-proposals',
        name: 'main-view-all-proposals',
        component: View_Proposals_User,
        props: true
      },
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
        path: 'fav-neo/:neoId/reject-neologisme',
        name: 'r-neologismes',
        component: () => import('@/views/Reject_Neologisme.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'fav-neo/:neoId/modify-neologisme',
        name: 'm-neologismes',
        component: () => import('@/components/User_View/modify_proposal.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'login',
        name: 'login',
        props: true,
        component: () => import('@/views/LogIn.vue'),
      },
      {
        meta: {
        showModal: true
        },
        path: 'create-neologisme',
        name: 'Create Neologisme',
        props: true,
        component: () => import('@/views/CreateNeologisme.vue'),
      },
      {
        meta: {
          showModal: true
        },
        path: 'forgot-password',
        name: 'forgot-password',
        component: () => import('@/components/Main/fp-email.vue'),
      },
      {
        meta: {
          showModal: true
        },
        path: 'forgot-password/:userId/code',
        name: 'forgot-password-c',
        component: () => import('@/views/ForgotPassword.vue'),
      },
      {
        meta: {
          showModal: true
        },
        path: 'forgot-password/:userId/reset',
        name: 'forgot-password-cp',
        component: () => import('@/components/Main/Change-password.vue'),
      },
      {
        meta: {
          showModal: true
        },
        path: 'create-user',
        name: 'create-user',
        component: () => import('@/views/CreateUser.vue'),
      },
      {
        meta: {
          showModal: true
        },
        path: 'ranking_users',
        name: 'ranking',
        component: () => import('@/components/User_View/Ranking.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'ranking_neologismes',
        name: 'ranking_neo',
        component: () => import('@/components/Main/All_Neologismes_Ranking.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'faq',
        name: 'faq',
        component: () => import('@/components/faq.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'info',
        name: 'info',
        component: () => import('@/components/info.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'info_general',
        name: 'info_general',
        component: () => import('@/components/general_info.vue'),
        props: true
      }
    ]
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
    path: '/view-user/:userid/',
    name: 'vUser',
    props: true,
    component: () => import('@/views/ViewUser.vue'),
    children: [
      {
        meta: {
          showModal: true
        },
        path: 'ranking_neologismes',
        name: 'vu-ranking_neo',
        component: () => import('@/components/Main/All_Neologismes_Ranking.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-neologismes',
        name: 'view-all-neologismes',
        component: () => import('@/components/User_View/View_All_Neologismes.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-proposals',
        name: 'view-all-proposals',
        component: View_Proposals_User,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'badges_menu',
        name: 'vu-badges',
        component: badges_menu,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'ranking',
        name: 'vu-ranking',
        component: () => import('@/components/User_View/Ranking.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-neologisme/:neoId',
        name: 'v-neologisme',
        component: View_Neologisme,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-proposals/view-neologisme/:neoId',
        name: 'vp-neologismes',
        component: View_Neologisme,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-proposals/view-neologisme/:neoId',
        name: 'v-neologismes',
        component: View_Neologisme,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-all-neologismes/view-neologisme/:neoId/reject-neologisme',
        name: 'rp-neologismes',
        component: () => import('@/views/Reject_Neologisme.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'notify-error',
        name: 'n-error',
        component: () => import('@/views/Notify_Error.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'modify_profile',
        name: 'm-perfil',
        component: () => import('@/components/User_View/modify_profile.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'view-neologisme/:neoId/modify_proposal',
        name: 'm-proposal',
        component: () => import('@/components/User_View/modify_proposal.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'fav_neologismes',
        name: 'f-neo',
        component: () => import('@/components/User_View/fav-neologismes.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'fav_neologismes/view-neologisme/:neoId',
        name: 'fv-neologismes',
        component: View_Neologisme,
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'faq',
        name: 'faq',
        component: () => import('@/components/faq.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'info',
        name: 'info',
        component: () => import('@/components/info.vue'),
        props: true
      },
      {
        meta: {
          showModal: true
        },
        path: 'info_general',
        name: 'info_general_s',
        component: () => import('@/components/general_info.vue'),
        props: true
      }
    ]
  },
  {
    path: '/games/',
    name: 'games',
    props: true,
    component: () => import('@/views/Games_menu.vue'),
    children:[
      {
      meta: {
        showModal: true
      },
      path: 'info_g1',
      name: 'info_g1',
      component: () => import('@/components/Games/info_g1.vue'),
      props: true
    },
    {
      meta: {
        showModal: true
      },
      path: 'info_g2',
      name: 'info_g2',
      component: () => import('@/components/Games/info_g2.vue'),
      props: true
    },
    {
      meta: {
        showModal: true
      },
      path: 'faq',
      name: 'faq',
      component: () => import('@/components/faq.vue'),
      props: true
    },
    {
      meta: {
        showModal: true
      },
      path: 'info',
      name: 'info',
      component: () => import('@/components/info.vue'),
      props: true
    },
    {
      meta: {
        showModal: true
      },
      path: 'info_general',
      name: 'info_general',
      component: () => import('@/components/general_info.vue'),
      props: true
    }
    ]
  },
  {
    path: '/games/swipable-cards',
    name: 'game_1',
    component: () => import('@/components/Games/Swipable_cards.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: route,
})

export default router
