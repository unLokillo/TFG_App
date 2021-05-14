<template>
<div class="games-selection">
  <div class="top-menu">
    <h5>Juegos</h5>
    <p>¡¡Bienvenido a la zona de actividades!!</p>
  </div>
  <router-link :to="{ name: 'info_g1',params: {} }" class="game-selector" style="right: 55%;" tag="div">
    game_1
  </router-link >

  <div class="game-selector" style="left: 45%; ">
    game_2
  </div>
<div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
</div>
</template>
<script>
export default {
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

.games-selection{
    background-color: var(--secondary-color);
  display: flex;
  justify-content: space-around;
}
.game-selector{
  cursor: pointer;
  border: 5px solid var(--border);
  width: 30%;
  margin: 0 0 0 10%;
  height: 20rem;
  position: absolute;
  top: 30%;
  border-radius: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.game-selector:hover{
 transform: scale(1.1);
    transition: all .7s ease-in-out;
}
</style>