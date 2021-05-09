<template>
  <div id="app">
    <Header/>
    <router-view></router-view>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header/Header.vue'
export default {
  name: 'Home',
  components: {
    Header
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
input {
  border-radius: 0px !important;
}

a {
  color: black !important;
  text-decoration: none !important;
}

a:hover{
  color: #42b983 !important;
}


.modal-route {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
    border-radius: 0px !important;
  background: rgba($color: #000000, $alpha: 0.5);
  .modal-content {
    width: 50%;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    min-height: 50% !important;
    max-height: 80% !important;
    min-width: 65% !important;
    max-width: 65% !important;
    overflow: scroll;
    display: flex;
    justify-content: center;
    background-color: #e7e7e7;
    header{
      position: absolute;
      right: 5%;
      top: 5%;
    }
  }
}

  .modal-content > div{
    position: absolute;
    height: 100%;
    width: 100%;
  }

</style>
