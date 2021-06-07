<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Neologismos Aceptados </h3>
    </div>
     <div class="neo-card" v-for="(value,index) in neologismes" :key="index" >
         <div v-if="index<5">
        <b-avatar :src="value.img"></b-avatar>
         <h5>{{ value.neologisme }}</h5>
            <div>
            <font-awesome-icon icon="heart"/> {{ value.liked }}
            </div>
         <b-button class="bttn-app" :to="{name: 'v-neologisme',params: { userid: $route.params.userid ,neoId: value.id}}">+</b-button>
        </div>
     </div>
    <router-link :to="{name: 'view-all-neologismes',params: { userid: $route.params.userid }}" class="more-bttn" tag="b-button" >Ver mas</router-link>
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
            if (!response.data[index].proposal && !response.data[index].modify) {
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


<style lang="scss" scoped>
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
    background-color: var(--buttons);
}

.neo-card > div{
    padding: 10px;    
    display: flex;
    justify-content: center;
    align-items: center;
    justify-content: space-evenly;
}

</style>