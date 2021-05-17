<template>
<div class="games-selection">
  <div class="top-menu">
    <h5>Juegos</h5>
    <p>¡¡Bienvenido a la zona de actividades!!</p>
  </div>
<div>
  <router-link :to="{ name: 'info_g1',params: {} }" class="game-selector" style="right: 55%;" tag="div">
    <strong> Juego 1 </strong>
  </router-link >
  <div class="game-selector" style="left: 45%; ">
    <strong> Juego 2 </strong>
  </div>
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

.top-menu{
  margin: 2%;
  background-color: var(--secondary-color);
width: 100%;
height: 15%;
padding:1%;

}

.games-selection{
    background-color: var(--main-color);
  display: flex;
  justify-content: space-around;
  height: 38rem;
}
.game-selector{
  cursor: pointer;
  border: 5px solid var(--buttons);
  width: 30%;
  margin: 0 0 0 10%;
  height: 20rem;
  position: absolute;
  top: 35%;
  border-radius: 10px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.game-selector:hover{
 transform: scale(1.1);
 transition: all .7s ease-in-out;
  background-color: var(--buttons); 
  color: var(--letter-color);
}
</style>