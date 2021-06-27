<template>
    <div class="bages-section">
        <div class="close-modal"><a @click="$router.go(-1)"> <font-awesome-icon style="font-size: 140%;" icon="times"/> </a></div>
        <div class="top-badges_menu-section">
        <h3>Logros</h3>
        </div>
        <div class="main-section-badges">
            <h5>Logros del participante</h5>
            <div v-for="(value,index) in badges" :key="index" class="neologismes-badges">
            <div v-for="(value2,index2) in value" :key="index2"  class="neologismes-badges-card" >
                <h6>{{ value2.name }}</h6>
                <b-img :src="value2.img" v-bind="mainProps" rounded alt="Badge Img" v-if="!value2.completed"></b-img>
                <b-img :src="value2.img" v-bind="mainProps" style="opacity:0.5" rounded alt="Badge Img" v-else></b-img>
                <p > {{ value2.description }}</p>
                <div class="progress-bar-div">
                <b-progress max="100" v-if="!value2.completed">
                    <b-progress-bar :value="value2.percentage" variant="success"></b-progress-bar>
                </b-progress>
                <p v-if="!value2.completed"> {{ value2.percentage/10 }}/10 </p>
                <p v-else style="font-size:14px"> Completado el día: {{ value2.completed_date }} </p>
                </div>
             </div>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'View-User',
created() {
        axios.get('http://localhost:3000/badges')
          .then(response => {
              this.badges = new Array(Math.ceil(response.data.length / 4))
                    .fill()
                    .map(_ => response.data.splice(0, 4))
            });
    },
    data(){
        return{
            mainProps: {width: 75, height: 75, class: 'm1' },
            badges: [],
            labels: ["Usuarios", "Neologismos"]
        }
    }
}
</script>

<style>
.top-badges_menu-section{
    display: flex;
    justify-content: space-around;
    flex-direction: column;
    padding: 2%;
    border-bottom: 1px solid var(--border);
    align-items: center;
}

.neologismes-badges{
    display: flex;
}

.neologismes-badges-card{
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid var(--border);
    margin: 2%;
    max-width: 20%;
}

.neologismes-badges_menu > div{
    margin: 3%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.progress-bar-div{
    width: 90%;
}

.bages-section{
    padding: 2%;
}
</style>