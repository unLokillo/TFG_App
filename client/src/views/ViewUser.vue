<template>
<div class="v-user-body">
    <div class="top-menu">
        <div class="left-menu-card">
            <b-img src="https://picsum.photos/300/150/?image=41" v-bind="mainProps" rounded="circle" alt="Circle image"></b-img> 
            <div class="badges-info">
                <font-awesome-icon style="font-size:20px;"
                icon="trophy"/>
                asdfg
            </div>
            <div class="points-info">
                <font-awesome-icon style="font-size:20px;" icon="award" />
                asdf
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
</div>    
</template>

<script>
import Accepeted_Neos from '@/components/User_View/Ran_Accepted_Neo.vue'
import Non_Accepeted_Neos from '@/components/User_View/Ran_NonAccepted_Neo.vue'
export default {
  name: 'View-User',
  components: {
    Accepeted_Neos,
    Non_Accepeted_Neos
  },
  data(){
      return{
          mainProps: {width: '200%', height:'200%', class: 'm1' },
          name: "User1", 
          surname: "UserSurname1 "
      }
  }
}
</script>

<style>
.top-menu{
    display: grid;
    grid-template-columns: 2fr 5fr 1fr;
    margin: 3%;
}

.left-menu-card {
    padding: 4%;
    border-right: 2px solid black;
}

.badges-info{
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
</style>
