<template>
    <div class="card-body">
      <div class="close-modal"><router-link to="/"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <div class="card-neo-header">
            <h2>{{ name }}</h2>
            <div class="neo-likes" ><font-awesome-icon icon="heart"/> {{ likes }}</div> 
        </div>
        <div class="descriptions-card">
            <h4>Descripciones</h4>
        <div v-for="(value,index) in descriptions" :key=index >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.content }}</div>
        </div>
        </div>
        <div class="descriptions-card">
            <h4>Fuentes</h4>
        <div v-for="(value,index) in descriptions" :key=index >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.content }}</div>
        </div>
        </div>

        <div class="image-card">
            <b-img thumbnail src="https://picsum.photos/1024/400/?image=41" fluid-grow alt="Responsive image"></b-img>
        </div>

        <div class="user-tag">
            <div>Creado por: {{ creator }} </div> 
            <div>{{ date }} </div>
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
.card-body{
  display: flex;
  flex-direction: column;
  overflow: scroll;
  align-content: center;
}
.descriptions{
    margin-bottom: 2%;

    padding: 1%;
    text-align: left;
    border-left: 10px solid var(--border-left);
}
.card-neo-header{
    display:flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
}
.user-tag{
    display:flex;
    flex-direction: column;
    padding-bottom: 5%;
    color: grey;
    font-size: 14px; 
}
.descriptions-card{
    border-bottom: 1px solid var(--border);
}

h4{
    text-align: left;
    margin-top: 1%;
}

.img-thumbnail{
    margin: 2% 0 2% 0;
    background-color:var(--border-left) ;
}
</style>