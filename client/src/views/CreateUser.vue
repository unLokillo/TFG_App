<template>
    <div class="create-user-body">
        <div class="create-user-card">
    <b-form v-if="show">
      <b-form-group id="input-group-1" label="Nombre de Usuario" label-for="input-1">
        <b-form-input id="input-1" v-model="form.user_name" type="text" placeholder="Enter User Name" required></b-form-input>
      </b-form-group>
      
<b-form-group
        id="input-group-2"
        label="Nombre"
        label-for="input-1">
        <b-form-input
          id="input-2"
          v-model="form.name"
          type="text"
          placeholder="Enter Name"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Apellidos" label-for="input-3">
        <b-form-input id="input-3" v-model="form.surname" type="text" placeholder="Enter Last Name" required></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="E-mail" label-for="input-3">
        <b-form-input id="input-3" v-model="form.surname" type="email" placeholder="Enter E-mail" required></b-form-input>
      </b-form-group>

<div class="password-card">
      <b-form-group id="input-group-4" label="Contraseña" label-for="input-4">
        <b-form-input id="input-1" v-model="form.password" type="password" :state="validation" placeholder="Introduce Password" required>
        </b-form-input>
        <b-form-invalid-feedback :state="validation">Your password must be 5-12 characters long.</b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation">Looks Good.</b-form-valid-feedback>
      </b-form-group>

      <b-form-group id="input-group-5" label="Repetir Contraseña" label-for="input-5">
        <b-form-input
          id="input-5"
          :state="v_r_password"
          v-model="form.r_password"
          type="password"
          placeholder="Repite Password"
          required
        ></b-form-input>
         <b-form-invalid-feedback :state="v_r_password">Las contraseñas deben ser iguales</b-form-invalid-feedback>
        <b-form-valid-feedback :state="v_r_password">Looks Good.</b-form-valid-feedback>
      </b-form-group>
    </div>

     <b-form-group
        id="input-group-6"
        label="Fecha"
        label-for="input-6">
        <b-form-input
          id="input-6"
          v-model="form.date"
          type="date"
          placeholder="Repite Password"
          required
        ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-7" label="Genero" label-for="input-7">
        <b-form-select
          id="input-7"
          v-model="form.gender"
          :options="genders"
          required
        ></b-form-select>
    </b-form-group>


    <b-form-group id="input-group-7" label="Lengua Materna" label-for="input-7">
        <b-form-select
          id="input-7"
          v-model="form.gender"
          :options="genders"
          required
        ></b-form-select>
    </b-form-group>
    
     <b-form-file
      v-model="form.image"
      :state="Boolean(form.image)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
      plain
    ></b-form-file>
    <div class="mt-3">Selected file: {{ form.image ? form.image.name : '' }}</div>
    </b-form>


          <b-button class="mt-3" type="submit" variant="primary">Submit</b-button>
    </div>
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

.password-card{
    display: flex;
    justify-content: space-around;
}

.create-user-card{
    background-color: rgb(231, 231, 231);
    margin: 5%;
    padding: 3%;
    box-shadow: 0px 0px 20px 1px black;
}
</style>