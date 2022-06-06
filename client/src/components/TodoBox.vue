<template>
  <div>
    <div class="todo-card">
      <b-form-textarea
        v-model="newItem"
        placeholder="Introduce the information"
        rows="3"
        max-rows="6"
        v-on:keyup="emitToParent"
        maxlength="500"
      ></b-form-textarea>
      <b-button @click="addItem" class="bttn-todo">Click to add</b-button>
    </div>

    <b-list-group>
      <b-list-group-item
        class="list-item"
        v-on:keyup="emitToParent"
        v-for="(value, index) in items"
        :key="index"
        ><div>{{ value.value }}</div>
        <b-button @click="removeItem(value.id)" class="bttn-todo">
          <font-awesome-icon icon="times" /> </b-button
      ></b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newItem: "",
      items: [],
    };
  },
  methods: {
    addItem: function () {
      if (this.items.length > 0) {
        if (this.newItem.length > 0) {
          this.items.push({
            id: this.items[this.items.length - 1].id + 1,
            value: this.newItem,
          });
        }
      } else {
        if (this.newItem.length > 0) {
          this.items.push({
            id: 1,
            value: this.newItem,
          });
        }
      }
      this.newItem = "";
    },
    removeItem: function (itemID) {
      this.items = this.items.filter((newItem) => newItem.id !== itemID);
    },
    emitToParent(event) {
      this.$emit("childToParent", this.items);
    },
  },
};
</script>

<style>
.list-item {
  display: flex;
  /* grid-auto-columns: 5fr 1fr;
  grid-auto-flow: column;*/
  justify-content: space-between;
}

.list-item > button {
  max-width: 50%;
  max-height: 100%;
}

.list-item > input {
  min-height: 50%;
}

.list-item > div {
  overflow: auto;
  margin: 10px;
}
.todo-card {
  display: flex;
}
</style>