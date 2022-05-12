<template>
  <div class="body">
    <Header @actualizar="actualizacion()" :key="updateheader" />
    <div class="menu-1">
      <h2>Te damos la bienvenida a <br /></h2>
      <div id="box">
        <p id="flashlight">
          <span id="flash">Pesca</span>
          <span id="light">Neo</span>
        </p>
      </div>
      <h4>
        Una aplicación para proponer, definir y valorar nuevos términos en el
        ámbito de la <strong>descarbonización</strong>. <br>
        Si quieres saber más pulsa 
        <strong>
          <router-link :to="`/info_general`" style="text-decoration:none;color: #3481c0;">aquí</router-link>
        </strong>.
          <br><br>
      </h4>
      <p style="color: var(--fail)" v-if="!login_info.success">
        Necesitas haber iniciado sesión para acceder a esta opción
      </p>
      <b-button v-if="!login_info.success" disabled variant="primary">
        ¡Contribuye!
      </b-button>
      <router-link :to="`/create-neologisme`" tag="b-button" v-else>
        ¡Contribuye!
      </router-link>
    </div>

    <FlashMessage></FlashMessage>

    <h4>Neologismos de la semana</h4>
    <div class="frequent-words">
      <template v-if="this.appear">
        <NeologismoCard
          :neologismeData="neoData[0]"
          v-if="neoData[0]"
        ></NeologismoCard>
        <NeologismoCard
          :neologismeData="neoData[1]"
          v-if="neoData[1]"
        ></NeologismoCard>
        <NeologismoCard
          :neologismeData="neoData[2]"
          v-if="neoData[2]"
        ></NeologismoCard>
      </template>
    </div>
    <h4>Actividades</h4>
    <div class="menu-2">
      <p>
        ¿Te parecen apropiados estos nuevos términos propuestos por otros
        usuarios?
      </p>
      <p style="color: var(--fail)" v-if="!login_info.success">
        Necesitas haber iniciado sesión para acceder a esta opción
      </p>
      <b-button
        disabled
        class="sidebar-button"
        tag="b-button"
        v-if="!login_info.success"
      >
        ¡Participa!
      </b-button>
      <router-link
        :to="{ name: 'games', params: {} }"
        class="sidebar-button"
        tag="b-button"
        v-else
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
    axios
      .get("http://127.0.0.1:5000/week-neologismes", { withCredentials: true })
      .then((response) => {
        for (var i = 0; (i < 3) & (i < response.data.length); i++)
          this.neoData.push(response.data[i]);
        this.appear = true;
      });
    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.login_info = response.data;
      })
      .catch((err) => {});
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
      neoData: [],
      login_info: [],
      varparamostrar: "",
      updateheader: 0,
      appear: null,
    };
  },
  methods: {
    actualizacion() {
      this.updateheader += 1;
      this.login_info.success = false;
    },
  },
};
</script>

<style lang="scss" scoped>
/* box ------------------------------------------------------ */

#box {
  text-align: center;
  font-size: 3em;
  font-weight: bold;
  // -webkit-backface-visibility: hidden; /* fixes flashing */
}

/* flashlight ------------------------------------------------------ */

#flashlight {
  color: hsla(0, 0%, 0%, 0);
  perspective: 80px;
  outline: none;
}

/* flash ------------------------------------------------------ */

#flash {
  display: inline-block;
  text-shadow: #3481c0 0 0 1px, #fff 0 -1px 2px, #fff 0 -3px 2px,
    rgba(0, 0, 0, 0.8) 0 0px 25px;
  transition: margin-left 1s cubic-bezier(0, 1, 0, 1);
}

// #box:hover #flash {
//   text-shadow: #3481c0 0 0 1px, rgba(255, 255, 255, 0.1) 0 1px 3px;
//   margin-left: 20px;
//   transition: margin-left 1s cubic-bezier(0, 0.75, 0, 1);
// }

/* light ------------------------------------------------------ */

#light {
  display: inline-block;
  text-shadow: #1f4d74 0 0 1px, rgba(255, 255, 255, 0.1) 0 1px 3px;
}

// #box:hover #light {
//   text-shadow: #fff 0 0 4px, #3481c0 0 0 20px;
//   transform: rotateY(-60deg);
//   transition: transform 1s cubic-bezier(0, 0.75, 0, 1),
//     text-shadow 0.1s ease-out;
// }

// -------------------------------
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