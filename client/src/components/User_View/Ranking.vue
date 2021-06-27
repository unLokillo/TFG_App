<template>
    <div class="v-ranking-card">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="v-ranking-title">
            <h3>Participantes destacados</h3>
        </div>
        <div class="v-ranking-user" v-for="(value,index) in users" :key="index">
            <div class="position-badge" :style="asign_color(value.position)"> <strong> {{ value.position }} </strong></div>
            <div class="avatar-card">
                <b-avatar :src="require(`../../assets/images/${value.image}`)"></b-avatar> 
                {{value.name}}
            </div>
            <div class="v-ranking-points">
                <font-awesome-icon style="font-size:15px;" icon="trophy"/>
                {{  value.points  }}
            </div>

            <div >
            <b-dropdown right text="Opciones" class="m-2" v-if="logged.admin">
                <b-dropdown-item v-on:click="addPrivileges('linguist',value.id)"> Convertir en Lingüista </b-dropdown-item>
                <b-dropdown-item v-on:click="addPrivileges('admin',value.id)"> Convertir en Administrador </b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item v-on:click="addPrivileges('admin',value.id)" v-if="value.linguist"> <div style="color: red !important;"> Quitar privilegios de Lingüista </div> </b-dropdown-item>
                <b-dropdown-item v-on:click="addPrivileges('admin',value.id)" v-if="value.admin"> <div style="color: red !important;"> Quitar privilegios de Administrador </div> </b-dropdown-item>
                <b-dropdown-item v-on:click="deleteData(value.id)"> <div style="color: red !important;"> Eliminar Usuario </div> </b-dropdown-item>
            </b-dropdown>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    created() {
        axios.get('http://localhost:3000/users')
          .then(response => {
              for (let index = 0; index < response.data.length; index++) {
            if (!response.data[index].admin) {
                this.users.push(response.data[index]);
            }
        }
    });

    axios.get('http://localhost:3000/login/1')
          .then(response => {
              this.logged = response.data;
            });
    },
    data(){
        return{
            admin: true,
            users: [],
            logged: []
        }
    },
    methods: {
        asign_color: function(pos){
            var style  = {};
            switch(pos){
                default: style.backgroundColor = "var(--buttons)"; break;
                case 1: style.backgroundColor = "var(--gold) "; break;
                case 3: style.backgroundColor = "var(--bronze)"; break;
                case 2: style.backgroundColor = "var(--silver)"; break;
            }
            return style;
        },

    deleteData(id) {
        axios.delete('http://localhost:3000/users/' + id)
            .then(response => {});
        },
    addPrivileges(type,id){
        var payload={};
        switch(type){
            case 'linguist': payload={linguist:true}; break;
            case 'admin': payload={admin:true}; break;
        }
        axios.patch('http://localhost:3000/users/' + id, payload).then(response_l => {
      });
    }
    }
}
</script>

<style>
.v-ranking-title{
    border-bottom: 1px solid var(--border);
    margin: 2%;
}

.v-ranking-points{
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.v-ranking-user{
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 3rem;
    border: 1px solid var(--border);
    margin: 2%;
}

.position-badge{
    display: flex;
    align-items: center;
    width: 20%;
    height: 100%;
    justify-content: center;
    color: var(--letter-color);
    font-size: 20px;
}
.avatar-card{
    width: 30%;
    display: flex;
    justify-content: inherit;
    align-items: center;
}

</style>