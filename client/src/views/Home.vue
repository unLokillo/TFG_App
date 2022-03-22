<template>
  <div class="body">
    <Header />
    <div class="menu-1">
      <p>
        ¡Os damos la bienvendia a <strong>Pescaneo</strong>! <br />
        Una aplicación para proponer, definir y valorar nuevos términos en el
        ámbito del Internet de las Cosas. <br />
        Si quieres participar, regístrate y pulsa en
        <strong> “¡Contribuye!” </strong>
      </p>
      <p style="color: var(--fail)" v-if="!login_info.logged">
        Necesitas haber iniciado sesión para acceder a esta opción
      </p>
      <b-button v-if="!login_info.logged" disabled variant="primary">
        ¡Contribuye!
      </b-button>
      <router-link :to="`/create-neologisme`" tag="b-button" v-else>
        ¡Contribuye!
      </router-link>
    </div>
    <h4>Neologismos de la semana</h4>
    <div class="frequent-words">
      <!--<NeologismoCard :neologismeData="neoData[0]"></NeologismoCard>
      <NeologismoCard :neologismeData="neoData[1]"></NeologismoCard>
      <NeologismoCard :neologismeData="neoData[2]"></NeologismoCard>-->
    </div>
    <h4>Actividades</h4>
    <div class="menu-2">
      <p>
        ¿Te parecen apropiados estos nuevos términos propuestos por otros
        usuarios?
      </p>
      <router-link
        :to="{ name: 'games', params: {} }"
        class="sidebar-button"
        tag="b-button"
      >
        ¡Participa!
      </router-link>
    </div>
    <h4>Clasificaciones</h4>
    <div class="rankings">
      <ranking_users />
      <ranking_neo />
    </div>
    <div v-if="showModal" class="modal-route">
      <div class="modal-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header/Header.vue";
import NeologismoCard from "@/components/Main/NeologismoCard.vue";
import ranking_users from "@/components/Main/Ranking_users_main.vue";
import ranking_neo from "@/components/Main/Ranking_neo_main.vue";
import axios from "axios";
export default {
  name: "Home",
  components: {
    Header,
    NeologismoCard,
    ranking_users,
    ranking_neo,
  },

  beforeCreate() {
    axios.get("/nothing").then((response) => { // /neologismes
      //this.name = response.data[0].name;
      this.neoData = response.data;
    });
    axios
      .post("http://192.168.1.22:5000/nothing", {
        username: 'R',
        password: 'pass1234',
        email: 'admin@admin.com',
        name: 'R',
        surname: 'MR',
        school: 'ETSIINF',
        points: 0,
        privileges: 'admin'
      })
      .then((response) => {
        //this.name = response.data[0].name;
        console.log(response);
        this.login_info = response.data;
      })
      .catch((err) => {
        console.log("Ha habido un errorsito de na, mira:")
        console.log(err);
      });
  },

  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  data() {
    return {
      showModal: false,
      neoData: "",
      login_info: [],
      varparamostrar: "",
    };
  },
};
</script>

<style lang="scss" scoped>
.body > h4 {
  display: flex;
  margin: 2%;
  border-bottom: 1px solid var(--border);
}

.menu-1 {
  background-color: var(--secondary-color);
  display: flex;
  padding: 4%;
  flex-direction: column;
}

.frequent-words {
  display: flex;
  justify-content: space-around;
}

.menu-2 {
  margin: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  background-color: var(--secondary-color);
}

.menu-2 > p {
  margin-bottom: 2%;
}

.rankings {
  display: flex;
  justify-content: space-evenly;
}
</style>