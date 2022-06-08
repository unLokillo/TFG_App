<template>
  <div class="card-body">
    <div class="card-neo-header">
      <h2 class="titulito">{{ this.neologismeData.name_eng }}</h2>
      <div class="neo-likes">
        <font-awesome-icon icon="heart" /> {{ this.neologismeData.liked }}
      </div>
    </div>
    <div
      v-for="(value, index) in this.neologismeData.descriptions"
      :key="index"
    >
      <div v-if="index < 3" class="descriptions">
        {{ index + 1 }}.- {{ value[0] }}
      </div>
    </div>
    <div class="user-tag">
      <div>Created by {{ this.neologismeData.user }}</div>
      <div>{{ this.neologismeData.date }}</div>
    </div>
    <router-link
      :to="`/fav-neo/${this.neologismeData.id}`"
      tag="b-button"
      style="width: 100%"
      v-if="login"
    >
      See more
    </router-link>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    neologismeData: Object,
    required: true,
  },
  watch: {
    /*$route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }*/
  },
  created() {
    axios.get("http://127.0.0.1:5000/login", { withCredentials: true })
    .catch((err) => {
      console.log(err)
      this.login=false
    });
  },
  data() {
    return {
      showModal: false,
      neo_id: "",
      name: "",
      creator: "",
      date: "",
      likes: "",
      descriptions: "",
      login: true
    };
  },
};
</script>


<style lang="scss" scoped>
.descriptions {
  padding: 3%;
  padding-left: 10%;
  text-align: left;
}
.card-body {
  background-color: var(--third-color);
  max-width: 350px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border-width: 3px;
  border-radius: 10px;
  border: solid #3481c0;
}
.card-neo-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.user-tag {
  display: flex;
  flex-direction: column;
  padding-bottom: 5%;
  color: grey;
  font-size: 14px;
}
.titulito {
  padding: 3%;
  padding-left: 10%;
}
.neo-likes {
  padding-right: 5%;
}
</style>