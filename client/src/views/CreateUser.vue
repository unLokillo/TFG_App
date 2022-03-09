<template>
  <div class="modify-user-body">
        <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h4>Crear cuenta</h4>
      <b-form @submit="submit">
          <b-input-group prepend="* Alias: " class="mt-3" >
            <b-form-input required v-model="form.nickname" ></b-form-input>
          </b-input-group>

          <b-input-group prepend="* Nombre: " class="mt-3" >
            <b-form-input required v-model="form.name" ></b-form-input>
          </b-input-group>


      <b-input-group prepend="* Apellidos: " class="mt-3" >
            <b-form-input required v-model="form.surname" ></b-form-input>
          </b-input-group>

      <b-input-group prepend="* Correo electrónico: " class="mt-3" >
            <b-form-input required v-model="form.email" type="email" ></b-form-input>            
          </b-input-group>

      <div class="password-box">
        <b-input-group prepend="* Contraseña: " class="mt-3" >
            <b-form-input required type="password" id="input-live" aria-describedby="input-live-help input-live-feedback" v-model="form.password" :state="password_state" trim></b-form-input>
          <b-form-invalid-feedback id="input-live-feedback">
              La contraseña debe de tener entre 6 y 12 caracteres, una mayuscula y un caracter no alfabético.
          </b-form-invalid-feedback>
        </b-input-group>

        <b-input-group prepend="* Repite la Contraseña: " class="mt-3" >
            <b-form-input required type="password"  v-model="r_password" :state="repeat_password" aria-describedby="r_password_helper" ></b-form-input>
            <b-form-invalid-feedback id="r_password_helper">
              Las contraseñas deben coincidir.
          </b-form-invalid-feedback>
          </b-input-group>
      </div>
          <div class="selectors-card">
            <h6>Fecha de Nacimiento</h6>
            <b-form-datepicker v-model="form.date" class="mb-2" :show-decade-nav=true></b-form-datepicker>
          </div>  
          <div class="selectors-card">
            <h6>Género</h6>
            <b-form-select  v-model="form.gender" :options="genders"></b-form-select>
          </div>  
          <div class="selectors-card">
            <h6>Lengua materna</h6>
            <b-form-select class="mt-3"  v-model="form.mother_tonge" :options="mother_tonge"></b-form-select>
          </div>
          <div class="selectors-card">
            <h6>* Escuela UPM</h6>
            <b-form-select class="mt-3"  v-model="form.school" :options="schools" required></b-form-select>
          </div>  
      <div>
<div class="selectors-card">
  <h6>Avatar</h6>
      <b-form-file 
      v-model="form.image"
      accept=".jpg, .png"
      webkitdirectory
      plain
    ></b-form-file>
    <div class="mt-3">Archivo seleccionado: {{ form.image ? form.image.name : '' }}</div>
</div>

    </div>
    <b-button  class="mt-3" type="submit" variant="primary">Enviar</b-button>
    </b-form>
</div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return{
        form: {
          nickname: '',
          name: '',
          surname: '',
          email: '',
          date: '',
          gender: '',
          password: '',
          school: '',
          mother_tonge: '',
          image: undefined,
          points: 0,
          position: 4,
          proposals:[],
          accepted_neo: [],
          fav_neo: [],
          admin: false,
          linguist:false
        },
        genders: [{ text: 'Select One', value: null }, 'Masculino', 'Femenino', 'No binario', 'Prefiero no decirlo'],
        schools: [{ text: 'Select One', value: null }, 'ETSAM','ETSE','ETSIINF', 'ETSII', 'ETSIAE', 'INEF','ETSISI','ETSIST','ETSME'],
        mother_tonge: [{ text: 'Select One', value: null }, 'Español', 'Ingles', 'Portugues','Aleman','Frances', 'Chino'],
        show: true,
        r_password: ''
      }
    },
    computed: {
      password_state(){
        return (this.form.password.length > 6 && this.form.password.length <14) 
        && this.isUpper(this.form.password) && this.hasNumeric(this.form.password);
      },
      repeat_password(){
        return this.form.password.localeCompare(this.r_password) ? false:true
      }
    },
    methods:{
      submit(event){
        event.preventDefault()
        if(this.form.image!=undefined){
         this.form.image = this.form.image.name;
        }else{
         this.form.image = 'default_profile.png';
        }
            axios.post('/users', this.form);
            console.log(axios.get("/users").data)
            console.log("Form: ")
            console.log(JSON.stringify(this.form))
            this.$router.push({ path: `/login` }) 
        },
    isUpper(str) {
      var result=false;
        for (let index = 0; !result&& (index <str.length); index++) {
                var character = str.charAt(index);
                if (character == character.toUpperCase()) {
                    result = true;
                }
              }
          return result;   
    },
    hasNumeric(str){
        var result=false;
        for (let index = 0; !result&& (index <str.length); index++) {
                if (!isNaN(str.charAt(index) * 1)) {
                    result = true;
                }
              }
          return result;   
    }
  }
}
</script>

<style scoped>
.modify-user-body{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3%;
}

.modal-content{
  min-height: 85% ;
}
.modify-user-card{
    background-color: rgb(231, 231, 231);
    padding: 3%;
}

input{
    margin-bottom: 4%;
}
h4{
  margin-bottom: 3%;
  border-bottom: 1px solid var(--border);
}
.selectors-style{
  display: flex;
  justify-content: space-evenly;
  padding-bottom: 3%;
}

.password-box{
  padding: 3%;
  border: 1px solid var(--border);
}

select{
  display: block;
width: 100%;
padding: 0.375rem 0.75rem;
font-size: 1rem;
font-weight: 400;
line-height: 1.5;
color: #212529;
background-color: #fff;
background-clip: padding-box;
border: 1px solid #ced4da;
-webkit-appearance: none;
-moz-appearance: none;
appearance: none;
border-radius: 0.25rem;
transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
background: #fff url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") no-repeat right .75rem center/8px 10px;
}

.selectors-card {
  margin: 2%;
}
</style>