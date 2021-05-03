<template>
<div>
<div class="todo-card">
  <b-form-textarea
      id="textarea"
      v-model="newItem"
      placeholder="Enter something..."
      rows="3"
      max-rows="6"
    ></b-form-textarea>
    <b-button @click="addItem">Add</b-button>
    </div>
    <b-list-group>
      <b-list-group-item class="list-item" v-for="(value,index) in items" :key=index><div>{{ value.description }} </div><b-button @click="removeItem(value.id)">X</b-button></b-list-group-item>
  </b-list-group>

</div>
</template>

<script>
export default {
    data(){
        return {
          newItem: '',
          items: []
        }
    },
     methods: {
      addItem: function() {
        if (this.items.length>0) {
          this.items.push({
          id: this.items[this.items.length-1].id + 1,
          description: this.newItem,
          completed: false,
        });
        } else {
          this.items.push({
          id: this.items.length + 1,
          description: this.newItem,
          completed: false,
        });
        }
        this.newItem = '';
      },
     removeItem: function (itemID) {
        this.items = this.items.filter((newItem) => newItem.id!== itemID);
      } 
     }
}
</script>

<style>
.list-item{
  display: flex;
  justify-content: space-evenly;
}
.list-item > div{
overflow:auto;
margin: 10px;
}
.todo-card{
  display: flex;
}
</style>