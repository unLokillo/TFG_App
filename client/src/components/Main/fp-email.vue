<template>

<div class="f-password-body">
 <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h2>¿Has olvidado la contraseña?</h2>
        <p>Introduce tu email, para que podamos mandarte el código de verificación.</p>
        <b-form-input
          id="input-1"
          v-model="email"
          type="email"
          placeholder="Introduce tu correo electrónico"
          :state="this.correct_email"
          required>
          </b-form-input>

        <b-form-invalid-feedback id="input-live-feedback">
            El email introducido no es valido.
        </b-form-invalid-feedback>
    <b-button style="width:70%" v-on:click="submit" type="submit" >Confirmar</b-button>
</div>
</template>

<script>
import axios from 'axios';
    export default {
        created(){ 
         axios.get('http://localhost:3000/users') .then(response => {
             this.form = response.data;
         })
        },
        data() {
            return {
                email: "",
                form:[],
                correct_email:null
            }
        },
        methods: {
            submit() {
                for (let index = 0; index < this.form.length; index++) {
                    if(this.form[index].email.localeCompare(this.email)==0){
                        this.correct_email = true;
                        this.$router.push({ name: `forgot-password-cp`,params:{userId: this.form[index].id}});
                        break;
                    }
                }
                if(this.correct_email==null){
                    this.correct_email = false;
                }
      },
    }
}
</script>

<style lang="scss" scoped>
.f-password-body{
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center !important; 
}

.f-password-card{
    background-color: rgb(231, 231, 231);
    width: 100%;
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