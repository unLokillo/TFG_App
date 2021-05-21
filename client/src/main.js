import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faGamepad, faHeart, faAward, faTrophy,faCog, faTimesCircle,faCheckCircle,faQuestionCircle,faBars,faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { makeServer } from "./server";
import { Server, Response } from "miragejs";

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(VueRouter)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
library.add(faGamepad,faHeart,faAward,faTrophy,faCog,faTimesCircle,faCheckCircle,faQuestionCircle,faBars,faTimes)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false
/*
if (window.Cypress) {
  // mirage cypress/test server
  new Server({
    environment: "test",
    routes() {
      let methods = ["get", "put", "patch", "post", "delete"];
      methods.forEach(method => {
        this[method]("/*", async (schema, request) => {
          let [status, headers, body] = await window.handleFromCypress(request);
          return new Response(status, headers, body);
        });
      });
    }
  });
} else {
  // this is the mirage development and production server
  makeServer();
}*/

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')



export default router
