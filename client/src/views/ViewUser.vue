<template>
<div class="v-user-body">
    <div class="top-menu">
        <div class="left-menu-card">
            <b-img src="https://picsum.photos/300/150/?image=41" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img> 
            <div class="badges_menu-info">
               <router-link :to="{name: 'ranking',params: { userid: $route.params.userid }}" tag="div">
                <font-awesome-icon style="font-size:20px;" icon="trophy"/>
               </router-link> 
            </div>

            <div class="points-info">
                <router-link :to="{name: 'badges',params: { userid: $route.params.userid }}" tag="div">
                <font-awesome-icon style="font-size:20px;" icon="award" />
                    15/20
                </router-link>
            </div>
            <div class="bio-info">

            </div>
        </div>

        <div class="main-info-card">
            <div class="info-card">
                <strong> Name: </strong> {{ name }}
            </div>
            <div class="info-card">
                <strong> Surname: </strong> {{ surname }}
            </div>
            <div class="info-card">
                <strong> Name: </strong> {{ name }}
            </div>
            <div class="info-card">
                <strong> Name: </strong> {{ name }}
            </div>
            <div class="info-card">
                <strong> Name: </strong> {{ name }}
            </div>
        </div>

        <div class="options">
            <font-awesome-icon style="font-size:30px;" icon="cog"/>
        </div>
    </div>
    
    <div class="bottom-menu">
        <h3>Neologismos creados y Propuestas</h3>
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
export default {
    name: 'View-User',
    components: {
      Accepeted_Neos,
      Non_Accepeted_Neos
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
          showModal: false,
          mainProps: {width: '200%', height:'200%', class: 'm1' },
          name: "User1", 
          surname: "UserSurname1 "
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

.left-menu-card {
    padding: 4%;
    border-right: 2px solid var(--border);
}

.badges_menu-info{
    margin: 8%;
}

.main-info-card{
    display: flex;
    flex-direction: column;
    margin: 5%;
    background-color: brown
}

.info-card{
    border-left: 10px solid red;
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
</style>
