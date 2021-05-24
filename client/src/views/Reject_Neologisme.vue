<template>
    <div class="reject-body">
              <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h2> Rechazar Neologismo </h2>
        <p> Porfavor escriba a continuación la razón del rechazo</p>
        <b-form-textarea v-model="mssg" placeholder="Introduce la información del rechazo" rows="5" max-rows="150" class="reject-info"></b-form-textarea>
        <b-button v-on:click="submit(1,mssg)" style="background-color: var(--success) !important"> Aceptar </b-button>
    </div>
</template>

<script>

export default {
    data(){
        return{
            mssg: ''
        }
    },
    methods:{
      submit(id,n_mssg){
        var payload = {rejected:true,mssg:n_mssg }; 
            axios.patch('http://localhost:3000/neologismes/1', payload)
                .then(function( response ){
                    // Handle success
                }.bind(this));
        },
}
}
</script>

<style scoped>
h2{
    border-bottom: 1px solid var(--fail);
    padding-bottom: 2%;
}

.reject-body{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 3%;
}

.reject-info{
    width: 100% ;
    min-height: 50%;
    border: 2px solid var(--fail);
}

</style>
