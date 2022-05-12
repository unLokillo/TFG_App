<template>
  <div class="all-neologismes-card">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <div class="top-all-neologismes">
      <h5>Tus neologismos propuestos</h5>
    </div>

    <div class="neologisme-cards">
      <div v-for="(value, index) in neologismes" :key="index">
        {{ index + 1 }}
        <!--<b-avatar :src="require(`../../assets/images/${value.img}`)"></b-avatar>-->
        <h5>{{ value.neologisme }}</h5>
        
        <div class="neo_card_pendent" v-if="value.state=='pendiente'">
          <font-awesome-icon
            style="font-size: 20px; color: darkorange"
            icon="question-circle"
          />
          Pendiente
        </div>
        <div class="neo_card_pendent" v-else-if="value.state=='aceptado'">
          <font-awesome-icon
            style="font-size: 20px; color: green"
            icon="circle-check"
          />
          Aceptado
        </div>
        <div v-else>
          <font-awesome-icon
            style="font-size: 20px; color: darkred"
            icon="times-circle"
          />
          Rechazado
        </div>
        <b-button
          class="bttn-app"
          :to="{
            name: 'v-neologismes',
            params: { userid: $route.params.userid, neoId: value.id },
          }"
        >
          +</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  async created() {
    axios.get("http://127.0.0.1:5000/login", { withCredentials: true })
    .then((response_l) => {
      this.login = response_l.data;
    });
    await axios
      .get("http://127.0.0.1:5000/user-neo", { withCredentials: true })
      .then((response) => {
        this.neologismes = response.data.allneos;
      });
  },
  data() {
    return {
      neologismes: [],
      login: [],
      form_user: [],
    };
  }
};
</script>

<style>
.top-all-neologismes {
  margin: 30px;
  border-bottom: 1px solid var(--border);
  color: black;
}

.all-neologismes-card {
  height: 100%;
  max-height: 700px;
  overflow: scroll;
}

.neologisme-cards > div {
  border-left: 16px solid var(--border-left) !important;
  padding: 10px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border: 1px solid var(--border);
  margin: 5%;
}
</style>