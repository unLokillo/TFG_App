<template>
    <div class="card-body">
        <div class="card-neo-header">
            <h2>{{ name }}</h2>
            <div class="neo-likes" ><font-awesome-icon icon="heart"/> {{ likes }}</div> 
        </div>
        <div v-for="(value,index) in descriptions" :key=index >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.content }}</div>
        </div>
        <div class="user-tag">
            <div>Creado por: {{ creator }} </div> 
            <div>{{ date }} </div>
        </div>
        <router-link :to="`/fav-neo/${neo_id}`" tag="b-button" style="width: 100%;"> Ver más </router-link>
       
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
  },data() {    
        return {
            showModal: false,
            neo_id: '987654321',
            name: 'Palabra',
            creator: 'User1 Surname ',
            date: '31/09/1997',
            likes: 10,
            descriptions: [
                {id:0,content:"Definicion 1"},
                {id:1,content:"Esto es un texto de prueba"},
                {id:2,content:"Texto muy muy muy muy muy muy muy muy muy muy muy muy muy largo"},
                {id:3,content:"Pedazo de palabra cruck"}
            ]
        };
    },
}
</script>


<style lang="scss" scoped>
.descriptions{
    padding: 3%;
    padding-left: 10%;
    text-align: left;
}
.card-body{
    background-color: lightblue;
    max-width: 350px;
}
.card-neo-header{
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.user-tag{
    display:flex;
    flex-direction: column;
    padding-bottom: 5%;
    color: grey;
    font-size: 14px; 
}

</style>