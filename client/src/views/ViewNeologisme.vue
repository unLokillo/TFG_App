<template v-if='this.appear' :key="updateneo">
  <div class="card-body" v-if='this.appear'>
    <div class="close-modal">
      <a @click="$router.go(-1)">
        <font-awesome-icon style="font-size: 140%" icon="times" />
      </a>
    </div>

    <div class="card-neo-header">
      <h2>{{ form.neologisme }}</h2>
      <div class="neo-likes" v-if="this.liked">
        <font-awesome-icon
          v-on:click="like"
          style="color: red; font-size: 35px"
          icon="heart"
        />
        {{ this.likes  }}
      </div>
      <div class="neo-likes" v-else>
        <font-awesome-icon
          v-on:click="like"
          icon="heart"
          style="font-size: 35px; color: grey"
        />
        {{ this.likes }}
      </div>
    </div>

    <div class="rejected-neologisme-admin" v-if="form.state == 'rechazado'">
      <h4>Su propuesta ha sido rechazada</h4>
      <p>
        La propuesta del Neologismo: <strong>{{ form.neologisme }}</strong
        >, ha sido rechazada por la siguiente razón: <br />
        {{ form.mssg }}
        <br />
        <strong
          >Si usted lo desea puede modificar la informacón requerida, y el
          neologismo será evaluado nuevamente. Gracias por su atencón
        </strong>
      </p>

      <router-link
        :to="{
          name: 'm-proposal',
          params: { userid: $route.params.userid, neoId: $route.params.neoId },
        }"
        class="bttn-app"
        style="background-color: var(--fail) !important"
        >Modificar</router-link
      >
    </div>

    <div class="rejected-neologisme" v-if="rech">
      <h4>Su propuesta ha sido rechazada</h4>
      <p>
        La propuesta del Neologismo: <strong>{{ form.neologisme }}</strong
        >, ha sido rechazada por la siguiente razón: <br />
        {{ form.state }}
        <br />
        <strong
          >Si usted lo desea puede modificar la información requerida, y el
          neologismo será evaluado nuevamente. Gracias por su atención
        </strong>
      </p>

      <router-link
        :to="{
          name: 'm-proposal',
          params: { userid: $route.params.userid, neoId: $route.params.neoId },
        }"
        class="bttn-app"
        style="background-color: var(--fail) !important"
        >Modificar</router-link
      >
    </div>
    <br />
    <div class="descriptions-card">
      <h4>Contextos</h4>
      <div v-for="(value, index) in form.descriptions" :key="index">
        <div v-if="index < 3" class="descriptions">
          {{ index + 1 }}.- {{ value[0] }}
        </div>
      </div>
    </div>
    <div class="descriptions-card">
      <h4>Fuentes</h4>
      <div v-for="(value, index) in form.sources" :key="index">
        <div v-if="index < 3" class="descriptions">
          {{ index + 1 }}.- {{ value[0] }}
        </div>
      </div>
    </div>

    <!--<div class="image-card" v-if="form.img!=null">
            <b-img thumbnail :src="require(`../assets/images/${form.img}`)"  alt="Responsive image"></b-img>
        </div>-->
    <br>
    <div class="user-tag">
      <div>Creado por: {{ form.user }}</div>
      <div v-if="form.date!='None'">Aprobado el {{ form.date }}</div>
    </div>
    <div
      class="admin-options"
      v-if="(login.privileges=='linguist' || login.privileges=='admin') & form.state=='pendiente'"
      :key="updateneo"
    > 
      <b-button
        class="bttn-app"
        v-on:click="accept()"
        style="background-color: var(--success) !important"
      >
        Aceptar propuesta
      </b-button>
      <b-button
        class="bttn-app"
        :to="{
          name: 'r-neologismes',
          params: { userid: $route.params.userid, neoId: $route.params.neoId },
        }"
        style="background-color: var(--fail) !important"
      >
        Rechazar propuesta
      </b-button>
    </div>

    <router-link
      v-if="form.state=='pendiente'"
      tag="b-button"
      class="bttn-app"
      :to="{
        name: 'm-neologismes',
        params: { userid: $route.params.userid, neoId: $route.params.neoId },
      }"
    >
      Modificar propuesta
    </router-link>

    <div v-if="form.state == 'aceptado' && (username == form.user || login.privileges == 'admin' || login.privileges == 'linguist')">
      <b-button
        class="bttn-app"
        @click="deleteneo"
        style="background-color: var(--fail) !important"
      >
        Eliminar neologismo
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  created() {
    axios
      .get("http://127.0.0.1:5000/neologismes/" + this.$route.params.neoId, {
        withCredentials: true,
      })
      .then((response_neo) => {
        this.form = response_neo.data;
        this.rech = this.form.state.includes('rechazado')
      });
    axios
      .get("http://127.0.0.1:5000/user", { withCredentials: true })
      .then((response_u) => {
        this.login = response_u.data;
      });
      axios
      .get(
        "http://127.0.0.1:5000/neologismes/" +
          this.$route.params.neoId +
          "/likes",
        { withCredentials: true }
      )
      .then((response) => {
        this.response = response;
        this.loging();
        
      });
  },
  watch: {
    $route: {
      immediate: true,
      handler: function (newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      },
    },
  },
  data() {
    return {
      proposals: [],
      login: [],
      form: [],
      form_user: [],
      appear: false,
      liked: false,
      likes: 0,
      username: null,
      updateneo: 0,
      rech: false,
      response: ""
    };
  },
  methods: {
    
    async loging() {
      let res = await axios
        .get("http://127.0.0.1:5000/login", { withCredentials: true });
      this.username = res.data.username;
      this.liked = false;
      var i = 0
      for (i; i < this.response.data.length; i++){
        if (this.username == this.response.data[i].nickname) {
          this.liked = true;
        }
      }
      this.likes = i;
      this.appear = true;
    },
    like() {
      axios
        .get("http://127.0.0.1:5000/login", { withCredentials: true })
        .then((res) => {
          if (res.status != 200) {
            this.$router.push("/login");
          }
          this.username = res.data.username;
        });
      axios
        .get(
          "http://127.0.0.1:5000/neologismes/" +
            this.$route.params.neoId +
            "/likes",
          { withCredentials: true }
        )
        .then((response) => {
          this.liked = false;
          for (var i = 0; i < response.data.length; i++)
            if (this.username == response.data[i].nickname) {
              this.liked = true;
              break;
            }
          this.likes = response.data.length
        });

      if (this.liked)
        axios.delete(
          "http://127.0.0.1:5000/neologismes/" +
            this.$route.params.neoId +
            "/likes",
          { withCredentials: true }
        ).then(res => {
          if(res.status==204){
            this.liked = false;
            this.likes -= 1;
          }
        });
      else
        axios.post(
          "http://127.0.0.1:5000/neologismes/" +
            this.$route.params.neoId +
            "/likes",
            "carga",
          { withCredentials: true }
        ).then(res => {
          if(res.status==201){
            this.liked = true;
            this.likes += 1;
          }
        });
    },

    accept() {
      var formData = new FormData();
      formData.append('do', 'accept');
      axios.put("http://127.0.0.1:5000/neologismes/" +
        this.$route.params.neoId,
        formData,
        { withCredentials: true }
        );
      this.updateneo += 1
    },
    deleteneo() {
      axios.delete("http://127.0.0.1:5000/neologismes/" +
        this.$route.params.neoId,
        { withCredentials: true }
        ).then(res => {
          if (res.status==204){
            this.$router.go(-1)
          } else console.log("Something went wrong while deleting")
        });
    }
  },
};
</script>


<style lang="scss" scoped>
.card-body {
  display: flex;
  flex-direction: column;
  overflow: scroll;

  align-content: center;
}
.descriptions {
  margin-bottom: 2%;
  padding: 1%;
  text-align: left;
  border-left: 10px solid var(--border-left);
}
.card-neo-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
}
.user-tag {
  display: flex;
  flex-direction: column;
  padding-bottom: 5%;
  color: grey;
  font-size: 14px;
}
.descriptions-card {
  border-bottom: 1px solid var(--border);
}

h4 {
  text-align: left;
  margin-top: 1%;
}

.img-thumbnail {
  margin: 2% 0 2% 0;
  background-color: var(--border-left);
}
.admin-options {
  display: flex;
  justify-content: space-evenly;
}
.rejected-neologisme {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  margin-top: 2%;
  border: 2px solid var(--fail);
}

.rejected-neologisme > h4 {
  border-bottom: 1px solid var(--border);
  margin: 2%;
}

.card-body > button {
  max-height: 3rem;
}

.admin-options {
  margin-bottom: 3%;
}

.rejected-neologisme-admin {
  overflow: scroll;
  max-height: 30rem;
}
</style>