<template>
  <div class="reject-body">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h2>Tell us an error</h2>
    <p>Tell us with detail what happened, please.</p>
    <b-form-textarea
      placeholder="Explain the problem (from 10 to 500 characters)"
      rows="5"
      v-model="text"
      :state="text.length >= 10 && text.length <= 500"
      class="reject-info"
    ></b-form-textarea>
    <b-button @click="submit">
      Submit
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
