<template>
<div class="header-img">
    <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div" v-if="logged">
        <b-avatar src="https://picsum.photos/300/150/?image=41"></b-avatar> User_1 
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
              this.logged = response.data.logged;
              this.user_id = response.data.user_id;
              console.log(response.data.logged);
              console.log(response.data.user_id);
            });
    },
    mounted(){
         axios.get('http://localhost:3000/login/1')
          .then(response => {
              this.logged = response.data.logged;
              this.user_id = response.data.user_id;
              console.log(response.data.logged);
              console.log(response.data.user_id);
            });
            this.$forceUpdate()
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
            logged: false
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