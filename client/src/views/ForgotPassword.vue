<template>

<div class="f-password-body">
    <header> <router-link to="/"> X </router-link> </header>
        <h3>Forgot Password</h3>
        <p>Introduce el código que has recibido por correo</p>
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required>
          </b-form-input>
    <button type="submit" class="btn btn-dark btn-lg btn-block">Reset password</button>
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

<style lang="scss" scoped>
.f-password-body{
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center !important; 
}

.f-password-card{
    background-color: rgb(231, 231, 231);
    width: 100%;
    margin: 2%;
}

input{
    width: 70%;
}

.title-card{
    display: flex;
    justify-content: space-evenly;
}
</style>