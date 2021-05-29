<template>
<div class="header-img">
    <router-link :to="{ name: 'vUser',params: { userid: login_info.user_id } }" class="user-bttn" tag="div" v-if="login_info.logged">
        <b-avatar :src="login_info.img"></b-avatar> {{ login_info.email_or_user }} 
    </router-link>
    <router-link :to="`/login`" tag="div" v-else>
        Log in 
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
            });
    },
    watch: {
    $route: {
      immediate: true,
      handler: function(newVal, oldVal) {
        this.showModal = newVal.meta && newVal.meta.showModal;
      }
    }
  },
    data() {
        return {
            showModal: false,
            user_id: '',
            login_info: []
        }
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