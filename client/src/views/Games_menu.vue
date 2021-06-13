<template>
<div class="body-games">
  <Header/>
  <div style="background-color: var(--secondary-color); padding: 5%">
    <h3>Actividades</h3>
    ¡Bienvenido a la zona de Actividades!
  </div>
<div class="games-selection">
  <div class="game-selector" style="margin-right:20%">
    <router-link :to="{ name: 'info_g1',params: {} }" tag="div">
      <strong> Cartas deslizantes </strong>
    </router-link >
  </div>
  <div class="game-selector">
    <router-link :to="{ name: 'info_g2',params: {} }" class="game-selector-1" tag="div">
      <strong> El contexto correcto </strong>
    </router-link >
  </div>
  </div>
<div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
<Footer/>
  </div>
</template>
<script>
  import Header from '@/components/Header/Header.vue'
  import Footer from '@/components/Footer/Footer.vue'
export default {
  components: {
    Header,
    Footer
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
        showModal: false
      }
    }
}
</script>

<style lang="scss" scoped>
.body-games{
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
}
.games-selection{
  background-color: var(--main-color);
  display: flex;
  justify-content: center;
  height: 67%;
}

.game-selector{
  width: 25rem;
  height: 50%;
  margin-top: 10%;
  background-color: #a6d3f8;
}

.game-selector > div{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.game-selector:hover{
 transform: scale(1.1);
 transition: all .7s ease-in-out;
  background-color: var(--buttons); 
  color: var(--letter-color);
}

</style>