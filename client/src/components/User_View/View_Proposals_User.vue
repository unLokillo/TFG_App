<template>
    <div class="all-neologismes-card">
        <div class="top-all-neologismes">
            <h5> Propuestas de Neologismo </h5>
                <router-link :to="{ name: 'vUser',params: { userid: user_id } }" class="user-bttn" tag="div">
                <font-awesome-icon icon="times"/>
            </router-link>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index">
                <h5>{{ value.neologismo }}</h5>
            <div v-if="value.accepeted">
            <font-awesome-icon style="font-size: 20px;color: darkred;" icon="times-circle"/> Rechazada
            </div>

            <div class="neo_card_pendent" v-else>
            <font-awesome-icon style="font-size: 20px;color: darkorange;" icon="question-circle"/> Pendiente 
            </div>
         <b-button>+</b-button>
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
                {neologismo: 'Neologismo 1',accepeted: true},
                {neologismo: 'Neologismo 2',accepeted: false},
                {neologismo: 'Neologismo 3',accepeted: false},
                {neologismo: 'Neologismo 4',accepeted: true},
                {neologismo: 'Neologismo 5',accepeted: true},
                {neologismo: 'Neologismo 6',accepeted: true}
                ]
        }
    }
}
</script>

<style>
.top-all-neologismes{
    margin: 30px;
    border-bottom: 1px solid grey;
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
    border: 1px solid black;
    margin: 5%;
}

</style>