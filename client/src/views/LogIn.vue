<template>
  <div class="login-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h3>Log in</h3>
    <b-form-input
      v-model="form.email_or_user"
      placeholder="Email"
      :state="this.correct_login"
      required
      v-on:keypress.enter="getUserInfo"
    ></b-form-input>
    <b-form-input
      v-model="form.password"
      type="password"
      placeholder="Password"
      :state="this.correct_login"
      v-on:keypress.enter="getUserInfo"
    ></b-form-input>

    <b-form-text id="password-help-block"></b-form-text>

    <b-form-invalid-feedback id="input-live-feedback">
      Incorrect user or password
    </b-form-invalid-feedback>

    <div class="links">
      <p>
        <a href="/forgot-password" class="blue-text ml-1"
          >Forgot the password?</a
        >
      </p>
      <p><a href="/create-user" class="blue-text ml-1">Sign in</a></p>
    </div>
    <FlashMessage :position="'left top'"></FlashMessage>
    <b-button
      v-on:click="getUserInfo"
      class="mt-3"
      type="submit"
      variant="primary"
      >Submit</b-button
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  beforeCreate() {
    axios
      .get("http://127.0.0.1:5000/login", { credentials: "include" })
      .then((res) => {
        if (res.status == 200) {
          this.$router.push({ path: `/` });
        }
      })
      .catch((err) => {});
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
      axios
        .post(
          "http://127.0.0.1:5000/login",
          {
            username: this.form.email_or_user,
            password: this.form.password,
          },
          { withCredentials: true }
        )
        .then((response) => {
          if (response.status === 200) {
            var formData = new FormData();
            formData.append("achiev", "login");
            axios.post("http://127.0.0.1:5000/badges", formData, { withCredentials: true })
            .then(res => {
              if(res.status==201){
                this.flashMessage.setStrategy('multiple');
                this.flashMessage.show({
                  status: "success",
                  title: "You have earned a new badge!",
                  message: "Go to your badges section to check it out",
                  time: 5000,
                  position: 'left top'
                });
              }
            })
            this.correct_login = true;
            this.$router.push({ path: `/` });
            //var login = this.getlogin();
            
            this.flashMessage.show({
              status: "success",
              title: "You are now logged in!",
              message: "We are happy to have you back :)",
              time: 5000,
              position: 'left top',
              //html: '<h3>ey</h3>'
            });
          }
        });
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