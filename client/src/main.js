import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faInfoCircle,faSignOutAlt,faGamepad, faPlusCircle, faHeart, faAward,faBookOpen, faTrophy,faCog, faTimesCircle,faCheckCircle,faQuestionCircle,faBars,faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import JsonCSV from 'vue-json-csv'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(VueRouter)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
library.add(faInfoCircle,faSignOutAlt,faPlusCircle,faGamepad,faBookOpen,faHeart,faAward,faTrophy,faCog,faTimesCircle,faCheckCircle,faQuestionCircle,faBars,faTimes)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false

Vue.component('downloadCsv', JsonCSV)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')



export default router
