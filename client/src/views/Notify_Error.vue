<template>
  <div class="reject-body">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h2>Notificar error</h2>
    <p>Por favor, cuéntanos con detalle qué ha pasado.</p>
    <b-form-textarea
      placeholder="Explicanos cuál es el problema (de 10 a 500 caracteres)"
      rows="5"
      v-model="text"
      :state="text.length >= 10 && text.length <= 500"
      class="reject-info"
    ></b-form-textarea>
    <b-button @click="submit">
      Aceptar
    </b-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      text: ""
    };
  },
  methods: {
    submit() {
      var formData = new FormData();
      formData.append("description", this.text)
      axios.post(
          "http://127.0.0.1:5000/error",
          formData,
          { withCredentials: true }
        ).then(res => {
          if(res.status==201){
            this.$router.go(-2);
          }
        })
    }
  }
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
  min-height: 40%;
  border: 2px solid var(--fail);
}
</style>
