<template>
    <div class="ranking-card">
    <div class="ranking-title">
    <h3> Ranking </h3>
    </div>
     <b-table small :fields="labels" :items="items" responsive="sm">
        <!--<template #cell(img)="data">
         <b-avatar :src="data.item.img"></b-avatar>   
    </template>-->
    </b-table>
    <b-button class="more-bttn">Ver mas</b-button>
    </div>
</template>

<script>
export default {
    created(){
        axios.get("http://127.0.0.1:5000/week-neologismes", { withCredentials: true }).then(response => {
              var i = 0;
              while(i < 5 && i < response.data.length){
                  if(!response.data[i].proposal){
                    this.items.push(response.data[i]);
                  }
                   i++;
              }
            })
    },
    data() {
        return {
           labels: [,
            { key: 'position', label: 'Posición' },
            { key: 'neologismo', label: 'Neologismo' },
            { key: 'user', label: 'Usuario' }, 
            { key: 'liked', label: 'Puntuación' }],
            items: []
        }
    }
}
</script>


<style>
.ranking-card{
    margin: 40px 10px 40px 10px;
}
.ranking-title{
    text-align: left;
    padding-left: 20px;
    color: black;
    background-color: lightblue;
}

.more-bttn{
    width: 100%;
    background-color: lightblue !important;
}
</style>