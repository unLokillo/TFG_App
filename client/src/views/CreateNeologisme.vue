<template>
  <div class="create-neologisme-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h4>Crear Neologismo</h4>
    <p style="font-size: 14px">
      <i>
        Un neologismo es una palabra del ámbito del Internet de las Cosas que te
        parezca novedosa.</i
      >
    </p>
    <h6>Neologismo</h6>
    <b-form-input
      id="input-1"
      v-model="form.neologisme"
      type="text"
      placeholder="Introduce el Neologismo"
      required
    ></b-form-input>
    <div>
      <div>
        <h6>Contextos</h6>
        <p style="font-size: 14px">
          <i>
            Añade descripciones o definiciones que se le podrían dar al
            neologismo</i
          >
        </p>
        <TodoBox v-on:childToParent="onDescriptionsClick" />
      </div>

      <h6>Fuentes</h6>
      <p style="font-size: 14px">
        <i> Indica con detalle dónde lo has encontrado </i>
      </p>
      <TodoBox v-on:childToParent="onSourcesClick" />
    </div>
    <h6>Imagen</h6>
    <div class="selectors-card">
      <input
        type="file"
        name="image"
        id="image"
        class="custom-file-upload-hidden"
        ref="image"
        accept=".jpg, .png"
        @change="handleUploadImage"
      />
    </div>
    <b-button @click="submit"> Listo </b-button>
  </div>
</template>

<script>
import axios from "axios";
import TodoBox from "@/components/TodoBox.vue";
export default {
  name: "Home",
  components: {
    TodoBox,
  },
  data() {
    return {
      image: undefined,
      form: {
        neologisme: "",
        descriptions: "",
        sources: "",
      },
    };
  },
  methods: {
    // Triggered when `childToParent` event is emitted by the child.
    onDescriptionsClick(value) {
      this.form.descriptions = value;
    },
    onSourcesClick(value) {
      this.form.sources = value;
    },
    submit(event) {
      event.preventDefault();
      var formData = new FormData();
      if (this.image != undefined) {
        formData.append("imagen", this.image, this.image.name);
        formData.append("imageno", "yes");
      } else {
        this.image = "default";
        formData.append("imageno", "default");
      }

      // Add descriptions
      for (var i = 0; i < this.form["descriptions"].length; i++) {
        formData.append(
          "description" + i,
          JSON.parse(JSON.stringify(this.form["descriptions"][i])).value
        );
      }
      formData.append("numDescr", this.form["descriptions"].length);

      // Add sources
      for (var i = 0; i < this.form["sources"].length; i++) {
        formData.append(
          "source" + i,
          JSON.parse(JSON.stringify(this.form["sources"][i])).value
        );
      }
      formData.append("numSources", this.form["sources"].length);

      formData.append("neologisme", this.form.neologisme);
      formData.append("liked", 0);
      formData.append("state", "pendiente");

      axios.post("http://127.0.0.1:5000/create-neologisme", formData, {
        withCredentials: true,
      });
      this.$router.push({ path: `/` });
    },
    handleUploadImage(event) {
      this.image = event.target.files[0];
    },
  },
};
</script>

<style>
.create-neologisme-body {
  background-color: var(--main-color);
  padding: 3%;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.todo-card {
  width: 100%;
}

h6 {
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}

.selectors-card {
  margin-bottom: 15px;
}
</style>