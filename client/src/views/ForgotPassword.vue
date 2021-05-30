<template>

<div class="f-password-body">
 <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h2>¿Has olvidado la contraseña?</h2>
        <p>Introduce el código que has recibido por correo</p>
        <b-form-input
          id="input-1"
          v-model="form.code"
          type="email"
          placeholder="Introduce el código"
          required>
          </b-form-input>
    <b-button style="width:70%" v-on:click="submit" type="submit" >Confirmar</b-button>
</div>
</template>

<script>
    export default {
        data() {
            return {
                form: {
                    code: "",
                }
            }
        },
        methods: {
            submit() {
                console.log(this.form.code.localeCompare("ASDFG")); 
                if(this.form.code.localeCompare("ASDFG")==0){
                    this.$router.push({ path: `/forgot-password/reset` }) // -> /user/123
                }
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
    height: 12%;
    width: 70%;
}

.title-card{
    display: flex;
    justify-content: space-evenly;
}
</style>