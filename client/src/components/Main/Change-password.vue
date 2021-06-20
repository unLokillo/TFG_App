<template>

<div class="f-password-body">
 <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h2>Introduce tu nueva contraseña</h2>
        <p>Introduce el código que has recibido por correo</p>
        <div class="password-box">
        <b-input-group prepend="Contraseña: " class="mt-3" >
            <b-form-input required type="password" id="input-live" aria-describedby="input-live-help input-live-feedback" v-model="form.password" :state="password_state" trim></b-form-input>
          <b-form-invalid-feedback id="input-live-feedback">
              EL tamaño de la contraseña debe de tener entre 6 y 12 caracteres.
          </b-form-invalid-feedback>
        </b-input-group>
        <b-input-group prepend="* Repite la Contraseña: " class="mt-3" >
            <b-form-input required type="password"  v-model="r_password" :state="repeat_password" aria-describedby="r_password_helper" ></b-form-input>
            <b-form-invalid-feedback id="r_password_helper">
              Las contraseñas deben de coincidir.
          </b-form-invalid-feedback>
          </b-input-group>

      </div>
    <b-button variant="outline-success" style="width:70%" v-on:click="submit(form.password)">Modificar</b-button>
</div>
</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
                form: {
                    password: ''
                },
                r_password: ''
            }
        },
        computed: {
      password_state(){
        return this.form.password.length > 6 && this.form.password.length <14
        && this.hasNumeric(this.form.password);
      },
      repeat_password(){
        return this.form.password.localeCompare(this.r_password) ? false:true
      }
    },
    methods:{
         hasNumeric(str){
        var result=false;
        for (let index = 0; !result&& (index <str.length); index++) {
                if (!isNaN(str.charAt(index) * 1)) {
                    result = true;
                }
              }
          return result;   
    },
      submit(value){
            axios.patch('http://localhost:3000/users/'+ this.$route.params.userId, {password:value})
                .then(function( response ){
                    // Handle success
                }.bind(this));
            this.$router.push({ path: `/login` }) 
        },
    }
}
</script>

<style lang="scss" scoped>
.f-password-body{
  padding: 3%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center !important; 
}

.password-box{
    background-color: rgb(231, 231, 231);
    width: 80%;
    margin: 2%;
}

input{
    height: 12%;
    width: 70%;
}

.title-card{
    display: flex;
    justify-content: space-evenly;
}
</style>