<template>
    <div class="create-neologisme-body">
    <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h4>Crear Neologismo</h4>
        <p style="font-size: 14px"> <i> Un neologismo es una palabra del ámbito del Internet de las Cosas que te parezca novedosa.</i></p>
        <h6>Neologismo</h6>
        <b-form-input id="input-1" v-model="form.neologisme" type="text" placeholder="Introduce el Neologismo" required></b-form-input>
        <div>
          <h6>Fuentes</h6>
          <p style="font-size: 14px"> <i> Indica con detalle dónde lo has encontrado </i> </p>
          <TodoBox v-on:childToParent="onSourcesClick"/>
        </div>

        <div>
          <h6>Contextos</h6>
            <p style="font-size: 14px"> <i> Incluye la frase completa en la que has encontrado el neologismo</i> </p>
          <TodoBox v-on:childToParent="onDescriptionsClick"/>
        </div>
    <h6>Imagen</h6>
    <div>
      <b-form-file v-model="form.img"
      :state="Boolean(form.img)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
      plain
    ></b-form-file>
    <div class="mt-3">Archivo seleccionado: {{ form.img ? form.img.name : '' }}</div>
    </div>
    <b-button @click="submit"> Listo </b-button>
    </div>

</template>

<script>
import axios from 'axios';
import TodoBox from '@/components/TodoBox.vue'
export default {
  name: 'Home',
  components: {
    TodoBox
  },
  data(){
  return {
    form:{
          neologisme: '',
          descriptions: '',
          sources: '',
          img: null,
          liked: 0,
          proposal: true,
          user: [],
      }
  }
  },
  methods: {
    // Triggered when `childToParent` event is emitted by the child.
    onDescriptionsClick (value) {
      this.form.descriptions = value;
    },
    onSourcesClick (value) {
      this.form.sources = value;
      console.log(this.form.sources);
    },
    formatDate() {
    var d = Date.now()
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;
    console.log("asdas");
    return [year, month, day].join('-');
},
    submit(){
        console.log(this.formatDate());
        axios.get('http://localhost:3000/login/1')
          .then(response => {
            axios.get('http://localhost:3000/users/' + response.data.user_id)
             .then(response_user => {
               this.form.user.push({
                 user: response_user.data.nickname,
                 user_id: this.$route.params.userid,
                 date:  this.formatDate(),
                 rejected: false,
                 mssg: ''
               })
            axios.post('http://localhost:3000/neologismes', this.form)
              .then(function( response ){
                    // Handle success
              }.bind(this));
               });
            });
        this.$router.push({ path: `/` }) // -> /user/123
    }  
  }
}
</script>

<style>
.create-neologisme-body{
    background-color: var(--main-color);
    padding: 3%;
    overflow: scroll;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.todo-card{
  width: 100%;
}

 h6{
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}
</style>