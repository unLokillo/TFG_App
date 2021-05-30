<template>
<div class="v-user-body">
    <Header/>
    <div class="top-menu">
        <div class="left-menu-card">
            <b-img :src="this.img" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img> 
            <div class="ls-menu">
            <div class="left-side-menus">
               <router-link :to="{name: 'vu-ranking',params: { userid: $route.params.userid }}" tag="div">
                <font-awesome-icon style="font-size:20px;" icon="trophy"/> 
                <strong> Posición: {{ position }}</strong> <br>
                <strong>Puntos: {{ points }}</strong>
               </router-link> 
            </div>

            <div class="left-side-menus">
                <router-link :to="{name: 'vu-badges',params: { userid: $route.params.userid }}" tag="div">
                <font-awesome-icon style="font-size:20px;" icon="award" />
                    15/20
                </router-link>
            </div>

            <div class="left-side-menus">
                <router-link :to="{name: 'f-neo',params: { userid: $route.params.userid }}" tag="div">
                <font-awesome-icon style="font-size:20px;" icon="heart" />
                    {{ liked_neo }}
                </router-link>
            </div>
        </div>
        </div>

        <div class="main-info-card">
            <div class="info-card">
                <strong> Nombre: </strong> {{ name }}
            </div>
            <div class="info-card">
                <strong> Apellido: </strong> {{ surname }}
            </div>
            <div class="info-card">
                <strong> Fecha Nacimiento: </strong> {{ date }}
            </div>
            <div class="info-card">
                <strong> Email: </strong> {{ email }}
            </div>
            <div class="info-card">
                <strong> Genero: </strong> {{ gender }}
            </div>
            <div class="info-card">
                <strong> Escuela: </strong> {{ school }}
            </div>
        </div>

        <div class="options">
            <b-dropdown right text="Opciones" class="m-2">
            <!--<font-awesome-icon style="font-size:30px;" icon="cog"/>-->
                 <b-dropdown-item :to="{name: 'm-perfil',params: { userid: $route.params.userid}}">Modificar Perfil</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item>Cambiar Idioma</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item :to="{name: 'n-error',params: { userid: $route.params.userid}}">Notificar Error</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item >
                    <download-csv :data   = "neologismes" name    = "filename.csv">
	                Descargar información Neologismos 
                    </download-csv>
                </b-dropdown-item>
            </b-dropdown>
        </div>
    </div>
    
    <div class="bottom-menu">
        <h4>Neologismos creados y Propuestas</h4>
        <div class="user-rankings">
            <Accepeted_Neos/>
            <Non_Accepeted_Neos/>
        </div>
    </div>

         
     <div v-if="showModal" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
</div>    
</template>

<script>
import Accepeted_Neos from '@/components/User_View/Accepted-Neo-Menu.vue'
import Non_Accepeted_Neos from '@/components/User_View/Proposed-Neo-Menu.vue'
import Header from '@/components/Header/Header.vue'
import axios from 'axios'
export default {
    name: 'View-User',
    components: {
      Accepeted_Neos,
      Non_Accepeted_Neos,
      Header
    },
    created(){
        axios.get('http://localhost:3000/users/' + this.$route.params.userid)
        .then(response => {
            //this.name = response.data[0].name;
            console.log(response.data);
            this.name = response.data.name;
            this.surname = response.data.surname;
            this.email = response.data.email;
            this.date = response.data.date;
            this.gender = response.data.gender;
            this.school = response.data.school;
            this.points = response.data.points;
            this.position = response.data.position;
            this.img = response.data.img;
        });
        axios.get('http://localhost:3000/neologismes')
        .then(response => {
            this.neologismes = response.data;
        });
    },
    methods: {
      toCSV: function(){  
          axios.get('http://localhost:3000/neologismes')
        .then(response => {
            var array = typeof response.data != 'object' ? JSON.parse(response.data) : response.data;
            var str = '';
           for (var i = 0; i < array.length; i++) {
                var line = '';
                for (var index in array[i]) {
                    if (line != '') line += ','
                    line += array[i][index];
                }
                str += line + '\r\n';
            }
            // Convert Object to JSON
            var encodedUri = encodeURI(str);
            var link = document.createElement("a");
            link.setAttribute("href", encodedUri);
            link.setAttribute("download", "my_data.csv");
            document.body.appendChild(link); // Required for FF
            link.click();
            document.body.removeChild(link);
        });
        }
    },
    watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },
  data(){
      return{
          liked_neo: 0,
          showModal: false,
          mainProps: {width: '200%', height:'200%', class: 'm1' },
          name: '', 
          surname: '',
          email: '',
          date: '',
          gender: '',
          school: '',
          img: '',
          points: 0,
          position: 0,
          neologismes: []
      }
  }
}
</script>

<style lang="scss" scoped>
.top-menu{
    display: grid;
    grid-template-columns: 2fr 5fr 1fr;
    margin: 3%;
}
.bottom-menu > h4{
  display: flex;
  margin: 2%;
  border-bottom: 1px solid var(--border);
}
.left-menu-card {
    padding: 4%;
    border-right: 2px solid var(--border);
}

  .ls-menu{
      border: 2px solid var(--border);
      background-color: var(--second-color);
      margin: 8% 0 0 0;
  }

.left-side-menus{

    padding: 2%;
    background-color: var(--third-color);
}


.main-info-card{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin: 5%;
    background-color: var(--third-color)
}

.info-card{
    border-left: 10px solid var(--border-left);
    padding-left: 2%;
    margin-bottom: 2%;
    margin-top: 2%;
    text-align: left;
}
.user-rankings{
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: 1fr 1fr;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba($color: #000000, $alpha: 0.6);
  
}
.modal-content {
    width: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    overflow: scroll;
  }
  .options-bttn > button{
      padding: 10% !important;
  }
</style>
