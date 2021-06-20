<template>
<div class="login-body">
   <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h3>Iniciar sesión</h3>
        <b-form-input v-model="form.email_or_user" placeholder="Correo electronico" :state="this.correct_login" required></b-form-input>
        <b-form-input v-model="form.password" type="password" placeholder="Contraseña" :state="this.correct_login"></b-form-input>
        
        <b-form-text id="password-help-block"></b-form-text>

        <b-form-invalid-feedback id="input-live-feedback">
          Usuario o contraseña incorrectos
        </b-form-invalid-feedback>

      <div class="links">
          <p><a href="/forgot-password" class="blue-text ml-1">¿Has olvidado la <br> contraseña?</a></p>
          <p><a href="/create-user" class="blue-text ml-1">Registrate</a></p>
      </div>
    
      <b-button v-on:click="getUserInfo" class="mt-3" type="submit" variant="primary">Enviar</b-button>

  </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return{
        form: {
          email_or_user: '', //variable que indica el nombre de usuario o el email 
          password: '',
          logged: false,
          user_id: 0,
          admin: false,
          linguist: false,
          img: ''
        },
        correct_login: null,
        show: true
      }
    },
    methods: {
      getUserInfo(){
        this.correct_login = false;
        var i = -1; 
         axios.get('http://localhost:3000/users')
        .then(response => {
            while (!this.correct_login && (i < response.data.length)) {
              i++;
              this.correct_login = (response.data[i].email.localeCompare(this.form.email_or_user)==0|| 
              (response.data[i].nickname.localeCompare(this.form.email_or_user)==0)) &&
                            (response.data[i].password.localeCompare(this.form.password)==0);

          if(this.correct_login){
            this.form.user_id = response.data[i].id;
            this.form.logged = true;
            this.form.admin = response.data[i].admin;
            this.form.linguist = response.data[i].linguist;
            this.form.user_id = response.data[i].id;
            this.form.img = response.data[i].image;
            console.log(response.data[i].image);
          axios.put('http://localhost:3000/login/1',this.form)
          .then(response => {      
            });
          this.$router.push({ path: `/register`}) 
          this.$router.push({ path: `/`}) 
          };
        }
      });
    },
    }

}
</script>

<style lang="scss" scoped>
.login-body{
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center !important; 
}

.login-card{
    background-color: rgb(231, 231, 231);
    padding: 3%;
}
.links{
  width: 100%;
    display:flex;
    justify-content:space-around;
}

input{
    width: 70%;
    height: 8%;
}

.modal-content{
  height: 65%;
}

button {
  border-radius: 0 px !important;
  width: 70%;
  height: 4rem;

}
</style>