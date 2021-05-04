<template>
    <div class="all-neologismes-card">
        <div class="top-all-neologismes">
            <h5> Neologismos Aceptados </h5>
            <font-awesome-icon icon="times"/>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index">
                <h5>{{ value.neologismo }}</h5>
                <div>
                    <font-awesome-icon icon="heart"/> {{ value.likes }}
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