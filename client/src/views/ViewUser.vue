<template>
  <div class="v-user-body">
    <Header />
    <div class="top-menu">
      <div class="left-menu-card">
        <!--<b-img :src="require(`../assets/images/${img}`)" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img> -->
        <div class="ls-menu">
          <div class="left-side-menus">
            <router-link
              :to="{
                name: 'vu-ranking',
                params: { userid: $route.params.userid },
              }"
            >
            <div>
              <font-awesome-icon style="font-size: 80px" icon="trophy" /> <br />
              <br />
              <strong>Posición: {{ position }}</strong> <br />
              <strong>Puntuación: {{ points }}</strong>
            </div>
            </router-link>
          </div>

          <div class="left-side-menus">
            <router-link
              :to="{
                name: 'vu-badges',
                params: { userid: $route.params.userid },
              }"
            >
            <div>
              <font-awesome-icon style="font-size: 20px" icon="award" />
              Mis logros ({{nbadges}})
            </div>
            </router-link>
          </div>

          <div class="left-side-menus">
            <router-link
              :to="{ name: 'f-neo', params: { userid: $route.params.userid } }"
            >
            <div>
              <font-awesome-icon
                style="font-size: 20px; color: red"
                icon="heart"
              />
              Neologismos favoritos ({{ fav_neo }})
            </div>
            </router-link>
          </div>
        </div>
      </div>

      <div class="main-info-card">
        <div class="info-card">
          <strong> Nombre y Apellidos: </strong> {{ this.name }}
          {{ this.surname }}
        </div>
        <div class="info-card">
          <strong> Fecha Nacimiento: </strong> {{ this.date }}
        </div>
        <div class="info-card">
          <strong> Correo Electrónico: </strong> {{ this.email }}
        </div>
        <div class="info-card">
          <strong> Género: </strong> {{ this.gender }}
        </div>
        <div class="info-card">
          <strong> Escuela UPM: </strong> {{ this.school }}
        </div>
      </div>

      <div class="options">
        <b-dropdown right text="Opciones" class="m-2">
          <b-dropdown-item
            :to="{ name: 'm-perfil', params: { userid: $route.params.userid } }"
            >Modificar perfil</b-dropdown-item
          >
          <b-dropdown-divider></b-dropdown-divider>
          <!-- <b-dropdown-item>Cambiar idioma</b-dropdown-item>
          <b-dropdown-divider></b-dropdown-divider> -->
          <b-dropdown-item
            :to="{ name: 'n-error', params: { userid: $route.params.userid } }"
            >Notificar error</b-dropdown-item
          >
          <b-dropdown-divider
           v-if="this.privileges=='admin' || this.privileges=='linguist'"
          ></b-dropdown-divider>
          <b-dropdown-text v-if="this.privileges=='admin' || this.privileges=='linguist'" style="font-style: italic; font-weight: 300">
            Descargar CSV de:
          </b-dropdown-text>
          <b-dropdown-item v-if="this.privileges=='admin' || this.privileges=='linguist'">
            <download-csv :data="proposed" name="Proposed.csv">
              - Propuestas de neologismos
            </download-csv>
          </b-dropdown-item>
          <b-dropdown-item v-if="this.privileges=='admin' || this.privileges=='linguist'">
            <download-csv :data="accepted" name="Accepted.csv">
              - Neologismos aceptados
            </download-csv>
          </b-dropdown-item>
          <b-dropdown-item v-if="this.privileges=='admin' || this.privileges=='linguist'">
            <download-csv :data="neologismes" name="All_neologismes.csv">
              - Todos los neologismos
            </download-csv>
          </b-dropdown-item><b-dropdown-item v-if="this.privileges=='admin' || this.privileges=='linguist'">
            <download-csv style="color: darkred" :data="errores" name="error_notifications.csv">
              - Errores notificados
            </download-csv>
          </b-dropdown-item>
          <b-dropdown-divider
           v-if="this.privileges=='admin' || this.privileges=='linguist'"
          ></b-dropdown-divider>
          <b-dropdown-item v-on:click="logout">
            <div style="color: red !important">
              Cerrar sesión
            </div></b-dropdown-item
          ><b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item v-on:click="deleteData($route.params.userid)">
            <div style="color: darkred !important">
              Eliminar cuenta
            </div></b-dropdown-item
          >
        </b-dropdown>
      </div>
    </div>

    <div class="bottom-menu">
      <h4>Neologismos propuestos y aceptados</h4>
      <div class="user-rankings">
        <Non_Accepeted_Neos />
        <Accepeted_Neos />
      </div>
    </div>

    <div v-if="showModal" class="modal-route">
      <div class="modal-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Accepeted_Neos from "@/components/User_View/Accepted-Neo-Menu.vue";
import Non_Accepeted_Neos from "@/components/User_View/Proposed-Neo-Menu.vue";
import Header from "@/components/Header/Header.vue";
import axios from "axios";
export default {
  name: "View-User",
  components: {
    Accepeted_Neos,
    Non_Accepeted_Neos,
    Header,
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/users/0", { withCredentials: true }) // + this.$route.params.userid)
      .then((response) => {
        this.name = response.data.name;
        this.surname = response.data.surname;
        this.email = response.data.email;
        this.date = response.data.date;
        this.gender = response.data.gender;
        this.school = response.data.school;
        this.points = response.data.points;
        this.position = response.data.position;
        this.img = response.data.image;
        this.privileges = response.data.privileges;
        this.lingu = response.data.lingu;
      });
    axios
      .get("http://127.0.0.1:5000/badges", { withCredentials: true }) // + this.$route.params.userid)
      .then((response) => {
        this.nbadges = response.data.length;
      });
    axios
      .get(
        "http://127.0.0.1:5000/users/" + this.$route.params.userid + "/favs",
        { withCredentials: true }
      ) // + this.$route.params.userid)
      .then((response) => {
        this.fav_neo = response.data.length;
      });
    axios.get('http://127.0.0.1:5000/neologismes', { withCredentials: true })
        .then(response => {
            this.neologismes = response.data;
            for(let i = 0; i<this.neologismes.length; i++){
              if(this.neologismes[i].state == 'aceptado')
                this.accepted.push(this.neologismes[i]);
              else if(this.neologismes[i].state == 'pendiente')
                this.proposed.push(this.neologismes[i]);
            }
        });
    axios.get('http://127.0.0.1:5000/error', { withCredentials: true })
      .then(res => {
        this.errores = res.data;
      })
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
      liked_neo: 0,
      showModal: false,
      mainProps: { width: "200%", height: "200%", class: "m1" },
      name: "",
      surname: "",
      fav_neo: [],
      email: "",
      date: "",
      gender: "",
      school: "",
      img: "",
      points: 0,
      position: 0,
      admin: false,
      lingu: false,
      neologismes: [],
      nbadges: 0,
      privileges: "",
      accepted: [],
      proposed: [],
      errores: []
    };
  },
  methods: {
    deleteData(id) {
      axios.delete("http://127.0.0.1:5000/users/" + id, {
        withCredentials: true,
      });
      axios.get("http://127.0.0.1:5000/logout", { withCredentials: true });
      this.$router.push("/");
    },
    logout(){
      axios.get('http://127.0.0.1:5000/logout', { withCredentials: true })
      .then(res => {
        if(res.status==204){
          this.$router.push({ path: `/`})
        }
      })
    }
  },
};
</script>

<style lang="scss" scoped>
.top-menu {
  display: grid;
  grid-template-columns: 2fr 5fr 1fr;
  margin: 3%;
}
.bottom-menu > h4 {
  display: flex;
  margin: 2%;
  border-bottom: 1px solid var(--border);
}
.left-menu-card {
  padding: 4%;
  border-right: 2px solid var(--border);
}

.ls-menu {
  border: 2px solid var(--border);
  background-color: var(--second-color);
  margin: 8% 0 0 0;
}

.left-side-menus {
  padding: 2%;
  background-color: var(--third-color);
}

.left-side-menus:hover {
  color: #3481c0;
  cursor: pointer;
}

.main-info-card {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  margin: 5%;
  background-color: var(--third-color);
}

.info-card {
  border-left: 10px solid var(--border-left);
  padding-left: 2%;
  margin-bottom: 2%;
  margin-top: 2%;
  text-align: left;
}
.user-rankings {
  border-top: 0px;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr 1fr;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba($color: #000000, $alpha: 0.6);
}
.modal-content {
  width: 70%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  overflow: scroll;
}
.options-bttn > button {
  padding: 10% !important;
}
</style>
