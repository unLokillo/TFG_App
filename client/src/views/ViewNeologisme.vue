<template>
    <div class="card-body">
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
         
        <div class="card-neo-header">
            <h2>{{ name }}</h2>
            <div class="neo-likes" ><font-awesome-icon icon="heart"/> {{ likes }}</div> 
        </div>
        
        <div class="rejected-neologisme" v-if="rejected">
            <h4>Su propuesta ha sido rechazada</h4>
            <p>La propuesta del Neologismo: <strong>{{ name }}</strong>, ha sido rechazada por la siguiente razón: <br>
            {{ rejected_reason }}
            <br>
            <strong>Si usted lo desea puede modificar la informacón requerida, y el neologismo sera evaluado nuevamente.
                Gracias por su atencón
            </strong>
        </p>
            <b-button class="bttn-app" style="background-color: var(--fail) !important">Modificar</b-button>
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

        <div class="user-tag" v-if="validated">
            <div>Creado por: {{ creator }} </div> 
            <div>{{ date }} </div>
        </div>
        <div class="admin-options" v-if="adm_flag">
            <b-button class="bttn-app" style="background-color: var(--success) !important"> Aceptar Neologismo </b-button>
            <b-button class="bttn-app" :to="{name: 'r-neologismes',params: { userid: $route.params.userid ,neoId: $route.params.neoId}}"  style="background-color: var(--fail) !important"> Rechazar Neologismo </b-button>
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
            validated: true,
            adm_flag: true,
            showModal: false,
            rejected:true,
            neo_id: '987654321',
            name: 'Palabra',
            creator: 'User1 Surname ',
            date: '31/09/1997',
            likes: 10,
            rejected_reason: 'Mucho texto mi pana',
            descriptions: [
                {id:0,content:"Definicion 1"},
                {id:1,content:"Esto es un texto de prueba"},
                {id:2,content:"Texto muy muy muy muy muy muy muy muy muy muy muy muy muy largo"},
                {id:3,content:"Pedazo de palabra cruck"}
            ],
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
.admin-options{
    display: flex;
    justify-content: space-evenly;

}
.rejected-neologisme{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin-top: 2%;
    border: 2px solid var(--fail);
}

.rejected-neologisme > h4{
    border-bottom: 1px solid var(--border);
    margin: 2%
}
</style>