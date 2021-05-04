<template>
    <div class="create-neologisme-body">
        <router-link :to="`/`">X</router-link>
        <b-form>
      <b-form-group id="input-group-1" label="Neologismo" label-for="input-1">
        <b-form-input id="input-1" v-model="neologisme" type="text" placeholder="Introduce el Neologismo" required></b-form-input>
      </b-form-group>
      </b-form>

        <div>
          <h4>Fuentes</h4>
          <TodoBox/>
        </div>

        <div>
          <h4>Descripciones</h4>
          <TodoBox/>
        </div>

      <b-form-file v-model="img"
      :state="Boolean(img)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
      plain
    ></b-form-file>
    <div class="mt-3">Selected file: {{ img ? img.name : '' }}</div>
    <b-button> DONE</b-button>
    </div>

</template>

<script>
import TodoBox from '@/components/TodoBox.vue'
export default {
  name: 'Home',
  components: {
    TodoBox
  },
  data(){
  return {
          neologisme: '',
          img: null
      }
  }
  }

</script>

<style>
.create-neologisme-body{
    background-color: rgb(231, 231, 231);
    padding: 3%;
    max-height: 550px;
    overflow: scroll;
}
</style>