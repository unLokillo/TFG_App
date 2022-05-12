<template>
  <div class="header-img">
    <b-button
      :to="{ name: 'vUser', params: { userid: login_info.user_id } }"
      class="header-img"
      style="text-decoration: none; height: 100%; border-width:0px"
      v-if="login_info.success"
    >
      <!--<b-avatar :src="require(`../../assets/images/${login_info.img}`)"></b-avatar>-->
      <font-awesome-icon
                style="font-size: 120%; !important; color: white; padding-right:10%; padding-bottom:4%"
                icon="user"
              />
      <strong style="color: white; justify-content: center"><h5> {{login_info.username}} </h5></strong>
      <!-- <font-awesome-icon
                style="font-size: 120%; !important; color: black; padding-left:10%; padding-right:10%; transform: rotate(90deg);"
                icon="play"
              /> -->
    </b-button>
    <router-link :to="`/login`" class="header-img" v-else style="text-decoration: none; border-width:0px"
      ><div style="color: white">Iniciar sesión</div></router-link
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.login_info = response.data;
      })
      .catch((err) => {});
  },
  data() {
    return {
      filename: "Under_construction.png",
      user_info: false,
      showModal: false,
      user_id: "",
      login_info: [],
    };
  },
  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.header-img {
  padding: 5%;
  border-left: solid 1px var(--border);
  background-color: var(--buttons);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  cursor: pointer;
}
.header-img:hover {
  transition: all 0.4s ease-in-out;
  background-color: var(--buttons_hover);
}
</style>