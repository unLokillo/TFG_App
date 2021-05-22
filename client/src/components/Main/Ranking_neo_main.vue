<template>
    <div class="ranking-card">
    <div class="ranking-title"><h3> Top Neologismos </h3></div>
    <b-table class="ranking-table" small :fields="labels" :items="items" responsive="sm" >
        <template #cell(img)="data">
         <b-avatar :src="data.item.img"></b-avatar>   
    </template>
    </b-table>
    <b-button class="more-bttn">Ver mas</b-button>
    </div>
</template>

<script>
    import axios from 'axios';
export default {
    created(){
        axios.get('http://localhost:3000/neologismes')
          .then(response => {
              this.items = response.data;
            })
    },
    data() {
        return {
            labels: [,
            'position',{ key: 'img', label: 'Imagen' },'neologisme', 'liked'],
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
    padding-left: 20px;
    color: black;
    background-color: var(--buttons);
}

.more-bttn{
    width: 100%;
    background-color: var(--buttons);
}

.ranking-table{
    min-width: 500px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    border: 1px solid var(--border);
    min-height: 50px;
}

</style>