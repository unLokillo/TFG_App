<template>
  <div class="v-ranking-card">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <div class="v-ranking-title">
      <h3>Ranking Neologismos</h3>
    </div>
    <div v-if="logged.privileges == 'admin' || logged.privileges == 'linguist'">
    <b-button
        class="bttn-app"
        @click="toggle_proposals = !toggle_proposals"
        v-if="!toggle_proposals"
        style="margin-bottom: 1rem"
      >
        Revisar propuestas
    </b-button>
    <b-button
        class="bttn-app"
        @click="toggle_proposals = !toggle_proposals"
        v-else
        style="margin-bottom: 1rem"
      >
        Ver todos los neologismos
    </b-button>
    </div>
    <div v-if="!toggle_proposals">
    <div
      class="v-ranking-user"
      v-for="(value, index) in neologismes"
      :key="index"
    >
      <div class="position-badge" :style="asign_color(value.position)">
        <strong> {{ value.position }} </strong>
      </div>
      <div class="avatar-card">
        <!--<b-avatar :src="require(`../../assets/images/${value.img}`)"></b-avatar>-->
        {{ value.neologismo }}
      </div>
      <div class="author">
        <font-awesome-icon style="font-size: 15px; margin-right: 7px" icon="fa-user" />
        {{value.user}}
      </div>
      <div class="v-ranking-points">
        <font-awesome-icon style="font-size: 15px; margin-right: 7px" icon="heart" />
        {{ value.liked }}
      </div>
      <router-link
        :to="`/fav-neo/${value.id}`"
        tag="b-button"
        style="margin-right: 2rem"
      >
        + info
      </router-link>
    </div>
  </div>
  <div v-else>
    <div
      class="v-ranking-user"
      v-for="(value, index) in proposals"
      :key="index"
    >
      <div class="position-badge" :style="asign_color(4)">
        <font-awesome-icon
            style="font-size: 20px; color: darkorange"
            icon="question-circle"
          />
      </div>
      <div class="avatar-card">
        <!--<b-avatar :src="require(`../../assets/images/${value.img}`)"></b-avatar>-->
        {{ value.neologismo }}
      </div>
      <div class="author">
        <font-awesome-icon style="font-size: 15px; margin-right: 7px" icon="fa-user" />
        {{value.user}}
      </div>
      <div class="v-ranking-points">
        <font-awesome-icon style="font-size: 15px; margin-right: 7px" icon="heart" />
        {{ value.liked }}
      </div>
      <router-link
        :to="`/fav-neo/${value.id}`"
        tag="b-button"
        style="margin-right: 2rem"
      >
        + info
      </router-link>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.logged = response.data;
      });
    axios
      .get("http://127.0.0.1:5000/neologismes", { withCredentials: true })
      .then((response) => {
        if(this.logged.privileges == 'admin' || this.logged.privileges == 'linguist')
          for (let index = 0; index < response.data.length; index++) {
            this.neologismes.push(response.data[index]);
            if(response.data[index].state == 'pendiente'){
              this.proposals.push(response.data[index]);
            }
          }
        else {
          var pos = 1
          for (let index = 0; index < response.data.length; index++) {
            if(response.data[index].state=='aceptado'){
              response.data[index].position = pos;
              pos++;
              this.neologismes.push(response.data[index]);
            }
          }
        }
      });

  },
  data() {
    return {
      admin: true,
      neologismes: [],
      logged: [],
      proposals: [],
      toggle_proposals: false
    };
  },
  methods: {
    asign_color: function (pos) {
      var style = {};
      switch (pos) {
        default:
          style.backgroundColor = "var(--buttons)";
          break;
        case 1:
          style.backgroundColor = "var(--gold) ";
          break;
        case 3:
          style.backgroundColor = "var(--bronze)";
          break;
        case 2:
          style.backgroundColor = "var(--silver)";
          break;
      }
      return style;
    },
  },
};
</script>

<style>
.v-ranking-title {
  border-bottom: 1px solid var(--border);
  margin: 2%;
}

.v-ranking-points {
  /* background-color: aqua; */
  text-align: left;
  /* display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  padding-left: 70%; */
}

/* .author {
  background-color: blue; 
  display: flex;
  justify-content: space-between;
  text-align: left;
  padding-left: 0%; 
} */

.v-ranking-user {
  display: grid;
  grid-template-columns: 10% 33% 30% 10% 15%;
  gap: 0.5rem;
  grid-auto-flow: column;
  margin: 0 0.5rem 1rem 0.5rem;
  /* display: flex; */
  /* justify-content: space-between; */
  align-items: center;
  height: 3rem;
  border: 1px solid var(--border);
  /* margin: 2%; */
}

.position-badge {
  display: flex;
  align-items: center;
  width: 4rem;
  height: 100%;
  justify-content: center;
  color: var(--letter-color);
  font-size: 20px;
}
.avatar-card {
  /* width: 20%; */
  /* display: flex;
  justify-content: inherit;
  align-items: center;
  position: fixed; */
  /* text-align: left; */
  font-weight: bold;
}
</style>