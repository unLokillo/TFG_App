<template>
<div class="header-img">
    <router-link :to="{ name: 'vUser',params: { userid: login_info.user_id } }" class="user-bttn" tag="div" v-if="login_info.logged">
        <b-avatar :src="require(`../../assets/images/${login_info.img}`)"></b-avatar> {{ user_info.nickname }} 
    </router-link>
    <router-link :to="`/login`" tag="div" v-else>
        Iniciar sesión
    </router-link>
</div>
</template>

<script>
import axios from 'axios';
export default {
    created() {
        axios.get('http://localhost:3000/login/1')
          .then(response => {
              this.login_info = response.data;
        axios.get('http://localhost:3000/users/' + response.data.user_id)
          .then(response_u => { 
              this.user_info = response_u.data;
            });
            });
    },
    data() {
        return {
            filename: 'Under_construction.png',
            user_info: [],
            showModal: false,
            user_id: '',
            login_info: []
        }
    },
    watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    },
}
}
</script>

<style lang="scss" scoped>
.header-img{
    padding: 5%;
    border-left: solid 1px var(--border);
    background-color: var(--buttons);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%; 
    height:100%;
    cursor: pointer;
}
.header-img:hover{
     transition: all .4s ease-in-out;
    background-color: var(--buttons_hover);
}

</style>