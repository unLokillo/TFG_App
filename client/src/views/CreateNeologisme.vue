<template>
    <div class="create-neologisme-body">
    <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <h4>Crear Neologismo</h4>
        <b-form-input id="input-1" v-model="form.neologisme" type="text" placeholder="Introduce el Neologismo" required></b-form-input>
        <div>
          <h6>Fuentes</h6>
          <TodoBox v-on:childToParent="onSourcesClick"/>
        </div>

        <div>
          <h6>Descripciones</h6>
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
    <div class="mt-3">Selected file: {{ form.img ? form.img.name : '' }}</div>
    </div>
    <b-button @click="submit"> DONE</b-button>
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
          points:0,
          user: '',
          date: '',
          rejected: false,
          mssg: ''
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
    },
    prepare_data(){
        this.form.date = Date.now(); // get actual date
        var user_get = "";
        axios.get('http://localhost:3000/login/1')
          .then(response => {
            axios.get('http://localhost:3000/users/' + response.data.user_id)
             .then(response => {
                 user_get = (' ' + response.data.nickname).slice(1);
                 console.log('response.data.nickname');
                 console.log(response.data.nickname);
               });
            });
            console.log(user_get);
            return user_get;
        },
    submit(){
        this.form.user = this.prepare_data();
        console.log(this.form.user);
        axios.post('http://localhost:3000/neologismes', this.form)
              .then(function( response ){
                    // Handle success
              }.bind(this));
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

h4, h6{
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}
</style>