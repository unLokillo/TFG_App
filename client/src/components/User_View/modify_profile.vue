<template>
  <div class="modify-user-body">
        <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h4>Modificar Información de usuario</h4>

          <b-input-group prepend="Nombre de Usuario: " class="mt-3" >
            <b-form-input :value="form.user_name" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

          <b-input-group prepend="Nombre: " class="mt-3" >
            <b-form-input :value="form.name" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <b-input-group prepend="Apellidos: " class="mt-3" >
            <b-form-input :value="form.user_name" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <b-input-group prepend="email: " class="mt-3" >
            <b-form-input :value="form.user_name" type="email" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success">Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

      <div class="password-box">
        <b-input-group prepend="Contraseña: " class="mt-3" >
            <b-form-input type="password" :value="form.password" ></b-form-input>
          </b-input-group>

        <b-input-group prepend="Repite la Contraseña: " class="mt-3" >
            <b-form-input type="password" :value="form.r_password" ></b-form-input>
          </b-input-group>
                <b-button variant="outline-success">Modificar</b-button>
      </div>

          <div class="selectors-card">
            <h6>Genero</h6>
            <b-form-select :value="form.gender" :options="genders" required></b-form-select>
          </div>  
          <div class="selectors-card">
            <h6>Lengua materna</h6>
            <b-form-select class="mt-3" :value="form.mother_tonge" :options="mother_tonge" required></b-form-select>
          </div>
          <div class="selectors-card">
            <h6>Escuela UPM</h6>
            <b-form-select class="mt-3" :value="form.mother_tonge" :options="mother_tonge" required></b-form-select>
          </div>  
      <div>

      <b-form-file v-model="img"
      :state="Boolean(img)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
      plain
    ></b-form-file>
    <div class="mt-3">Selected file: {{ img ? img.name : '' }}</div>
    </div>
    <b-button class="mt-3" type="submit" variant="primary">Submit</b-button>
</div>
</template>

<script>
export default {
    data() {
        return{
        form: {
          user_name: 'User_1',
          name: 'Username',
          surname: 'Apellido_1',
          email: 'emai@email.com',
          date: '',
          password: 'contraseña',
          r_password: 'contraseña',
          mother_tonge: 'Español',
          gender: 'non binary',
          image: null,
        },
        genders: [{ text: 'Select One', value: null }, 'male', 'female', 'non binary', 'undefined'],
        mother_tonge: [{ text: 'Elige una ', value: null }, 'Español', 'Ingles', 'Frances', 'Aleman'],
        show: true
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