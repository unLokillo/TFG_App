<template>
  <div class="modify-user-body">
          <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h4>Modificar Propuesta de Neologismo</h4>

          <b-input-group prepend="Neologismo: " class="mt-3" >
            <b-form-input :value="neo_name" ></b-form-input>
          </b-input-group>

        <h6> Modificar Fuentes</h6>
          <div v-for="(value,index) in sources" :key="index">
          <b-input-group prepend="Fuente: " class="mt-3" >
            <b-form-input :value="value.source" ></b-form-input>
          </b-input-group>
        </div>
        <h6> Añadir Fuentes</h6>
        <TodoBox/>
        <h6>Modificar Descripciones</h6>
          <div v-for="(value,index) in descriptions" :key="index">
          <b-input-group prepend="Descripción: " class="mt-3" >
            <b-form-input :value="value.description" ></b-form-input>
          </b-input-group>
        </div>
      <h6> Añadir Descripciones</h6>
      <TodoBox/>
    <b-button class="mt-3" type="submit" variant="primary">Modificar</b-button>
</div>
</template>

<script>
import TodoBox from '@/components/TodoBox.vue'
export default {
  components: {
    TodoBox
  },
    data() {
        return{
          neo_name: 'Neologismo_1',
          sources: [
            {id: '123',source: 'RAE'},
          {id: '123',source: 'Vandal'},
          {id: '123',source: 'ETSISI Enfurecida'}
            ],
          descriptions: [
          {id: '123',description: 'Descripción 1'},
          {id: '123',description: 'Descripción 2'},
          {id: '123',description: 'DEscripcion 3'}
          ]
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


h4,h6{
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}
</style>