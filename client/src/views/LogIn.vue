<template>
<div class="login-body">
   <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h3>Iniciar sesión</h3>
        <b-form-input
          id="input-1"
          v-model="form.email_or_user"
          type="email"
          placeholder="Correo electronico"
          :state="this.correct_login"
          required
        ></b-form-input>
        <b-form-input  
        v-model="form.password" 
        type="password" 
        id="text-password" 
        aria-describedby="password-help-block" 
        placeholder="Contraseña" 
        :state="this.correct_login"></b-form-input>
        
        <b-form-text id="password-help-block"></b-form-text>

        <b-form-invalid-feedback id="input-live-feedback">
          Usuario o contraseña incorrectos
        </b-form-invalid-feedback>

      <div class="links">
          <p><a href="/forgot-password" class="blue-text ml-1">¿Has olvidado la <br> contraseña?</a></p>
          <p><a href="/create-user" class="blue-text ml-1">Registrate</a></p>
      </div>
    
      <b-button v-on:click="getUserInfo" class="mt-3" type="submit" variant="primary">Enviar</b-button>
    
    <!-- DEscomentar para ver mas info sobre el JSON
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    -->
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
          admin: true
        },
        correct_login: null,
        show: true
      }
    },
    methods: {
      getUserInfo(){
        this.correct_login = false;
        var i = 0; 
         axios.get('http://localhost:3000/users')
        .then(response => {
            while (!this.correct_login && (i < response.data.length)) {
              this.correct_login = (response.data[i].nickname.localeCompare(this.form.email_or_user)) &&
                            (response.data[i].password.localeCompare(this.form.password));
              i++;
          
          if(this.correct_login){
            this.form.user_id = response.data[i].id;
            this.form.logged = true;
            this.admin = response.data[i].admin;
          axios.put('http://localhost:3000/login/' + i,this.form)
          .then(response => {      
            });
          this.$router.push({ path: `/`}) // -> /user/123
          };
        }
      });
    },

      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
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