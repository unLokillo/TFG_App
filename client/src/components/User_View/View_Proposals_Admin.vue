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
                <div>
                    <font-awesome-icon icon="heart"/> {{ value.likes }}
                </div>
                <b-dropdown text="Acciones">
                    <b-dropdown-item href="#">Aceptar Propuesta</b-dropdown-item>
                    <b-dropdown-item href="#">Rechazar Propuesta</b-dropdown-item>
                    <b-dropdown-item style="color: red;" href="#">Eliminar Propuesta</b-dropdown-item>
                </b-dropdown>
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