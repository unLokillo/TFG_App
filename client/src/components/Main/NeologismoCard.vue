<template>
    <div class="card-body">
        <div class="card-header">
            <h2>{{ name }}</h2>
            <div class="neo-likes"><font-awesome-icon icon="heart"/> {{ likes }}</div> 
        </div>
        <div class="descriptions" v-for="(value,index) in descriptions" :key=index >
            <div v-if="index<3">{{ index }}.-{{ value.content }}</div>
        </div>

        <div class="user-tag">
            {{ creator }}
            {{ date }}
        </div>
        <router-link :to="`/view-neologisme`" tag="b-button"> </router-link>
    </div>

</template>

<script>
export default {
    data() {
        return {
            id: 0,
            name: 'Palabra',
            creator: 'User1 Surname ',
            date: '31/09/1997',
            likes: 10,
            descriptions: [
                {id:0,content:"Definicion 1"},
                {id:1,content:"Esto es un texto de prueba"},
                {id:2,content:"Texto muy muy muy muy muy muy muy muy muy muy muy muy muy largo"},
                {id:3,content:"Pedazo de palabra cruck"}
            ]
        };
    },
}
</script>


<style>
.card-body{
    background-color: lightblue;
    margin: 40px 10px 40px 10px;
}
.card-header{
    display:flex;
    justify-content: space-between;
}
.user-tag{
    display:flex;
    flex-direction: column;
    justify-content: space-between;
    border: 1px solid black;
}
</style>