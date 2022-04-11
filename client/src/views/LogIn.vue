<template>
  <div class="login-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h3>Iniciar sesión</h3>
    <b-form-input
      v-model="form.email_or_user"
      placeholder="Correo electronico"
      :state="this.correct_login"
      required
    ></b-form-input>
    <b-form-input
      v-model="form.password"
      type="password"
      placeholder="Contraseña"
      :state="this.correct_login"
    ></b-form-input>

    <b-form-text id="password-help-block"></b-form-text>

    <b-form-invalid-feedback id="input-live-feedback">
      Usuario o contraseña incorrectos
    </b-form-invalid-feedback>

    <div class="links">
      <p>
        <a href="/forgot-password" class="blue-text ml-1"
          >¿Has olvidado la <br />
          contraseña?</a
        >
      </p>
      <p><a href="/create-user" class="blue-text ml-1">Regístrate</a></p>
    </div>

    <b-button
      v-on:click="getUserInfo"
      class="mt-3"
      type="submit"
      variant="primary"
      >Enviar</b-button
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  beforeCreate(){
    axios.get('http://127.0.0.1:5000/login', {credentials: 'include'})
    .then(res => {
      if(res.status==200){
        this.$router.push({ path: `/` });
      }
    }).catch((err) => {})
  },
  data() {
    return {
      form: {
        email_or_user: "", //variable que indica el nombre de usuario o el email
        password: "",
        logged: false,
        user_id: 0,
        admin: false,
        linguist: false,
        img: "",
      },
      correct_login: null,
      show: true,
    };
  },
  methods: {
    getUserInfo() {
      this.correct_login = false;
      axios.post("http://127.0.0.1:5000/login",
      {
        username: this.form.email_or_user,
        password: this.form.password
      }, { withCredentials: true }).then((response) => {
        if (response.status === 200) {
          this.correct_login = true
          this.$router.push({ path: `/` });
        }
      })
    },
  },
};
</script>

<style lang="scss" scoped>
.login-body {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center !important;
}

.login-card {
  background-color: rgb(231, 231, 231);
  padding: 3%;
}
.links {
  width: 100%;
  display: flex;
  justify-content: space-around;
}

input {
  width: 70%;
  height: 8%;
}

.modal-content {
  height: 65%;
}

button {
  border-radius: 0 px !important;
  width: 70%;
  height: 4rem;
}
</style>