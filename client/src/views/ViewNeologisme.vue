<template>
    <div class="card-body">
      <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
         
        <div class="card-neo-header">
            <h2>{{ form.neologisme }}</h2>
            <div class="neo-likes" v-if="seeLiked" ><font-awesome-icon v-on:click="like" style="color:red;" icon="heart"/> {{ form.liked }}</div> 
            <div class="neo-likes" v-else ><font-awesome-icon v-on:click="like" icon="heart"/> {{ form.liked }}</div> 
        </div>
        
        <div class="rejected-neologisme-admin" v-if="form.user[0].rejected">
            <h4>Su propuesta ha sido rechazada</h4>
            <p>La propuesta del Neologismo: <strong>{{ form.neologisme }}</strong>, ha sido rechazada por la siguiente razón: <br>
            {{ form.mssg }}
            <br>
            <strong>Si usted lo desea puede modificar la informacón requerida, y el neologismo sera evaluado nuevamente.
                Gracias por su atencón
            </strong>
        </p>

            <router-link :to="{name: 'm-proposal',params: { userid: $route.params.userid ,neoId: $route.params.neoId}}" class="bttn-app" style="background-color: var(--fail) !important">Modificar</router-link>
        </div>

        <div class="rejected-neologisme" v-if="form.user[0].rejected">
            <h4>Su propuesta ha sido rechazada</h4>
            <p>La propuesta del Neologismo: <strong>{{ form.neologisme }}</strong>, ha sido rechazada por la siguiente razón: <br>
            {{ form.user[0].mssg }}
            <br>
            <strong>Si usted lo desea puede modificar la información requerida, y el neologismo sera evaluado nuevamente.
                Gracias por su atención
            </strong>
        </p>

            <router-link :to="{name: 'm-proposal',params: { userid: $route.params.userid ,neoId: $route.params.neoId}}" class="bttn-app" style="background-color: var(--fail) !important">Modificar</router-link>
        </div>

        <div class="descriptions-card">
            <h4>Contextos</h4>
        <div v-for="(value,index) in form.descriptions" :key=index >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.value}}</div>
        </div>
        </div>
        <div class="descriptions-card">
            <h4>Fuentes</h4>
        <div v-for="(value,index) in form.sources" :key=index >
            <div v-if="index<3" class="descriptions">{{ index }}.- {{ value.value }}</div>
        </div>
        </div>

        <div class="image-card" v-if="form.img!=null">
            <b-img thumbnail :src="require(`../assets/images/${form.img}`)"  alt="Responsive image"></b-img>
        </div>

        <div class="user-tag" >
            <div>Creado por: {{ form.user[0].user }} </div> 
            <div>{{ form.user[0].date }} </div>
        </div>
        <div class="admin-options" v-if="(login.linguist || login.admin)&&form.proposal">
            <b-button class="bttn-app" v-on:click="submit(form.id)" style="background-color: var(--success) !important"> Aceptar propuesta </b-button>
            <b-button class="bttn-app" :to="{name: 'r-neologismes',params: { userid: $route.params.userid ,neoId: $route.params.neoId}}"  style="background-color: var(--fail) !important"> Rechazar propuesta </b-button>
        </div>

        <router-link v-if="form.proposal" tag="b-button" class="bttn-app" :to="{name: 'm-neologismes',params: { userid: $route.params.userid ,neoId: $route.params.neoId}}" > Modificar propuesta </router-link>
    </div>

</template>

<script>
import axios from 'axios'
export default {
    beforeCreate(){
    axios.get("http://localhost:3000/neologismes/" + this.$route.params.neoId)
        .then(response_neo => {
            this.form = response_neo.data;

    axios.get('http://localhost:3000/login/1')
          .then(response_log => {
              this.login = response_log.data;    
    
    axios.get('http://localhost:3000/users/' + response_log.data.user_id)
          .then(response_u => {
              this.form_user = response_u.data;    
          })
          })
         })
    },
    watch: {
        $route: {
            immediate: true,
            handler: function(newVal, oldVal) {
            this.showModal = newVal.meta && newVal.meta.showModal;
        }
    }
  },data() {    
        return {
            proposals: [],
            login: [],
            form: [],
            form_user: []
        };
    },
    methods:{
        seeModify(){
            return this.form.proposal && ((this.form.user[0].user_id == this.login.user_id) || (this.loginlogin.admin || this.login.admin))
        },
        seeLiked(){
            return this.form_user.fav_neo.includes(this.form.id);
        },
      like(){
          if(!this.form_user.fav_neo.includes(this.form.id)){
          var payload = {liked:this.form.liked+1}; 
            axios.patch("http://localhost:3000/neologismes/" + this.$route.params.neoId, payload)
                .then(function( response ){
                }.bind(this));
          this.form_user.fav_neo.push(this.form.id);
            axios.patch("http://localhost:3000/users/" + this.login.user_id, {fav_neo: this.form_user.fav_neo})
                .then(function( response ){
                }.bind(this));
        this.form.liked = this.form.liked+1; 
          }
        },
   
      submit(id){
        var payload = {
                proposal:false, 
                user:[{
                    user_id: this.form.user[0].user_id,
                    user: this.form.user[0].user,
                    date: this.form.user[0].date,
                    rejected: false,
                    mssg: "",
                }],
            }
            axios.patch('http://localhost:3000/neologismes/' + id, payload)
                .then(function( response ){
                    // Handle success
                }.bind(this));
            this.$router.push({ path: `/` })
        }
    },
}
</script>


<style lang="scss" scoped>
.card-body{
  display: flex;
  flex-direction: column;
  overflow: scroll;
  
  align-content: center;
}
.descriptions{
    margin-bottom: 2%;
    padding: 1%;
    text-align: left;
    border-left: 10px solid var(--border-left);
}
.card-neo-header{
    display:flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
}
.user-tag{
    display:flex;
    flex-direction: column;
    padding-bottom: 5%;
    color: grey;
    font-size: 14px; 
}
.descriptions-card{
    border-bottom: 1px solid var(--border);
}

h4{
    text-align: left;
    margin-top: 1%;
}

.img-thumbnail{
    margin: 2% 0 2% 0;
    background-color:var(--border-left) ;
}
.admin-options{
    display: flex;
    justify-content: space-evenly;

}
.rejected-neologisme{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin-top: 2%;
    border: 2px solid var(--fail);
}

.rejected-neologisme > h4{
    border-bottom: 1px solid var(--border);
    margin: 2%
}

.card-body > button{
    max-height: 3rem;
}

.admin-options{
    margin-bottom: 3%;
}

.rejected-neologisme-admin{
    overflow: scroll;
    max-height: 30rem;
}
</style>