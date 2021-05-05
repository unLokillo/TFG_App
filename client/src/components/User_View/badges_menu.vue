<template>
    <div class="bages-section">
        <div class="top-badges_menu-section">
        <h5>Logros</h5>
        <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div">
                <font-awesome-icon icon="times"/>
            </router-link>
        </div>

        <div class="main-section">
            <div class="neologismes-badges_menu">
                <Badge/>
            </div>
            <div class="game-badges_menu">

            </div>
        </div>
    </div>
</template>

<script>
import Badge from '@/components/User_View/Badge.vue'
export default {
  name: 'View-User',
  components: {
    Badge
  },
    data(){
        return{
            user_id: '123456789',
        }
    }
}
</script>

<style>
.top-badges_menu-section{
    display: flex;
    justify-content: space-around;
    padding: 2%;
    border-bottom: 1px solid black;
}
</style>