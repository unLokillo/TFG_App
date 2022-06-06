<template>
  <div class="f-password-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h2>Have you forgotten your password?</h2>
    <p>Submit your email for setting a new one.</p>
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
      There is no account associated with that email
    </b-form-invalid-feedback>
    <b-button
      style="width: 70%"
      v-on:click="submit"
      type="submit"
      v-if="this.correct_email"
      >Confirm</b-button
    >
    <b-button style="width: 70%" v-on:click="submit" type="submit" v-else
      >Retry</b-button
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
            this.flashMessage.show({
              status: "warning",
              title: "Password recovery",
              message: "A link for setting a new password has been sent to you via email. USE IT IN THE NEXT 10 MINUTES.",
              time: 8000,
              position: 'left top',
              //html: '<h3>ey</h3>'
            });
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