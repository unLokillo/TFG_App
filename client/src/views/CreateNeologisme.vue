<template>
    <div class="create-neologisme-body">
    <div class="close-modal"><router-link to="/">  <font-awesome-icon style="font-size: 140%;" icon="times"/> </router-link></div>
        <b-form-input id="input-1" v-model="neologisme" type="text" placeholder="Introduce el Neologismo" required></b-form-input>

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
    background-color: var(--main-color);
    padding: 3%;
    overflow: scroll;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.todo-card{
  width: 100%;
}
</style>