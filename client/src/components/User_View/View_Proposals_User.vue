<template>
    <div class="all-neologismes-card">
         <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="top-all-neologismes">
            <h5> Neologismos propuestos </h5>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index" >
                {{ index+1 }}
                <b-avatar :src="require(`../../assets/images/${value.img}`)"></b-avatar>
                <h5>{{ value.neologisme }}</h5>
            
            <div v-if="value.user[0].rejected">
                <font-awesome-icon style="font-size: 20px;color: darkred;" icon="times-circle"/> Rechazado
            </div>
            <div class="neo_card_pendent" v-else>
                <font-awesome-icon style="font-size: 20px;color: darkorange;" icon="question-circle"/> Pendiente 
            </div>
             <b-dropdown text="Acciones" v-if="login.linguist || login.admin">
                    <b-dropdown-item v-on:click="submit(value.id,'accepted','')">Aceptar propuesta</b-dropdown-item>
                    <b-dropdown-item :to="{name: 'rp-neologismes',params: { userid: $route.params.userid ,neoId: value.id}}">Rechazar propuesta</b-dropdown-item>
                    <b-dropdown-item v-if="login.admin" style="color: red; !important" v-on:click="deleteData(value.id)">Eliminar propuesta</b-dropdown-item>
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
        axios.get('http://localhost:3000/login/1')
          .then(response_l => {
              this.login = response_l.data;
          
        axios.get('http://localhost:3000/users/' + response_l.data.user_id)
          .then(response_u => { 

        axios.get('http://localhost:3000/neologismes')
          .then(response => {
            if(response_l.data.admin || response_l.data.linguist){
                     for (let index = 0; index < response.data.length; index++) {
                         if (response.data[index].proposal) {
                        this.neologismes.push(response.data[index]);
                    }
                }
            }else{
                for (let index = 0; index < response.data.length; index++) {
                    console.log(response_u.data.proposals.includes(response.data[index].id));
                    if (response_u.data.proposals.includes(response.data[index].id)) {
                        this.neologismes.push(response.data[index]);
                    }
                }
            }
        })   
          })
        })
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
    deleteData(id) {
    axios.delete('http://localhost:3000/neologismes/' + id)
        .then(response => {
      console.log(this.result);
    });
    }
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
    max-height: 700px;
    overflow: scroll;
}

.neologisme-cards > div{
    border-left: 16px solid var(--border-left) !important;
    padding: 10px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    border: 1px solid var(--border);
    margin: 5%;
}

</style>