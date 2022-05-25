<template v-if='this.appear'>
  <div class="ranking-card">
    <div class="ranking-title">
      <h3>Neologismos Aceptados</h3>
    </div>
    <div class="neo-card" v-for="(value, index) in neologismes" :key="index">
      <div v-if="index < 5">
        <!--<b-avatar :src="require(`../../assets/images/${value.img}`)"></b-avatar>-->
        <h5>{{ value.neologisme }}</h5>
        <div><font-awesome-icon icon="heart" /> {{ value.liked }}</div>
        <b-button
          class="bttn-app"
          :to="{
            name: 'v-neologisme',
            params: { userid: $route.params.userid, neoId: value.id },
          }"
          >+ info</b-button
        >
      </div>
    </div>
    <!--<router-link
      :to="{
        name: 'view-all-neologismes',
        params: { userid: $route.params.userid },
      }"
      ><b-button class="more-bttn">Ver más</b-button></router-link
    >-->
  </div>
</template>

<script>
import axios from "axios";
export default {
  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/users/0/neologismes", { withCredentials: true })
      .then((response) => {
        this.neologismes = response.data.accepted;
        this.appear = true;
      });
  },
  data() {
    return {
      neologismes: [],
      login: [],
      appear: null,
    };
  },
};
</script>


<style lang="scss" scoped>
.ranking-card {
  margin: 40px 10px 40px 10px;
  background-color: var(--third-color);

}
.ranking-title {
  text-align: left;
  padding-left: 20px;
  color: var(--letter-color);
  background-color: var(--buttons);
}

.more-bttn {
  width: 100%;
  background-color: var(--buttons);
}

.neo-card > div {
  padding: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: space-evenly;
}
</style>