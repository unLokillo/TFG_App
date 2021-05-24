<template>
    <div class="all-neologismes-card">
         <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="top-all-neologismes">
            <h5> Propuestas de Neologismo </h5>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index" >
                <h5>{{ value.neologismo }}</h5>
            <div v-if="value.rejected">
            <font-awesome-icon style="font-size: 20px;color: darkred;" icon="times-circle"/> Rechazada
            </div>

            <div class="neo_card_pendent" v-else>
            <font-awesome-icon style="font-size: 20px;color: darkorange;" icon="question-circle"/> Pendiente 
            </div>
             <b-dropdown text="Acciones" v-if="login.admin">
                    <b-dropdown-item v-on:click="submit(value.id,'accepted','')">Aceptar Propuesta</b-dropdown-item>
                    <b-dropdown-item >Rechazar Propuesta</b-dropdown-item>
                    <b-dropdown-item style="color: red;" href="#">Eliminar Propuesta</b-dropdown-item>
                </b-dropdown>
                 <b-button class="bttn-app" :to="{name: 'v-neologismes',params: { userid: $route.params.userid ,neoId: value.id}}"> +</b-button>
            </div>
        </div>

    </div>
</template>

<script>
    import axios from 'axios';
export default {
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
 
        //console.log(this.neologismes);
        //console.log(non_proposals);
    },
    data() {
        return {
            neologismes: [],
            login: []
        }
    },
    methods:{
      submit(id,type,n_mssg){
        var payload = {}; 
          switch (type){
            case 'accepted': payload = {proposal:false}; break;
            case 'reject': payload = {rejected:true,mssg:n_mssg }; break;
          }
            axios.patch('http://localhost:3000/neologismes/' + id, payload)
                .then(function( response ){
                    // Handle success
                }.bind(this));
        },
}
}
</script>

<style>
.top-all-neologismes{
    margin: 30px;
    border-bottom: 1px solid var(--border)  ;
    color: black;
}

.all-neologismes-card{
    height: 100%;
    max-height: 500px;
    overflow: scroll;
}

.neologisme-cards > div{
    padding: 10px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    border: 1px solid var(--border);
    margin: 5%;
}

</style>