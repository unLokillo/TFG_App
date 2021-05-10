<template>
<div class="login-body">
   <div class="close-modal"><router-link to="/"> X </router-link></div>
        <h3>Log In</h3>
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Introuduce tu email"
          required
        ></b-form-input>

        <b-form-input type="password" id="text-password" aria-describedby="password-help-block" placeholder="Introuduce tu contraseña" :state="validation"></b-form-input>
            <b-form-text id="password-help-block"></b-form-text>

      <div class="links">
          <p><a href="/forgot-password" class="blue-text ml-1">Forgot Password?</a></p>
          <p><a href="/create-user" class="blue-text ml-1">Registrer</a></p>
      </div>
    
      <b-button class="mt-3" type="submit" variant="primary">Submit</b-button>
    
    <!-- DEscomentar para ver mas info sobre el JSON
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    -->
  </div>
</template>

<script>
export default {
    data() {
        return{
        form: {
          email: '',
          name: '',
        },
        show: true
      }
    },
    methods: {
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
    height: 12%;
}

.modal-content{
  height: 65%;
}

button {
  border-radius: 0 px !important;
  width: 70%;
}
</style>