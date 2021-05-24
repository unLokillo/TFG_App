<template>
<div class="body">
  <div class="menu-1">
    <p> ¡Buenos días! Bienvenido a <strong>Neologismos</strong> un proyecto de la Unviersidad Politecncia de Madrid que tiene con fin registrar nuevos nelogismos relaccionadsos con el mundos de las IT. ¿Te apetecería contribuir?</p>
    <router-link :to="`/create-neologisme`" tag="b-button"> ¡Contribuye! </router-link>  
  </div>
  <h4>Palabras de la semana</h4>
  <div class="frequent-words">
      <NeologismoCard :neologismeData="neoData[0]"></NeologismoCard>
      <NeologismoCard :neologismeData="neoData[1]"></NeologismoCard>
      <NeologismoCard :neologismeData="neoData[2]"></NeologismoCard>
  </div>
   <h4>Juegos</h4>
  <div class="menu-2">
    <p> ¡Aquí podras encontrar algunos juegos y actividades! </p>
     <router-link :to="{ name: 'games',params: {} }" class="sidebar-button" tag="b-button"> ¡Juega! </router-link>
  </div>
  <h4>Rankings</h4>
  <div class="rankings">
    <ranking_users/>
    <ranking_neo/>
  </div>
  <div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header/Header.vue'
import NeologismoCard from '@/components/Main/NeologismoCard.vue'
import ranking_users from '@/components/Main/Ranking_users_main.vue'
import ranking_neo from '@/components/Main/Ranking_neo_main.vue'
import axios from 'axios'
export default {
  name: 'Home',
  components: {
    Header,
    NeologismoCard,
    ranking_users,
    ranking_neo
  },
  
  beforeCreate(){
        axios.get('http://localhost:3000/neologismes')
        .then(response => {
            //this.name = response.data[0].name;
            this.neoData = response.data;
        })
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
      neoData: '',
    }
  }
}
</script>

<style lang="scss" scoped>

.body > h4{
  display: flex;
  margin: 2%;
  border-bottom: 1px solid var(--border);
}

.menu-1{
  background-color: var(--secondary-color);
  display: flex;
  padding: 4%;
  flex-direction: column;
}


.frequent-words{
  display: flex;
  justify-content: space-around;
}

.menu-2{
  margin: 20px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  background-color: var(--secondary-color);
}

.menu-2 > p{
  margin-bottom: 2%;
}

.rankings{
  display: flex;
  justify-content: space-evenly;
}

</style>