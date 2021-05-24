<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Neologismos Propuestos </h3>
    </div>
     <div class="neo-card" v-for="(value,index) in neologismes" :key="index" >
         <div v-if="index<5">
         <h5>{{ value.neologisme }}</h5>
            <div v-if="value.rejected">
            <font-awesome-icon style="font-size: 20px;color: darkred;" icon="times-circle"/> Rechazada
            </div>
            <div class="neo_card_pendent" v-else>
            <font-awesome-icon style="font-size: 20px;color: darkorange;" icon="question-circle"/> Pendiente 
            </div>
         <b-button class="bttn-app" :to="{name: 'v-neologismes',params: { userid: $route.params.userid ,neoId: value.id}}">+</b-button>
        </div>
     </div>
    <router-link :to="{name: 'view-all-proposals',params: { userid: $route.params.userid }}" class="more-bttn" tag="b-button" >Ver mas</router-link>
    </div>
</template>

<script>
import axios from 'axios'
export default {
      watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },
      created(){
        axios.get('http://localhost:3000/neologismes')
          .then(response => {
            for (let index = 0; index < response.data.length; index++) {
                console.log(response.data[index].proposal);
            if (response.data[index].proposal) {
                this.neologismes.push(response.data[index]);
            }
        }      
            }),
        axios.get('http://localhost:3000/login/1')
          .then(response => {
              this.login = response.data;
          })
    },
    data() {
        return {
            neologismes: [],
            login: []
        }
    },
}
</script>


<style>
.ranking-card{
    margin: 40px 10px 40px 10px;
        background-color: var(--third-color);
    border: 1px solid var(--border);
}
.ranking-title{
    text-align: left;
    padding-left: 20px;
    color: var(--letter-color);
    background-color: var(--buttons);
}

.more-bttn{
    width: 100%;
    background-color: var(--buttons) !important;
}

.neo-card{
    border-bottom: 1px solid var(--border);

}

.neo-card > div{
    padding: 10px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
}

.neo_card_pendent{
    padding-right: 1%;
}
</style>