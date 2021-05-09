<template>
    <div class="create-user-body">
        <div class="close-modal"><router-link to="/"> X </router-link></div>
        <b-form-input id="input-1" v-model="form.user_name" type="text" placeholder="Enter User Name" required></b-form-input>

        <b-form-input v-model="form.name" type="text" placeholder="Enter Name" required></b-form-input>

        <b-form-input v-model="form.surname" type="text" placeholder="Enter Last Name" required></b-form-input>

        <b-form-input v-model="form.surname" type="email" placeholder="Enter E-mail" required></b-form-input>
      <b-form-group>
        <b-form-input  v-model="form.password" type="password" :state="validation" placeholder="Introduce Password" required></b-form-input>
        <b-form-invalid-feedback :state="validation">Your password must be 5-12 characters long.</b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation">Looks Good.</b-form-valid-feedback>
      </b-form-group>
      <b-form-group>
        <b-form-input :state="v_r_password" v-model="form.r_password" type="password" placeholder="Repite Password" required></b-form-input>
        <b-form-invalid-feedback :state="v_r_password">Las contraseñas deben ser iguales</b-form-invalid-feedback>
        <b-form-valid-feedback :state="v_r_password">Looks Good.</b-form-valid-feedback>
      </b-form-group>  
        <b-form-input v-model="form.date" type="date" placeholder="Repite Password" required></b-form-input>
        <div>
        <b-form-select v-model="form.gender" :options="genders" required></b-form-select>

        <b-form-select v-model="form.gender" :options="genders" required></b-form-select>
      </div>
     <b-form-file v-model="form.image" :state="Boolean(form.image)" placeholder="Choose a file or drop it here..." drop-placeholder="Drop file here..." plain></b-form-file>
    <div class="mt-3">Selected file: {{ form.image ? form.image.name : '' }}</div>  
          <b-button class="mt-3" type="submit" variant="primary">Submit</b-button>
</div>
</template>
crear
<script>
export default {
    data() {
        return{
        form: {
          user_name: '',
          name: '',
          surname: '',
          email: '',
          date: '',
          password: '',
          r_password: '',
          mother_tonge: '',
          gender: '',
          image: null,
        },
        genders: [{ text: 'Select One', value: null }, 'male', 'female', 'non binary', 'undefined'],
        show: true
      }
    },
    computed: {
      validation() {
        return this.form.password.length > 4 && this.form.password.length < 13
      },
      v_r_password() {
          return this.form.password == this.form.r_password
      }
    }
}
</script>
<style>
.create-user-body{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3%;
}

.modal-content{
  min-height: 85% ;
}
.create-user-card{
    background-color: rgb(231, 231, 231);
    padding: 3%;
}

input{
    width: 70% !important;
    margin-bottom: 4%;
}
</style>