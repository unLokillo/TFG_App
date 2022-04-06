<template>
  <div class="f-password-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h2>¿Has olvidado la contraseña?</h2>
    <p>Introduce tu email para poder restablecer tu contraseña.</p>
    <b-form-input
      id="input-1"
      v-model="email"
      type="email"
      placeholder="Introduce tu correo electrónico"
      :state="this.correct_email"
      required
    >
    </b-form-input>

    <b-form-invalid-feedback
      id="input-live-feedback"
      v-if="!this.correct_email"
    >
      No existe una cuenta asociada a ese email
    </b-form-invalid-feedback>
    <b-button
      style="width: 70%"
      v-on:click="submit"
      type="submit"
      v-if="this.correct_email"
      >Confirmar</b-button
    >
    <b-button style="width: 70%" v-on:click="submit" type="submit" v-else
      >Reintentar</b-button
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      correct_email: true,
    };
  },
  methods: {
    submit() {
      axios
        .post(
          "http://127.0.0.1:5000/reset_password",
          {
            email: this.email,
          },
          { withCredentials: true }
        )
        .then((response) => {
          if (response.status == 200) {
            this.$router.push(`/login`);
          } else {
            this.correct_email = false;
          }
        });
      for (let index = 0; index < this.form.length; index++) {
        if (this.form[index].email.localeCompare(this.email) == 0) {
          this.correct_email = true;
          this.$router.push({
            name: `forgot-password-cp`,
            params: { userId: this.form[index].id },
          });
          break;
        }
      }
      if (this.correct_email == null) {
        this.correct_email = false;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.f-password-body {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center !important;
}

.f-password-card {
  background-color: rgb(231, 231, 231);
  width: 100%;
  margin: 2%;
}

input {
  height: 12%;
  width: 70%;
}

.title-card {
  display: flex;
  justify-content: space-evenly;
}
</style>