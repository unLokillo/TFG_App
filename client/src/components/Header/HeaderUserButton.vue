<template>
<div class="header-img">
    <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div" v-if="logged">
        <b-avatar src="https://picsum.photos/300/150/?image=41"></b-avatar> jajaja ahora si 
    </router-link>
    <router-link :to="`/login`" tag="div" v-else>
        Log in
    </router-link>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user_id: '123456789',
            logged: true
        }
    }
}
</script>

<style>
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
</style>