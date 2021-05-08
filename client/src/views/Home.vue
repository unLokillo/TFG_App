<template>
<div class="body">
  <div class="menu-1">
    <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris augue quam, finibus vitae blandit semper,</p>
    <router-link :to="`/create-neologisme`" tag="b-button"> ¡Contribuye! </router-link>  
  </div>
  <h2>Palabras de la semana</h2>
  <div class="frequent-words">
      <NeologismoCard/>
      <NeologismoCard/>
      <NeologismoCard/>
  </div>
  <div class="menu-2">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris augue quam, finibus vitae blandit semper,
    <b-button> Contribuye </b-button>
  </div>
  <div class="rankings">
    <Ranking/>
    <Ranking/>
  </div>
  <div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header/Header.vue'
import NeologismoCard from '@/components/Main/NeologismoCard.vue'
import Ranking from '@/components/Main/Ranking_Main.vue'
export default {
  name: 'Home',
  components: {
    Header,
    NeologismoCard,
    Ranking
  },
  watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },
  data(){
    return{
      showModal: false,
    }
  }
}
</script>

<style lang="scss" scoped>
.menu-1{
  background-color: rgb(231, 231, 231);
  display: grid;
  padding: 4%;
  grid-template-rows: 1fr 1fr;
}


.frequent-words{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  padding: 10px;
}

.menu-2{
  margin: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  background-color: rgb(231, 231, 231);
}

.rankings{
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba($color: #000000, $alpha: 0.5);
  .modal-content {
    width: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
  }
}
</style>