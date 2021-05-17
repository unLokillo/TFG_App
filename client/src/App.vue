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
:root{
  --main-color: #e0e5eb;
  --secondary-color: #c5cece;
  --third-color: rgb(245, 245, 245);
  --border: rgb(156, 155, 155);
  --border-left: rgb(58, 92, 245);
  --letter-color: rgb(245, 245, 245);
  --buttons: rgb(52, 129, 192);
  --buttons_hover: rgb(40, 96, 143);
  --success: #69b00b;
  --fail: #b00b69;
  --gold: #f7c628;
  --silver: #cac6c6;
  --bronze: #be5e10;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: var(--main-color);
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
.bttn-app{
  background-color: var(--buttons) !important;
  border-radius: none !important;
  border: none !important;
 // padding: 2% !important; 
 height: 100% !important;
  color: var(--letter-color) !important;
}

button{
  background-color: var(--buttons) !important;
  border-radius: none !important;
  border: none !important;
  //padding: 2% !important; 
  color: var(--letter-color) !important;
}

input {
  border-radius: 0px !important;
}

textarea{
  border-radius: none !important;
  max-height: 3rem;
}

header{
  width: 100%;
}

a {
  color: black !important;
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
    height: 100%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    min-height: 50% ;
    max-height: 80% ;
    min-width: 65% !important;
    max-width: 65% !important;
    overflow-y: auto;
    overflow-x: none;
    display: flex;
    justify-content: center;
    background-color: #e7e7e7;
  }
}

  .close-modal{
margin-right: 10%;
display: flex;
flex-direction: row-reverse;
width: 100%;
  }
  .modal-content > div{
    position: absolute;
    height: 100%;
    width: 100%;
  }

</style>
