<template>
  <div>
    <div v-b-toggle.sidebar-no-header class="hamburguer-button">
      <font-awesome-icon icon="bars" />Menu
    </div>
    <b-sidebar
      id="sidebar-no-header"
      aria-labelledby="sidebar-no-header-title"
      no-header
      shadow
    >
      <template #default="{ hide }">
        <div>
          <div class="sidemenu-top">
            <h4 id="sidebar-no-header-title">Menú</h4>
            <div style="cursor: pointer" block @click="hide">
              <font-awesome-icon style="font-size: 200%" icon="bars" />
            </div>
          </div>

          <div class="all-sidebar-buttons" v-if="screen">
            <router-link
              :to="{ name: 'games', params: {} }"
              class="sidebar-button"
              tag="div"
            >
              <div>
                <font-awesome-icon
                  style="font-size: 120%; !important"
                  icon="gamepad"
                />
              </div>
              Actividades
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'ranking', params: {} }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="trophy"
              />
              Ranking Usuarios
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'ranking_neo', params: { userid: form.user_id } }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="trophy"
              />
              Ranking Neologismos
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'main-view-all-proposals', params: {} }"
              class="sidebar-button"
              tag="div"
              v-if="form.success"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="book-open"
              />
              Tus propuestas
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'badges', params: {} }"
              class="sidebar-button"
              tag="div"
              v-if="form.success"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="award"
              />
              Logros
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'info_general' }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="info-circle"
              />
              Información
              <div></div>
            </router-link>

            <div
              class="sidebar-button"
              style="border-left: 10px solid red !important"
              v-on:click="logOut"
              v-if="form.success"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="sign-out-alt"
              />
              Salir
              <div></div>
            </div>
          </div>

          <div class="all-sidebar-buttons" v-else>
            <router-link
              :to="{ name: 'games', params: {} }"
              class="sidebar-button"
              tag="div"
            >
              <div>
                <font-awesome-icon
                  style="font-size: 120%; !important"
                  icon="gamepad"
                />
              </div>
              Actividades
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'vu-ranking', params: { userid: form.user_id } }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="trophy"
              />
              Ranking Usuarios
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'vu-ranking_neo', params: { userid: form.user_id } }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="trophy"
              />
              Ranking Neologismos
              <div></div>
            </router-link>

            <router-link
              :to="{
                name: 'view-all-proposals',
                params: { userid: form.user_id },
              }"
              class="sidebar-button"
              tag="div"
              v-if="form.logged"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="book-open"
              />
              Tus Propuestas
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'vu-badges', params: { userid: form.user_id } }"
              class="sidebar-button"
              tag="div"
              v-if="form.success"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="award"
              />
              Logros
              <div></div>
            </router-link>

            <router-link
              :to="{ name: 'info_general_s' }"
              class="sidebar-button"
              tag="div"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="info-circle"
              />
              Información
              <div></div>
            </router-link>

            <div
              class="sidebar-button"
              style="border-left: 10px solid red !important"
              v-on:click="logOut"
              v-if="form.success"
            >
              <font-awesome-icon
                style="font-size: 120%; !important"
                icon="sign-out-alt"
              />
              Salir
              <div></div>
            </div>
          </div>
        </div>
      </template>
    </b-sidebar>
  </div>
</template>

<script>
import axios from "axios";
export default {
  emits: ["actualiza"],
  created() {
    this.screen =
      this.$router.currentRoute.path.localeCompare("/") == 0 ? true : false;
    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.form = response.data;
      })
      .catch((err) => {});
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.form = response.data;
      })
      .catch((err) => {});
  },
  updated() {
    this.screen =
      this.$router.currentRoute.path.localeCompare("/") == 0 ? true : false;
  },
  data() {
    return {
      myToggle: false,
      form: [],
      screen: false,
    };
  },
  computed: {
    btnStates() {
      return this.buttons.map((btn) => btn.state);
    },
  },
  methods: {
    logOut() {
      axios
        .get("http://127.0.0.1:5000/logout", { withCredentials: true })
        .then((response_l) => {
          console.log("Reloading...");
          this.$emit("actualiza");
        })
        .catch((err) => {});
    },
  },
};
</script>

<style>
.option-button {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: left;
}

.hamburguer-button {
  height: 100%;
  display: flex;
  max-width: 150px;
  justify-content: space-evenly;
  align-items: center;
  border-right: 1px solid var(--border);
}

.all-sidebar-buttons {
  display: flex;
  flex-direction: column;
}

.sidebar-button {
  padding: 8%;
  display: flex;
  font-size: 130%;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid var(--border);
  border-left: 10px solid var(--border-left);
  cursor: pointer;
  justify-content: space-between;
}

.sidemenu-top {
  border-bottom: 1px solid var(--border);
  padding: 3% 0 3% 0;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: space-around;
}
</style>