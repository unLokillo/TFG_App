<template v-if='this.appear'>
  <div class="ranking-card">
    <div class="ranking-title"><h3>Neologismos destacados</h3></div>
    <b-table
      class="ranking-table"
      small
      :fields="labels"
      :items="items"
      responsive="sm"
    >
      <!--<template #cell(img)="data">
         <b-avatar :src="require(`@/assets/images/`+data.item.img)"></b-avatar>   
    </template>-->
    </b-table>
    <router-link
      class="more-bttn"
      :to="{ name: 'ranking_neo', params: { userid: $route.params.userid } }"
      tag="b-button"
    >
      Ver más</router-link
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/neologismes", { withCredentials: true })
      .then((response) => {
        var i = 0;
        while ((i < 5) & (i < response.data.length)) {
          if(response.data[i].state=='aceptado')
          this.items.push(response.data[i]);
          i++;
        }
      });
    this.appear = true;
  },
  data() {
    return {
      labels: [
        { key: "position", label: "Posición" },
        { key: "neologismo", label: "Neologismo" },
        { key: "user", label: "Usuario" },
        { key: "liked", label: "Puntuación" },
      ],
      items: [],
      appear: null,
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
  padding-left: 20px;
  color: rgb(255, 255, 255);
  background-color: var(--buttons);
}

.more-bttn {
  width: 100%;
  background-color: var(--buttons);
}

.ranking-table {
  min-width: 500px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border: 1px solid var(--border);
  min-height: 50px;
}
</style>