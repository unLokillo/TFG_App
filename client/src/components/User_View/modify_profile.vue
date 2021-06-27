<template>
  <div class="modify-user-body">
          <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h4>Modificar Información de usuario</h4>

          <b-input-group prepend="Alias: " class="mt-3" >
            <b-form-input  v-model="form.nickname" :value="form.nickname" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('nickname',form.nickname)" >Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

          <b-input-group prepend="Nombre: " class="mt-3" >
            <b-form-input v-model="form.name" :value="form.name" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('name',form.name)">  Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <b-input-group prepend="Apellidos: " class="mt-3" >
            <b-form-input v-model="form.surname" :value="form.surname" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('surname',form.surname)">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <b-input-group prepend="Correo electrónico: " class="mt-3" >
            <b-form-input v-model="form.email" :value="form.email" type="email" ></b-form-input>
              <b-input-group-append>
                <b-button  v-on:click="submit('email',form.email)" variant="outline-success">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <div class="password-box">
        <b-input-group prepend="Contraseña: " class="mt-3" >
            <b-form-input type="password"  v-model="form.password" :value="form.password" ></b-form-input>
          </b-input-group>

        <b-input-group prepend="Repite la Contraseña: " class="mt-3" >
            <b-form-input type="password" v-model="r_password" ></b-form-input>
          </b-input-group>
                <b-button variant="outline-success" v-on:click="submit('password',form.password)">Modificar</b-button>
      </div>
        
        <div class="selectors-card">
            <h6>Fecha de Nacimiento</h6>
            <b-form-datepicker v-model="form.date" class="mb-2"></b-form-datepicker>
                <b-button variant="outline-success" :show-decade-nav=true v-on:click="submit('date',form.date)">Modificar</b-button>
          </div>  
        <div class="selectors-card">
            <h6>Genero</h6>
            <b-form-select  v-model="form.gender" :value="form.gender" :options="genders" required></b-form-select>
            <b-button variant="outline-success"  v-on:click="submit('gender',form.gender)">Modificar</b-button>
          </div>  
          <div class="selectors-card">
            <h6>Lengua materna</h6>
            <b-form-select class="mt-3"  v-model="form.mother_tonge" :value="form.mother_tonge" :options="mother_tonges" required></b-form-select>
            <b-button variant="outline-success"  v-on:click="submit('mother_tonge',form.mother_tonge)">Modificar</b-button>
          </div>
          <div class="selectors-card">
            <h6>Escuela UPM</h6>
            <b-form-select class="mt-3"  v-model="form.school" :value="form.school" :options="schools" required></b-form-select>
            <b-button variant="outline-success"  v-on:click="submit('school',form.school)">Modificar</b-button>
          </div>  
      <div>
<div class="selectors-card">
  <h6>Avatar</h6>
      <b-form-file v-model="form.img"
      :state="Boolean(form.img)"
      placeholder="Elige un archivo o añadelo aquí"
      drop-placeholder="Drop file here..."
      plain
    ></b-form-file>
    <div class="mt-3">Imagen seleccionada: {{ form.img ? form.img.name : '' }}</div>
    <b-button class="mt-3" type="submit" v-on:click="submit('img',form.image)" variant="primary">Modificar imagen</b-button>
    </div>
    </div>  
</div>
</template>

<script>
import axios from 'axios'
export default {
      created(){
        axios.get('http://localhost:3000/users/' + this.$route.params.userid)

        .then(response => {
        //this.name = response.data[0].name;
            this.form.nickname = response.data.nickname;
            this.form.name = response.data.name;
            this.form.surname = response.data.surname;
            this.form.email = response.data.email;
            this.form.date = response.data.date;
            this.form.gender = response.data.gender;
            this.form.password = response.data.password;
            this.form.school = response.data.school;
            this.form.mother_tonge = response.data.mother_tonge;
            this.form.image = response.data.image;
        })
    },
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
          image: null,
          points: 0,
          position: 10,
          admin: false
        },
        genders: [{ text: 'Select One', value: null }, 'Masculino', 'Femenino', 'No binario', 'Prefiero no decirlo'],
        schools: [{ text: 'Select One', value: null }, 'ETSIINF', 'ETSII', 'ETSIAE', 'INEF'],
        mother_tonges: [{ text: 'Select One', value: null }, 'Español', 'Ingles', 'Frances', 'Chino'],
        show: true,
        r_password: ''
      }
    },
        methods:{
      submit(type,value){
        var payload = {}; 
          switch (type){
            case 'nickname': payload = {nickname:value}; break;
            case 'name': payload = {name:value}; break;
            case 'surname': payload = {surname:value}; break;
            case 'date': payload = {date:value}; break;
            case 'gender': payload = {gender:value}; break;
            case 'school': payload = {school:value}; break;
            case 'mother_tonge': payload = {mother_tonge:value}; break;
            case 'image': payload = {image:value}; break;
            case 'email': payload = {email:value}; break; 
            case 'password': payload = {password:value}; break; 
          }
            axios.patch('http://localhost:3000/users/' + this.$route.params.userid, payload);
        },
      
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
  padding: 3%;
  border: 1px solid var(--border);
  margin: 2%;
}

.selectors-card > button{
 margin-top: 2% ;
}
</style>