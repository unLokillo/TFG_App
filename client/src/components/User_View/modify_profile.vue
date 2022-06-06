<template>
  <div class="modify-user-body">
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>
    <h4>Modify profile</h4>
    <b-input-group prepend="Alias: " class="mt-3">
      <b-form-input
        v-model="form.nickname"
        :value="form.nickname"
      ></b-form-input>
    </b-input-group>

    <b-input-group prepend="Name: " class="mt-3">
      <b-form-input v-model="form.name" :value="form.name"></b-form-input>
    </b-input-group>

    <b-input-group prepend="Surname: " class="mt-3">
      <b-form-input v-model="form.surname"></b-form-input>
    </b-input-group>

    <b-input-group prepend="Email: " class="mt-3">
      <b-form-input
        v-model="form.email"
        :value="form.email"
        type="email"
      ></b-form-input>
    </b-input-group>

    <div class="password-box">
      <b-input-group prepend="Passwords: " class="mt-3">
        <b-form-input
          type="password"
          v-model="form.password"
          :value="form.password"
        ></b-form-input>
      </b-input-group>

      <b-input-group prepend="Password again: " class="mt-3">
        <b-form-input type="password" v-model="r_password"></b-form-input>
      </b-input-group>
    </div>

    <div class="selectors-card">
      <h6>Birthdate: {{form.date}}</h6>
      <b-form-datepicker v-model="form.date" class="mb-2">{{form.date}}</b-form-datepicker>
    </div>
    <div class="selectors-card">
      <h6>Gender</h6>
      <b-form-select
        v-model="form.gender"
        :value="form.gender"
        :options="genders"
        required
      ></b-form-select>
    </div>
    <div class="selectors-card">
      <h6>Mother tongue</h6>
      <b-form-select
        class="mt-3"
        v-model="form.mother_tongue"
        :value="form.mother_tongue"
        :options="mother_tonges"
        required
      ></b-form-select>
    </div>
    <div class="selectors-card">
      <h6>UPM school</h6>
      <b-form-select
        class="mt-3"
        v-model="form.school"
        :value="form.school"
        :options="schools"
        required
      ></b-form-select>
    </div>
    <div>
    <b-button
        class="mt-3"
        type="submit"
        v-on:click="submit()"
        variant="primary"
        >Save</b-button
      ><br><br><br>
      <!--<div class="selectors-card">
        <h6>Avatar</h6>
        <b-form-file
          v-model="form.img"
          :state="Boolean(form.img)"
          placeholder="Elige un archivo o añadelo aquí"
          drop-placeholder="Drop file here..."
          plain
        ></b-form-file>
        <div class="mt-3">
          Imagen seleccionada: {{ form.img ? form.img.name : "" }}
        </div>
        <b-button
          class="mt-3"
          type="submit"
          v-on:click="submit('img', form.image)"
          variant="primary"
          >Modificar imagen</b-button
        >
      </div>-->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/users/0", { withCredentials: true })
      .then((response) => {
        //this.name = response.data[0].name;
        this.form.nickname = response.data.nickname;
        this.form.name = response.data.name;
        this.form.surname = response.data.surname;
        this.form.email = response.data.email;
        this.form.date = response.data.date;
        this.firstdate = response.data.date;
        this.form.gender = response.data.gender;
        this.form.password = response.data.password;
        this.form.school = response.data.school;
        this.form.mother_tongue = response.data.mother_tongue;
        this.form.image = response.data.image;
      });
  },
  data() {
    return {
      form: {
        nickname: "",
        name: "",
        surname: "",
        email: "",
        date: "",
        gender: "",
        password: "",
        school: "",
        mother_tonge: "",
        image: null,
        points: 0,
        position: 10,
        admin: false,
      },
      genders: [
        { text: "Select One", value: null },
        "Masculine",
        "Femenine",
        "Non binary",
        "Prefer not to say",
      ],
      schools: [
        { text: "Select One", value: null },
        "ETSAM",
        "ETSE",
        "ETSIINF",
        "ETSII",
        "ETSIAE",
        "INEF",
        "ETSISI",
        "ETSIST",
        "ETSME",
      ],
      mother_tonges: [
        { text: "Select One", value: null },
        "Spanish",
        "English",
        "Portuguese",
        "German",
        "French",
        "Chinese",
      ],
      show: true,
      r_password: "",
      firstdate: ""
    };
  },
  methods: {
    submit() {
      var formData = new FormData();
      formData.append('do', 'modify');
      formData.append('nickname', this.form.nickname);
      formData.append('name', this.form.name);
      formData.append('surname', this.form.surname);
      formData.append('email', this.form.email);
      if(this.firstdate!=this.form.date){
        formData.append('date', this.form.date);
      }
      formData.append('gender', this.form.gender);
      formData.append('password', this.form.password);
      formData.append('school', this.form.school);
      formData.append('mother_tongue', this.form.mother_tongue);
      axios.put("http://127.0.0.1:5000/users/" +
        this.$route.params.userid,
        formData,
        { withCredentials: true }
        ).then(res => {
          if(res.status==201){
            this.$router.go(-1);
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
  padding: 3%;
  border: 1px solid var(--border);
  margin: 2%;
}

.selectors-card > button {
  margin-top: 2%;
}
</style>