<template>
<div class="header-img">
    <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div" v-if="logged">
        <b-avatar src="https://picsum.photos/300/150/?image=41"></b-avatar> jajaja ahora si 
    </router-link>
    <router-link :to="`/login`" tag="div" v-else>
        Log in
    </router-link>
    <div v-if="showModalLog" class="modal-route">
        <div class="modal-content">
            <router-view></router-view>
        </div>
    </div>
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
            showModalLog: false,
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
}
.user-bttn{
    cursor: pointer;
}

.header-img:hover{
    background-color: aqua;
}

.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  background: rgba($color: #000000, $alpha: 0.5);
  .modal-content {
    width: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
  }
}
</style>