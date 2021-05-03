<template>
    <div class="header-card">
        <Sidebar/> 
        <div class="main-section">
            <!--<SearchBar/>-->
           <a href="/" class="title-header">Neologismos</a>
            </div>
        <UserButton/>
    </div>
</template>
<script>
// @ is an alias to /src
import Sidebar from '@/components/Header/SideBar.vue'
import UserButton from '@/components/Header/HeaderUserButton.vue'
import SearchBar from '@/components/Header/SearchBar.vue'
export default {
  name: 'Home',
  components: {
      Sidebar,
      UserButton,
      SearchBar
  }
}
</script>
<style>
.header-card{
    width: 100%;
    height: 5%;
    background: rgb(123, 123, 243);
    display: grid;
    grid-auto-flow: column;
    grid-auto-columns: 1fr 5fr 1fr;
}

.main-section{
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-header{
    color: black !important;
    text-decoration: none !important;
    letter-spacing: 6px;
    font-size: 22px
}
</style>