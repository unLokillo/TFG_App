<template>
  <div class="ranking-card">
    <div class="ranking-title">
      <h3>Ranking</h3>
    </div>
    <div class="neo-card" v-for="(value, index) in items" :key="index">
      <div v-if="index < 5">
        <h5>{{ value.neologismo }}</h5>
        <div v-if="value.accepeted">
          <font-awesome-icon
            style="font-size: 20px; color: darkred"
            icon="times-circle"
          />
          Rechazada
        </div>

        <div class="neo_card_pendent" v-else>
          <font-awesome-icon
            style="font-size: 20px; color: darkorange"
            icon="question-circle"
          />
          Pendiente
        </div>
        <b-button>+</b-button>
      </div>
    </div>
    <b-button class="more-bttn">Ver mas</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { neologismo: "Neologismo 1", accepeted: true },
        { neologismo: "Neologismo 2", accepeted: false },
        { neologismo: "Neologismo 3", accepeted: false },
        { neologismo: "Neologismo 4", accepeted: true },
        { neologismo: "Neologismo 5", accepeted: true },
        { neologismo: "Neologismo 6", accepeted: true },
      ],
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
  color: black;
  background-color: lightblue;
}

.more-bttn {
  width: 100%;
  background-color: lightblue !important;
}

.neo-card > div {
  padding: 10px;
  display: flex;
  justify-content: space-evenly;
}

.neo_card_pendent {
  padding-right: 1%;
}
</style>