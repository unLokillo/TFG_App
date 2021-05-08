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
export default {
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
            user_id: '123456789',
            logged: false
        }
    }
}
</script>

<style lang="scss" scoped>
.header-img{
    padding: 5%;
    border-left: solid 1px black;
    display: flex;
    justify-content: center;
    align-items: center;
}
.user-bttn{
    cursor: pointer;
}

.header-img:hover{
    background-color: aqua;
}

</style>