<template>
  <div class="all-neologismes-card">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <div class="top-all-neologismes">
      <h5>Neologismos favoritos</h5>
    </div>

    <div class="neologisme-cards">
      <div v-for="(value, index) in neologismes" :key="index">
        <!--<b-avatar :src="value.img"></b-avatar>-->
        <h5>{{ value.name }}</h5>
        De: {{ value.user }}
        <div><font-awesome-icon icon="heart" /> {{ value.likes }}</div>
        <b-button
          class="bttn-app"
          :to="{
            name: 'fv-neologismes',
            params: { userid: $route.params.userid, neoId: value.id },
          }"
        >
          + info</b-button
        >
        <font-awesome-icon
            style="font-size: 20px; color: darkred"
            icon="times-circle"
            v-if="value.state.includes('rechazado')"
          />
        <font-awesome-icon
            style="font-size: 20px; color: darkorange"
            icon="question-circle"
            v-else-if="value.state == 'pendiente'"
          />
        <font-awesome-icon
            style="font-size: 20px; color: lightgreen"
            icon="circle-check"
            v-else-if="value.state == 'aceptado'"
          />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios.get('http://127.0.0.1:5000/users/' + this.$route.params.userid + '/favs', { withCredentials: true })
    .then(res => {
      this.neologismes = res.data;
    });
    
    /*axios.get("http://localhost:3000/login/1").then((response_log) => {
      this.login = response_log.data;
      axios
        .get("http://localhost:3000/users/" + this.$route.params.userid)
        .then((response_users) => {
          axios
            .get("http://localhost:3000/neologismes")
            .then((response_neo) => {
              for (
                let index = 0;
                index < response_users.data.fav_neo.length;
                index++
              ) {
                this.neologismes.push(
                  response_neo.data[response_users.data.fav_neo[index] - 1]
                );
              }
            });
        });
    });*/
  },
  data() {
    return {
      neologismes: [],
      login: [],
    };
  },
  methods: {
    submit(id, type, n_mssg) {
      var payload = {};
      switch (type) {
        case "accepted":
          payload = { proposal: false };
          break;
        case "reject":
          payload = { rejected: true, mssg: n_mssg };
          break;
      }
      axios.patch("http://localhost:3000/neologismes/" + id, payload);
    },
  },
};
</script>

<style>
.top-all-neologismes {
  border-bottom: 1px solid var(--border);
  margin: 2%;
}

.all-neologismes-card {
  height: 100%;
  max-height: 700px;
  overflow: scroll;
}

.neologisme-cards > div {
  border-left: 14px solid var(--border-left) !important;
  padding: 10px;
  display: flex;
  justify-content: space-evenly;
  border: 1px solid var(--border);
  margin: 5%;
  align-items: center;
}
</style>