<template>
<div class="login-body">
  <router-link to='/'>X</router-link>
<div class="login-card">
    <b-form @submit="onSubmit" v-if="show" ok-only>
      <b-form-group
        id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password" label-for="input-2">
        <b-form-input type="password" id="text-password" aria-describedby="password-help-block" :state="validation"></b-form-input>
            <b-form-text id="password-help-block">
                Your password must be 8-20 characters long, contain letters and numbers, and must not
                contain spaces, special characters, or emoji.
            </b-form-text>
      </b-form-group>

      <div class="links">
          <p><a href="/forgot-password" class="blue-text ml-1">Forgot Password?</a></p>
          <p><a href="/create-user" class="blue-text ml-1">Registrer</a></p>
      </div>
    
      <b-button class="mt-3" type="submit" variant="primary">Submit</b-button>
    
    </b-form>
    <!-- DEscomentar para ver mas info sobre el JSON
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    -->
  </div>
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
  justify-content: center !important;
  align-items: center !important;
}

.login-card{
    background-color: rgb(231, 231, 231);
    padding: 3%;
}
.links{
    display:flex;
    justify-content:space-around;
}

</style>