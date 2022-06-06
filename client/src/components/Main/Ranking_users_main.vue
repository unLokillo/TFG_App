<template>
  <div class="ranking-card">
    <div class="ranking-title">
      <h3>Users ranking</h3>
    </div>
    <b-table
      class="ranking-table"
      small
      :fields="labels"
      :items="items"
      responsive="sm"
    >
      <template #cell(image)="data">
        <b-avatar
          :src="require(`@/assets/images/` + data.item.image)"
        ></b-avatar>
      </template>
    </b-table>
    <router-link
      class="more-bttn"
      :to="{ name: 'ranking', params: { userid: $route.params.userid } }"
      tag="b-button"
    >
      See more</router-link
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/users/ranking-five", { withCredentials: true })
      .then((response) => {
        for (
          let index = 0;
          index < 5 && index < response.data.length;
          index++
        ) {
          if (response.data[index].privileges!='admin') {
            this.items.push(response.data[index]);
          }
        }
      });
  },

  data() {
    return {
      labels: [
        { key: "position", label: "Posición" },
        //{ key: "image", label: "Imagen" },
        { key: "nickname", label: "Participante" },
        { key: "points", label: "Puntuación" },
      ],
      items: [],
    };
  },
};
</script>


<style>
.ranking-card {
  margin: 40px 10px 40px 10px;
}
.ranking-title {
  text-align: left;
  padding: 2%;
  padding-left: 20px;
  color: black;
  background-color: var(--buttons);
}

.more-bttn {
  width: 100%;
  background-color: var(--buttons) !important;
}

.ranking-table {
  min-width: 500px;
}
</style>