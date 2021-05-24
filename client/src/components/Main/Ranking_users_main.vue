<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Ranking </h3>
    </div>
     <b-table class="ranking-table" small :fields="labels" :items="items" responsive="sm" >
        <template #cell(img)="data">
         <b-avatar :src="data.item.img"></b-avatar>   
    </template>
    </b-table>
    <router-link class="more-bttn" :to="{name: 'ranking',params: { userid: $route.params.userid }}" tag="b-button"> 
    Ver mas</router-link>
    </div>
</template>

<script>
import axios from 'axios';
export default {
        created(){
        axios.get('http://localhost:3000/users')
          .then(response => {
            for (let index = 0; index < response.data.length; index++) {
            if (!response.data[index].admin) {
                this.items.push(response.data[index]);
            }
            }
          })
    },

    data() {
        return {
            labels: [,
            'position',{ key: 'img', label: 'Imagen' },'nickname', 'points'],
            items: []
        }
    },
}
</script>


<style>
.ranking-card{
    margin: 40px 10px 40px 10px;
}
.ranking-title{
    text-align: left;
    padding: 2%;
    padding-left: 20px;
    color: black;
    background-color: var(--buttons);
}

.more-bttn{
    width: 100%;
    background-color: var(--buttons) !important;
}

.ranking-table{
    min-width: 500px;
}
</style>