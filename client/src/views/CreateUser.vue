<template>
  <div class="modify-user-body">
    <div class="close-modal">
      <router-link to="/">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </router-link>
    </div>
    <h4>Create account</h4>
    <b-form @submit="submit">
      <b-input-group prepend="* Username: " class="mt-3">
        <b-form-input required v-model="form.nickname"></b-form-input>
      </b-input-group>

      <b-input-group prepend="* Name: " class="mt-3">
        <b-form-input required v-model="form.name"></b-form-input>
      </b-input-group>

      <b-input-group prepend="* Surname: " class="mt-3">
        <b-form-input required v-model="form.surname"></b-form-input>
      </b-input-group>

      <b-input-group prepend="* Email: " class="mt-3">
        <b-form-input required v-model="form.email" type="email"></b-form-input>
      </b-input-group>

      <div class="password-box">
        <b-input-group prepend="* Password: " class="mt-3">
          <b-form-input
            required
            type="password"
            id="input-live"
            aria-describedby="input-live-help input-live-feedback"
            v-model="form.password"
            :state="password_state"
            trim
          ></b-form-input>
          <b-form-invalid-feedback id="input-live-feedback">
            Password must contain between 6 and 12 characters, one uppercas letter and a non alphabetic character.
          </b-form-invalid-feedback>
        </b-input-group>

        <b-input-group prepend="* Repite la Contraseña: " class="mt-3">
          <b-form-input
            required
            type="password"
            v-model="r_password"
            :state="repeat_password"
            aria-describedby="r_password_helper"
          ></b-form-input>
          <b-form-invalid-feedback id="r_password_helper">
            Passwords need to match.
          </b-form-invalid-feedback>
        </b-input-group>
      </div>
      <div class="selectors-card">
        <h6>* Birthdate:</h6>
        <b-form-datepicker
          v-model="form.date"
          class="mb-2"
          :state="form.date!=''"
          :show-decade-nav="true"
        ></b-form-datepicker>
      </div>
      <div class="selectors-card">
        <h6>Gender:</h6>
        <b-form-select v-model="form.gender" :options="genders"></b-form-select>
      </div>
      <div class="selectors-card">
        <h6>Mother tongue</h6>
        <b-form-select
          class="mt-3"
          v-model="form.mother_tongue"
          :options="mother_tongue"
        ></b-form-select>
      </div>
      <div class="selectors-card">
        <h6>* UPM school</h6>
        <b-form-select
          class="mt-3"
          v-model="form.school"
          :options="schools"
          required
        ></b-form-select>
      </div>
      <!--<div>
        <div class="selectors-card">
          <h6>Imagen de perfil</h6>
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
      </div>-->
      <b-button class="mt-3" type="submit" variant="primary">Enviar</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
export default {
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
        mother_tongue: "",
        points: 0,
        proposals: [],
        accepted_neo: [],
        fav_neo: [],
        privileges: "user",
      },
      image: undefined,
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
      mother_tongue: [
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
    };
  },
  computed: {
    password_state() {
      return (
        this.form.password.length > 6 &&
        this.form.password.length < 14 &&
        this.isUpper(this.form.password) &&
        this.hasNumeric(this.form.password)
      );
    },
    repeat_password() {
      return this.form.password.localeCompare(this.r_password) ? false : true;
    },
  },
  methods: {
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

      for (const i in this.form) {
        formData.append(i, this.form[i]);
      }
      if(this.password_state && this.repeat_password && this.form.date != ""){
        axios
          .post("http://127.0.0.1:5000/users", formData, {
            withCredentials: true,
          })
          .then((res) => {
            if(res.status==201){
              this.flashMessage.show({
                  status: "success",
                  title: "¡Registation complete!",
                  message: "Log in now to starat your experience",
                  time: 5000,
                  position: 'right bottom'
                });
            }
            this.$router.push({ path: `/login` });
          });
      } else {
        this.flashMessage.show({
                  status: "error",
                  title: "Error while signing in",
                  message: "Review the fields with red warnings",
                  time: 5000,
                  position: 'left top'
                });
      }
    },
    isUpper(str) {
      var result = false;
      for (let index = 0; !result && index < str.length; index++) {
        var character = str.charAt(index);
        if (character == character.toUpperCase()) {
          result = true;
        }
      }
      return result;
    },
    hasNumeric(str) {
      var result = false;
      for (let index = 0; !result && index < str.length; index++) {
        if (!isNaN(str.charAt(index) * 1)) {
          result = true;
        }
      }
      return result;
    },
    handleUploadImage(event) {
      this.image = event.target.files[0];
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
</style>