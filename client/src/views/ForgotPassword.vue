<template>
<div class="f-password-body">
    <div class="f-password-card">
        <b-form @submit="onSubmit" ok-only>
        <h3>Forgot Password</h3>
            <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
            description="We'll never share your email with anyone else.">

        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required>
          </b-form-input>
      </b-form-group>
    <button type="submit" class="btn btn-dark btn-lg btn-block">Reset password</button>
   </b-form>
   </div>
</div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    email: '',
                }
            }
        },
        methods: {
            onSubmit(event) {
            event.preventDefault()
            alert(JSON.stringify(this.form))
      },
    }
}
</script>

<style >
.f-password-body{
  display: flex;
  justify-content: center !important;
  align-items: center !important;
}

.f-password-card{
    background-color: rgb(231, 231, 231);
    width: 100%;
    margin: 2%;
}
</style>