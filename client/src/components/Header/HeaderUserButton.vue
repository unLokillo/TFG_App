<template>
  <div class="header-img">
    <router-link
      :to="{ name: 'vUser', params: { userid: login_info.user_id } }"
      class="user-bttn"
      tag="div"
      v-if="login_info.success"
    >
      <!--<b-avatar :src="require(`../../assets/images/${login_info.img}`)"></b-avatar>-->
      {{ login_info.username }}
    </router-link>
    <router-link :to="`/login`" tag="div" v-else> Iniciar sesión </router-link>
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