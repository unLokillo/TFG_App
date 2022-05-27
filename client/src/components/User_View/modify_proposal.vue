<template>
  <div class="modify-user-body" v-if="this.mostrar">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h4>Modificar Propuesta de Neologismo</h4>
    <p style="font-size: 14px">
      <i>
        Tu neologismo debe ser una palabra del ámbito del Internet de las Cosas que te
        parezca novedosa.</i
      >
    </p>
    <b-input-group prepend="Neologismo: " class="mt-3"> <!-- Término en español -->
      <b-form-input v-model="form.neologisme"></b-form-input>
    </b-input-group>
    <!-- <b-input-group prepend="Término en inglés: " class="mt-3">
      <b-form-input v-model="form.name_eng"></b-form-input>
    </b-input-group> -->
    <h6 v-if="this.mostrar && this.ndes>0">Modificar Contextos</h6>
    <div v-for="(value, index) in form.descriptions" :key="index">
      <b-input-group prepend="Descripción: " class="mt-3">
        <b-form-input v-model="form.descriptions[index][0]"></b-form-input>
        <b-input-group-append>
          <b-button
            style="background-color: darkred !important"
            v-on:click="del('description_single', index)"
            >Eliminar</b-button
          >
        </b-input-group-append>
      </b-input-group>
    </div>
    <h6>Añadir Contextos</h6>
    <p style="font-size: 14px">
      <i> Incluye la frase completa en la que has encontrado el neologismo o descripciones que se le puedan dar</i>
    </p>
    <TodoBox v-on:childToParent="onDescriptionsClick" />

    <h6 v-if="this.mostrar && this.nsour>0">Modificar Fuentes</h6>
    <div v-for="(value, index) in form.sources" :key="'A' + index">
      <b-input-group prepend="Fuente: " class="mt-3">
        <b-form-input v-model="form.sources[index][0]"></b-form-input>
        <b-input-group-append>
          <b-button
            style="background-color: darkred !important"
            v-on:click="del('source_single', index)"
            >Eliminar</b-button
          >
        </b-input-group-append>
      </b-input-group>
    </div>
    <h6>Añadir Fuentes</h6>
    <p style="font-size: 14px">
      <i> Indica con detalle dónde lo has encontrado </i>
    </p>
    <TodoBox v-on:childToParent="onSourcesClick" />
    <b-button
      class="mt-3"
      type="submit"
      variant="primary"
      v-on:click="submit()"
      >Modificar</b-button
    >
  </div>
</template>

<script>
import TodoBox from "@/components/TodoBox.vue";
import axios from "axios";
export default {
  components: {
    TodoBox,
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/neologismes/" +
      this.$route.params.neoId,
      { withCredentials: true })
      .then((response_neo) => {
        this.form = response_neo.data;
        this.ndes = this.form.descriptions.length;
        this.nsour = this.form.sources.length;
      })
  },
  data() {
    return {
      form: [],
      descriptions: [],
      login: [],
      sources: [],
      name: "",
      neo_aux: "",
      mostrar: false,
      ndes: 0,
      nsour: 0
    };
  },
  mounted(){
    this.mostrar=true
  },
  methods: {
    onDescriptionsClick(value) {
      this.descriptions = value;
    },
    onSourcesClick(value) {
      this.sources = value;
    },
    addDescriptions() {
      for (let index = 0; index < this.descriptions.length; index++) {
        this.form.descriptions.push(
          this.descriptions[index].value
        );
        this.ndes++;
      }
    },
    addSources() {
      for (let index = 0; index < this.sources.length; index++) {
        this.form.sources.push(
          this.sources[index].value
        );
        this.nsour++;
      }
    },
    del(type, index) {
      var payload = {};
      switch (type) {
        case "description_single":
          this.form.descriptions.splice(index, 1);
          this.ndes--;
          payload = {
            descriptions: this.form.descriptions,
          };
          break;
        case "source_single":
          this.form.sources.splice(index, 1);
          this.nsour--;
          payload = {
            sources: this.form.sources,
          };
          break;
      }
    },
    submit() {
      this.addDescriptions();
      this.addSources();
      var formData = new FormData();
      formData.append('do', 'modify');
      formData.append('name', this.form.neologisme);
      // formData.append('name_eng', this.form.name_eng);
      for(var i = 0; i < this.form.descriptions.length; i++){
        formData.append('description' + i, this.form.descriptions[i]);
      }
      formData.append('numDescr', this.form.descriptions.length);
      for(var i = 0; i < this.form.sources.length; i++){
        formData.append('source' + i, this.form.sources[i]);
      }
      formData.append('numSourc', this.form.sources.length);

      axios.put("http://127.0.0.1:5000/neologismes/" +
        this.$route.params.neoId,
        formData,
        { withCredentials: true }
        ).then(res => {
          if(res.status==201){
            this.$router.push({ path: `/` });
          } else {
            console.log("Something went wrong: ", res.status);
          }
        });
    },
  },
};
</script>

<style scoped>
.modify-user-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3%;
}

.modal-content {
  min-height: 85%;
}
.modify-user-card {
  background-color: rgb(231, 231, 231);
  padding: 3%;
}

input {
  margin-bottom: 4%;
}
h4 {
  margin-bottom: 3%;
  border-bottom: 1px solid var(--border);
}
.selectors-style {
  display: flex;
  justify-content: space-evenly;
  padding-bottom: 3%;
}

.password-box {
  padding: 3%;
  border: 1px solid var(--border);
}

select {
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
  background: #fff
    url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E")
    no-repeat right 0.75rem center/8px 10px;
}

.selectors-card {
  margin: 2%;
}

h4,
h6 {
  border-bottom: 1px solid var(--border);
  text-align: left;
  margin: 2%;
}
</style>