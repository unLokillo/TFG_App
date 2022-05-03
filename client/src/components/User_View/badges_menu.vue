<template>
  <div class="bages-section">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <div class="top-badges_menu-section">
      <h3 style="display:flex; justify-content: space-between; width:60%">
        <font-awesome-icon style="font-size: 40px; text-align: left;" icon="trophy" />
        Mis logros
        <font-awesome-icon style="font-size: 40px; text-align: right;" icon="trophy" />
      </h3>
      
    </div>
    <div>
      <b-table hover striped :items="badges" :fields="fields"></b-table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "View-User",
  created() {
    axios
      .get("http://127.0.0.1:5000/badges", { withCredentials: true })
      .then((response) => {
        this.badges = response.data;
        // this.badges = new Array(Math.ceil(response.data.length / 4))
        //   .fill()
        //   .map((_) => response.data.splice(0, 4));
      });
  },
  data() {
    return {
      mainProps: { width: 75, height: 75, class: "m1" },
      badges: [],
      labels: ["Usuarios", "Neologismos"],
      fields: [
          {
            key: 'Nombre',
            label: 'Logro',
            sortable: false
          },
          {
            key: 'Acción',
            sortable: false
          },
          {
            key: 'Fecha',
            sortable: true,
          },
          {
            key: 'Puntos',
            label: 'Puntuación',
            sortable: true
          }
        ],
    };
  },
};
</script>

<style>
.top-badges_menu-section {
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  padding: 2%;
  border-bottom: 1px solid var(--border);
  align-items: center;
}

.neologismes-badges {
  display: flex;
}

.neologismes-badges-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid var(--border);
  margin: 2%;
  max-width: 20%;
}

.neologismes-badges_menu > div {
  margin: 3%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.progress-bar-div {
  width: 90%;
}

.bages-section {
  padding: 2%;
}
</style>