<template>
  <div class="reject-body">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h2>Rechazar neologismo</h2>
    <p>Por favor, cuéntanos por qué rechazas este neologismo</p>
    <b-form-textarea
      v-model="mssg"
      placeholder="¿Por qué no es adecuado?"
      rows="5"
      max-rows="150"
      class="reject-info"
    ></b-form-textarea>
    <b-button
      v-on:click="submit(mssg)"
      style="background-color: var(--success) !important"
    >
      Enviar
    </b-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    /*var uri = "http://localhost:3000/neologismes/" + this.$route.params.neoId;
    axios.get(uri).then((response_neo) => {
      this.f_user = response_neo.data.user;
    });
    axios.get("http://localhost:3000/login/1").then((response_log) => {
      this.login = response_log.data;
    });*/
  },
  data() {
    return {
      login: [],
      f_user: [],
      mssg: "",
    };
  },
  methods: {
    submit(n_mssg) {
      var formData = new FormData();
      formData.append('do', 'reject');
      formData.append('message', n_mssg);
      axios.put("http://127.0.0.1:5000/neologismes/" +
        this.$route.params.neoId,
        formData,
        { withCredentials: true }
        ).then( res => {
          if(res.status==201)
            this.$router.go(-1)
          else console.log("El servidor ha devuelto una respuesta inesperada: ", res.status)
        });

      /*this.f_user.splice(0, 1, {
        user_id: this.f_user[0].user_id,
        user: this.f_user[0].user,
        date: this.f_user[0].date,
        rejected: true,
        mssg: n_mssg,
      });
      axios.patch(
        "http://localhost:3000/neologismes/" + this.$route.params.neoId,
        { user: this.f_user }
      );
      this.$router.go(-2); // -> /user/123*/
    },
  },
};
</script>

<style scoped>
h2 {
  border-bottom: 1px solid var(--fail);
  padding-bottom: 2%;
}

.reject-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3%;
}

.reject-info {
  width: 100%;
  min-height: 50%;
  border: 2px solid var(--fail);
}
</style>
