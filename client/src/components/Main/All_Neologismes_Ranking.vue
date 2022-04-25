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
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/neologismes", { withCredentials: true })
      .then((response) => {
        for (let index = 0; index < response.data.length; index++) {
          if (!response.data[index].proposal) {
            this.neologismes.push(response.data[index]);
          }
        }
      });

    axios
      .get("http://127.0.0.1:5000/login", { withCredentials: true })
      .then((response) => {
        this.logged = response.data;
      });
  },
  data() {
    return {
      admin: true,
      neologismes: [],
      logged: [],
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
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.v-ranking-user {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 3rem;
  border: 1px solid var(--border);
  margin: 2%;
}

.position-badge {
  display: flex;
  align-items: center;
  width: 20%;
  height: 100%;
  justify-content: center;
  color: var(--letter-color);
  font-size: 20px;
}
.avatar-card {
  width: 30%;
  display: flex;
  justify-content: inherit;
  align-items: center;
}
</style>