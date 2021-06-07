<template>
    <div class="reject-body">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h2> Rechazar neologismo </h2>
        <p> Por favor, cuéntanos por qué has rechazado este neologismo</p>
        <b-form-textarea v-model="mssg" placeholder="¿Por qué lo has rechazado?" rows="5" max-rows="150" class="reject-info"></b-form-textarea>
        <b-button v-on:click="submit(mssg)" style="background-color: var(--success) !important"> Enviar </b-button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    created(){
        var uri= "http://localhost:3000/neologismes/" + this.$route.params.neoId;
        axios.get(uri)
        .then(response_neo => {
            this.f_user = response_neo.data.user;
        });
         axios.get('http://localhost:3000/login/1')
          .then(response_log => {
              this.login = response_log.data;    
          })
    },
    data(){
        return{
            login: [],
            f_user: [],
            mssg: ''
        }
    },
    methods:{
      submit(n_mssg){
          for (let index = 0; index < this.f_user.length; index++) {
              if(this.login.user_id==this.f_user[index].user_id){
                  this.f_user.splice(index,1,{
                    user_id: this.f_user[index].user_id,
                    user: this.f_user[index].user,
                    date: this.f_user[index].date,
                    rejected:true,
                    mssg:n_mssg
                  }) 
              break;
              }
          }
            axios.patch('http://localhost:3000/neologismes/'+this.$route.params.neoId, {user:this.f_user})
                .then(function( response ){}.bind(this));
        this.$router.go(-1) // -> /user/123
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
