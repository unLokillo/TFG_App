<template>
    <div class="all-neologismes-card">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="top-all-neologismes">
            <h5> Neologismos aceptados </h5>
        </div>

        <div class="neologisme-cards">
            <div v-for="(value,index) in neologismes" :key="index">
                <b-avatar :src="value.img"></b-avatar>
                <h5>{{ value.neologisme }}</h5>
                
                <div>
                    <font-awesome-icon icon="heart"/> {{ value.liked }}
                </div>
                 <b-button class="bttn-app" :to="{name: 'v-neologismes',params: { userid: $route.params.userid ,neoId: value.id}}"> +</b-button>
            </div>
        </div>

    </div>
</template>

<script>
    import axios from 'axios';
export default {
    created(){
        axios.get('http://localhost:3000/login/1')
        .then(response_l => {
            this.login = response_l.data;
          axios.get('http://localhost:3000/users/' + response_l.data.id)
           .then(response_u => {
             axios.get('http://localhost:3000/neologismes')
             .then(response => {
                 if(response_l.data.admin || response_l.data.linguist){
                     for (let index = 0; index < response.data.length; index++) {
                         if (!response.data[index].proposal) {
                        this.neologismes.push(response.data[index]);
                    }
                }
            }else{
                for (let index = 0; index < response.data.length; index++) {
                    if (response_u.data.accepted_neo.includes(response.data[index].id)) {
                        this.neologismes.push(response.data[index]);
                    }
                }
            }
            })
            })
          })
    },
    data(){
        return{
            neologismes: [],
            login:[]
        }
    }
}
</script>

<style>
.top-all-neologismes{
    border-bottom: 1px solid var(--border);
    margin: 2%;
}

.all-neologismes-card{
    height: 100%;
    max-height: 700px;
    overflow: scroll;
}


.neologisme-cards > div{
    border-left: 14px solid var(--border-left) !important;
    padding: 10px;
    display: flex;
    justify-content: space-evenly;
    border: 1px solid var(--border);
    margin: 5%;
    align-items: center;
}

</style>