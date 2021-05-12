<template>
    <div class="all-neologismes-card">
        <div class="top-all-neologismes">
            <h5> Neologismos Aceptados </h5>
            <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div">
                <font-awesome-icon icon="times"/>
            </router-link>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index">
                <h5>{{ value.neologismo }}</h5>
                <div>
                    <font-awesome-icon icon="heart"/> {{ value.likes }}
                </div>
                 <b-button class="bttn-app" :to="{name: 'v-neologismes',params: { userid: $route.params.userid ,neoId: value.id}}"> +</b-button>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    data(){
        return{
            user_id: '123456789',
            neologismes: [
                {neologismo: 'Neologismo 1',likes: '20'},
                {neologismo: 'Neologismo 2',likes: '25'},
                {neologismo: 'Neologismo 3',likes: '55'},
                {neologismo: 'Neologismo 4',likes: '45'},
                {neologismo: 'Neologismo 5',likes: '65'},
                {neologismo: 'Neologismo 6',likes: '65'}
                ]
        }
    }
}
</script>

<style>
.top-all-neologismes{
    margin: 30px;
    border-bottom: 1px solid var(--border);
}

.all-neologismes-card{
    height: 100%;
    max-height: 500px;
    overflow: scroll;
}

.neologisme-cards > div{
    padding: 10px;
    display: flex;
    justify-content: space-evenly;
    border: 1px solid var(--border);
    margin: 5%;
}

</style>