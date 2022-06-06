<template>
  <div class="create-neologisme-body">
    <FlashMessage :position="'left top'"></FlashMessage>
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h4>Propose a term</h4>
    <p style="font-size: 14px">
      <i>
        This term should be related to sustainability and needs a good definition or context, as well as sources.</i
      >
    </p>
    <!-- <h6>Término en inglés</h6>
    <b-form-input
      id="input-1"
      v-model="form.name_eng"
      type="text"
      placeholder="Introduce el término en inglés"
      required
    ></b-form-input>
    <h6>Término en español</h6> -->
    <b-form-input
      id="input-1"
      v-model="form.neologisme"
      type="text"
      placeholder="Term"
      required
    ></b-form-input> <!--  término en español -->
    <div>
      <div>
        <h6>Definitions/contexts</h6>
        <p style="font-size: 14px">
          <i>
            Add descriptions, definitions or context that apply to this term.
          </i>
        </p>
        <TodoBox v-on:childToParent="onDescriptionsClick" />
      </div>

      <h6>Sources</h6>
      <p style="font-size: 14px">
        <i> Point out with detail where did you find the term </i>
      </p>
      <TodoBox v-on:childToParent="onSourcesClick" />
    </div><br>
    <!--<h6>Imagen</h6>
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
    </div>-->
    <b-button @click="submit"> Submit </b-button>
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
        // name_eng: "",
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
      /*if (this.image != undefined) {
        formData.append("imagen", this.image, this.image.name);
        formData.append("imageno", "yes");
      } else {
        this.image = "default";
        formData.append("imageno", "default");
      }*/

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
      // formData.append("name_eng", this.form.name_eng);
      formData.append("liked", 0);
      formData.append("state", "pendiente");

      axios.post("http://127.0.0.1:5000/neologismes", formData, {
        withCredentials: true,
      });
      this.flashMessage.show({
        status: "success",
        title: "Term proposal created",
        message: "You have earned a new BADGE! Search the badges section in the sidebar to check it out",
        time: 8000,
        position: "left top"
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