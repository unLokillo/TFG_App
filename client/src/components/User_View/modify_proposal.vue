<template>
  <div class="modify-user-body">
          <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <h4>Modificar Propuesta de Neologismo</h4>
        <p style="font-size: 14px"> <i> Un neologismo es una palabra del ámbito del Internet de las Cosas que te parezca novedosa.</i></p>
          <b-input-group prepend="Neologismo: " class="mt-3" >
            <b-form-input :value="form.neologisme" ></b-form-input>
              <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('neologisme')" >Modificar</b-button>
              </b-input-group-append>
          </b-input-group>

        <h6> Modificar Fuentes</h6>
          <div v-for="(value,index) in form.sources" :key="'A'+index">
          <b-input-group prepend="Fuente: " class="mt-3" >
            <b-form-input v-model="form.sources[index].value" ></b-form-input>
            <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('source_single')" >Modificar</b-button>
              </b-input-group-append>
          </b-input-group>
        </div>
        <h6> Añadir Fuentes</h6>
          <p style="font-size: 14px"> <i> Indica con detalle dónde lo has encontrado </i> </p>
        <TodoBox v-on:childToParent="onSourcesClick"/>

        <h6>Modificar Contextos</h6>
          <div v-for="(value,index) in form.descriptions" :key="index">
          <b-input-group prepend="Descripción: "  class="mt-3" >
            <b-form-input v-model="form.descriptions[index].value" ></b-form-input>
            <b-input-group-append>
                <b-button variant="outline-success" v-on:click="submit('description_single')" >Modificar</b-button>
              </b-input-group-append>
          </b-input-group>
        </div>
      <h6> Añadir Contextos</h6>
        <p style="font-size: 14px"> <i> Incluye la frase completa en la que has encontrado el neologismo</i> </p>
      <TodoBox v-on:childToParent="onDescriptionsClick"/>

    <b-button class="mt-3" type="submit" variant="primary" v-on:click="submit('all')">Modificar</b-button>
</div>
</template>

<script>
import TodoBox from '@/components/TodoBox.vue'
import axios from 'axios'
export default {
  components: {
    TodoBox
  },
    created(){
        axios.get("http://localhost:3000/neologismes/" + this.$route.params.neoId)
        .then(response_neo => {
            this.form = response_neo.data;
        }),
        axios.get("http://localhost:3000/login/1")
        .then(response => {
            this.login = response.data;
        })
    },
    data() {
        return{
          form:[],
          descriptions: [],
          login:[],
          sources: [],
          name: '',
          neo_aux: ''
    }
  },
  methods: {
    onDescriptionsClick (value) {
      this.descriptions = value;
    },
    onSourcesClick (value) {
      this.sources = value;
    },
    addDescriptions(){
          for (let index = 0; index < this.descriptions.length; index++) {
              this.form.descriptions.push({
                id:this.form.descriptions[this.form.descriptions.length-1].id+(1+index),
                value:this.descriptions[index].value
                });    
            }
    },
    addSources(){
          for (let index = 0; index < this.sources.length; index++) {
              this.form.sources.push({
                id:this.form.sources[this.form.sources.length-1].id+(1+index),
                value:this.sources[index].value
                });    
            }
    },
    
    submit(type){
        var payload = {};
        for (let index = 0; index < this.form.user.length; index++) {
              if(this.login.user_id==this.form.user[index].user_id){
                  this.form.user.splice(index,1,{
                    user_id: this.form.user[index].user_id,
                    user: this.form.user[index].user,
                    date: this.form.user[index].date,
                    rejected:false,
                    mssg:"",
                    modify_elements: this.mod_elements
                  }) 
              break;
              }
          };
          console.log(this.form.neologisme);
          switch (type){
            case 'neologisme': payload = {
              neologisme:this.form.neologisme,
              modify:true,
              user: this.form.user
              }; 
              break;
            case 'description_single': payload = {
              descriptions:this.form.descriptions,
              modify:true,
              user: this.form.user
              };
               break;
            case 'source_single': payload = {
              sources:this.form.sources,
              modify:true,
              user: this.form.user
            }; break;
            case 'all': 
              this.addDescriptions();
              this.addSources();
            payload = {
              neologisme: this.form.neologisme,
              descriptions: this.form.descriptions,
              sources: this.form.sources,
              modify:true,
              user: this.form.user
            }
            break;
          }
            axios.patch('http://localhost:3000/neologismes/' +  this.$route.params.neoId, payload)
                .then(function( response ){
                    // Handle success
                }.bind(this));
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
  margin: 2%;
}


h4,h6{
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}
</style>